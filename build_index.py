import os
import re
import json
from collections import defaultdict

DATASET_FOLDER = "dataset/Telegu Text Corpus"
INDEX_FOLDER = "index"
INDEX_FILE = "index/positional_index.json"


def get_telugu_words(text):
    words = re.findall(r'[\u0C00-\u0C7F]+', text)
    return words


positional_index = defaultdict(lambda: defaultdict(list))

document_count = 0
total_words = 0


for root, folders, files in os.walk(DATASET_FOLDER):

    for file in files:

        if file.endswith(".txt"):

            file_path = os.path.join(root, file)

            # Create a unique document name using its relative path
            document_id = os.path.relpath(
                file_path,
                DATASET_FOLDER
            )

            try:
                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    text = f.read()

            except Exception:
                print("Could not read:", document_id)
                continue

            words = get_telugu_words(text)

            document_count += 1
            total_words += len(words)

            position = 1

            for word in words:

                positional_index[word][document_id].append(position)

                position += 1


# Convert defaultdict to normal dictionaries
positional_index = {
    word: dict(documents)
    for word, documents in positional_index.items()
}


# Create index folder if it does not exist
os.makedirs(INDEX_FOLDER, exist_ok=True)


# Save the complete positional index
with open(
    INDEX_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        positional_index,
        f,
        ensure_ascii=False,
        indent=2
    )


print("Positional index created successfully.")
print("Documents processed:", document_count)
print("Total Telugu words:", total_words)
print("Unique Telugu words:", len(positional_index))
print("Index saved to:", INDEX_FILE)