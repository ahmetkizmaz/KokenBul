# KökenBul

Analyze the linguistic origins of Turkish texts with Python

KokenBul is a Python-based tool designed to analyze the etymological origins of words in Turkish texts. By leveraging natural language processing and the TDK Dictionary API, it identifies the source language of each word and provides a clear breakdown of origin distributions within a text.

This project is useful for linguistic analysis, academic research, digital humanities projects, or anyone interested in the historical composition of Turkish vocabulary.

## Features

- NLP-based analysis of Turkish texts
- Lemmatization (root/lemma extraction)
- Word origin detection using TDK dictionary API
- Statistical breakdown of word origins (Turkish, Arabic, Persian, etc.)
- Supports direct text input or file-based analysis

## Requirements

- Python 3.6 or higher
- stanza
- requests

## Installation

1. Clone this repository:
```
git clone https://github.com/ahmetkizmaz/KokenBul.git
cd KokenBul
```

2. Install the required Python packages:
```
pip install stanza requests
```

3. Download the Turkish NLP model (first run only):
```
python KokenBul.py --download
```

## Usage

KokenBul can be used in two ways:

### 1. Direct text analysis:

```
python KokenBul.py --text “The text you want to analyze goes here”
```

### 2. Text analysis from a file:

```
python KokenBul.py --file text_file.txt
```

Note: You must specify either the --text or --file parameter on the command line.

## Output Example

```
Kelime kökenleri:
----------------
farklı: Türkçe
köken: Türkçe
kelime: Arapça
dil: Türkçe
zengin: Farsça
kılmak: Türkçe
...

Köken dağılımı:
----------------
Türkçe: 12 kelime (60.0%)
Arapça: 5 kelime (25.0%)
Farsça: 2 kelime (10.0%)
Bilinmiyor: 1 kelime (5.0%)
```

## License

This project is licensed under the MIT License.
See the `LICENSE` file for more information.
