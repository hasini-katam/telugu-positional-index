import json

INDEX_FILE = "index/positional_index.json"

with open(INDEX_FILE, "r", encoding="utf-8") as file:
    positional_index = json.load(file)


def phrase_search(words):
    if len(words) == 0:
        return {}

    first_word = words[0]

    if first_word not in positional_index:
        return {}

    results = {}

    for document, positions in positional_index[first_word].items():

        current_positions = positions

        found = True

        for i in range(1, len(words)):

            word = words[i]

            if word not in positional_index:
                found = False
                break

            if document not in positional_index[word]:
                found = False
                break

            next_positions = positional_index[word][document]

            valid_positions = []

            for position in current_positions:
                if position + 1 in next_positions:
                    valid_positions.append(position + 1)

            current_positions = valid_positions

            if len(current_positions) == 0:
                found = False
                break

        if found:
            results[document] = current_positions

    return results


query = input("Enter a Telugu phrase: ").strip()

words = query.split()

results = phrase_search(words)

if len(results) == 0:
    print("\nPhrase not found.")
else:
    print("\nPhrase found.")
    print("Number of documents:", len(results))

    print("\nDocuments and positions:")

    for document, positions in results.items():
        print(document, "->", positions)