# KökenBul

KökenBul, Türkçe metinlerdeki kelimelerin kökenlerini analiz eden bir Python aracıdır. Bu araç, TDK Sözlük API'sini kullanarak kelimelerin hangi dilden geldiğini tespit eder ve metin içindeki farklı kökenli kelimelerin dağılımını gösterir.

## Özellikler

- Türkçe metinleri doğal dil işleme teknikleriyle analiz eder
- Kelimelerin köklerini (lemma) çıkarır
- TDK sözlük veritabanı üzerinden köken bilgisini sorgular
- Metin içindeki kelimelerin köken dağılımını hesaplar

## Gereksinimler

- Python 3.6 veya üzeri
- stanza
- requests

## Kurulum

1. Bu depoyu klonlayın:
```
git clone https://github.com/username/KokenBul.git
cd KokenBul
```

2. Gerekli Python paketlerini yükleyin:
```
pip install stanza requests
```

3. İlk kullanımda Türkçe dil modelini indirin:
```
python KokenBul.py --download
```

## Kullanım

KökenBul'u iki farklı şekilde kullanabilirsiniz:

### 1. Doğrudan metin analizi:

```
python KokenBul.py --text "Analiz etmek istediğiniz metin buraya"
```

### 2. Dosyadan metin analizi:

```
python KokenBul.py --file metin_dosyasi.txt
```

Not: Komut satırında --text veya --file parametrelerinden birini belirtmeniz gerekmektedir.

## Çıktı Örneği

```
Kelime kökenleri:
----------------
farklı: Türkçe
köken: Arapça
sözcük: Türkçe
dil: Türkçe
zenginleştirmek: Farsça
...

Köken dağılımı:
----------------
Türkçe: 12 kelime (60.0%)
Arapça: 5 kelime (25.0%)
Farsça: 2 kelime (10.0%)
Bilinmiyor: 1 kelime (5.0%)
```

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## Katkıda Bulunma

Hata raporları, özellik önerileri ve pull request'ler için GitHub'da issue açabilirsiniz.