import json

INDEX_FILE = "index/positional_index.json"

with open(INDEX_FILE, "r", encoding="utf-8") as file:
    positional_index = json.load(file)


def search_word(word):
    if word in positional_index:
        return positional_index[word]

    return None


word = input("Enter a Telugu word to search: ").strip()

result = search_word(word)

if result is None:
    print("Word not found in the index.")
else:
    print("\nWord found.")
    print("Number of documents:", len(result))

    print("\nDocuments and positions:")

    for document, positions in result.items():
        print(document, "->", positions)