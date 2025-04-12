import stanza
import urllib.parse
import requests
import argparse
from collections import defaultdict

def download_turkish_model():
    """Download Turkish language model if not already downloaded"""
    try:
        stanza.download("tr")
        print("Türkçe dil modeli başarıyla yüklendi.")
    except Exception as e:
        print(f"Dil modeli yüklenirken hata: {e}")
        exit(1)

def get_corrected_stems(sentence, nlp):
    """Extract lemmas (word stems) from a Turkish sentence"""
    doc = nlp(sentence)
    corrected_stems = []
    
    for sent in doc.sentences:
        for word in sent.words:
            # Skip punctuation and grammatical particles
            if word.upos in ["PUNCT", "ADP", "PART", "AUX"]:
                continue
                
            lemma = word.lemma.lower()
            pos = word.upos

            # Handle verbs
            if pos == "VERB":
                last_vowel = next((c for c in reversed(lemma) if c in 'aeıioöuü'), None)
                lemma += "mek" if last_vowel in {'e', 'i', 'ö', 'ü'} else "mak"
            # Filter single-letter non-content words
            elif len(lemma) == 1 and pos != "NOUN":
                continue

            corrected_stems.append(lemma)
    
    return corrected_stems

def get_word_origin(word):
    """Get origin of a Turkish word from TDK dictionary"""
    kelime = urllib.parse.quote(word)
    url = f"https://sozluk.gov.tr/gts?ara={kelime}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()

        if isinstance(data, list) and data and 'lisan' in data[0]:
            lang = data[0]['lisan'].split(' ', 1)[0] if data[0]['lisan'] else "Türkçe"
        else:
            lang = "Bilinmiyor"
            
        return lang
            
    except Exception as e:
        return f"Bilinmiyor (Hata: {str(e)})"

def analyze_text(text):
    """Analyze a text to find the origins of words"""
    # Stanza modelini yükle
    nlp = stanza.Pipeline("tr", processors="tokenize,mwt,pos,lemma")
    
    # Get word stems
    word_stems = get_corrected_stems(text, nlp)
    
    # Count word origins
    origin_counts = defaultdict(int)
    
    print("\nKelime kökenleri:")
    print("----------------")
    
    for word in word_stems:
        lang = get_word_origin(word)
        origin_counts[lang] += 1
        print(f"{word}: {lang}")
    
    # Print summary
    print("\nKöken dağılımı:")
    print("----------------")
    for lang, count in sorted(origin_counts.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / len(word_stems)) * 100
        print(f"{lang}: {count} kelime ({percentage:.1f}%)")
    
    return origin_counts

def main():
    parser = argparse.ArgumentParser(description='Türkçe metinlerdeki kelimelerin kökenlerini analiz eder.')
    parser.add_argument('--text', type=str, help='Analiz edilecek metin')
    parser.add_argument('--file', type=str, help='Analiz edilecek metin dosyası')
    parser.add_argument('--download', action='store_true', help='Türkçe dil modelini indir')
    
    args = parser.parse_args()
    
    if args.download:
        download_turkish_model()
        return
    
    # Get text to analyze
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as e:
            print(f"Dosya okuma hatası: {e}")
            return
    elif args.text:
        text = args.text
    else:
        parser.print_help()
        print("\nHATA: Lütfen analiz edilecek metni --text veya --file parametresi ile belirtin.")
        return
    
    analyze_text(text)

if __name__ == "__main__":
    main()
     

