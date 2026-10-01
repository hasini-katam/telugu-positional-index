import os

DATASET_FOLDER = "dataset/Telegu Text Corpus"

file_count = 0

for root, folders, files in os.walk(DATASET_FOLDER):
    for file in files:
        if file.endswith(".txt"):
            file_count += 1

print("Dataset check completed.")
print("Number of text files:", file_count)