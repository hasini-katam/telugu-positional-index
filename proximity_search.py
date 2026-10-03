import json

INDEX_FILE = "index/positional_index.json"

with open(INDEX_FILE, "r", encoding="utf-8") as file:
    positional_index = json.load(file)


def proximity_search(word1, word2, distance):
    results = {}

    if word1 not in positional_index or word2 not in positional_index:
        return results

    common_documents = set(positional_index[word1]) & set(positional_index[word2])

    for document in common_documents:

        positions1 = positional_index[word1][document]
        positions2 = positional_index[word2][document]

        matches = []

        for position1 in positions1:
            for position2 in positions2:

                if abs(position1 - position2) <= distance:
                    matches.append((position1, position2))

        if len(matches) > 0:
            results[document] = matches

    return results


query = input("Enter proximity query (word1 NEAR/k word2): ").strip()

parts = query.split()

if len(parts) != 3 or not parts[1].upper().startswith("NEAR/"):
    print("Invalid query format.")
else:
    word1 = parts[0]
    word2 = parts[2]

    try:
        distance = int(parts[1].split("/")[1])

        results = proximity_search(
            word1,
            word2,
            distance
        )

        if len(results) == 0:
            print("\nNo documents found.")
        else:
            print("\nProximity match found.")
            print("Number of documents:", len(results))

            print("\nDocuments and matching positions:")

            for document, matches in results.items():
                print(document, "->", matches)

    except ValueError:
        print("Invalid distance.")