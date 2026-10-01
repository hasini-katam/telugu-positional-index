# Telugu Positional Inverted Index

## 1. About the Project

This project implements a positional inverted index for a Telugu text dataset.

A positional inverted index stores each word along with the documents in which it occurs and the positions where it occurs.

The index is used for searching Telugu words and phrases.

---

## 2. Dataset

The project uses a Telugu Text Corpus containing Telugu text documents.

The complete dataset was used for building the index.

Dataset statistics:

- Documents processed: 1736
- Total Telugu words: 318247
- Unique Telugu words: 45968

---

## 3. System Pipeline

The pipeline of the project is:

Dataset  
↓  
Read Documents  
↓  
Preprocessing  
↓  
Telugu Word Extraction  
↓  
Position Assignment  
↓  
Positional Inverted Index  
↓  
Index Storage  
↓  
Searching and Retrieval

---

## 4. Preprocessing

Each text file is read using UTF-8 encoding.

Telugu words are extracted using the Telugu Unicode range `r'[\u0C00-\u0C7F]+'`.

For every document, positions are assigned starting from 1.

Example:

తెలుగు భాష చాలా అందమైన భాష

Positions:

1 → తెలుగు  
2 → భాష  
3 → చాలా  
4 → అందమైన  
5 → భాష

---

## 5. Positional Inverted Index

The index stores information in the following form:

`word → document → positions`

Example:

తెలుగు → document1.txt → [1, 8, 20]  
తెలుగు → document2.txt → [4, 15]

This tells us that the word "తెలుగు" occurs in both documents and also gives the positions where it occurs.

The complete index is stored in `index/positional_index.json`.

---

## 6. Storage

The positional index is stored as a JSON file.

File: `index/positional_index.json`

The JSON file contains the complete index generated from the dataset.

---

## 7. Searching and Retrieval

The `search.py` program is used for single-word searching.

Run the program using `python search.py` and enter a Telugu word when prompted.

Example: `Enter a Telugu word to search: తెలుగు`

The program displays whether the word was found, the number of documents containing the word, and the positions of the word in each document.

The `phrase_search.py` program is used for phrase searching.

Run the program using `python phrase_search.py` and enter a Telugu phrase when prompted.

Example: `Enter a Telugu phrase: తెలుగు బుక్`

The program checks whether the words in the phrase occur consecutively in the same document.

For example, `తెలుగు` gives the result "Word found" with 79 documents, while `తెలుగు బుక్` gives the result "Phrase found" with 2 documents.

If a word or phrase is not present, the program displays "Word not found in the index" or "Phrase not found."

The complete sample output is available in `output/sample_output.txt`.