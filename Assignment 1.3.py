import os
import string
import csv
import time
from collections import Counter
from sys import exit

start_time = time.time()

FOLDER = "sample_texts"
STOPWORDS = {
    'the','is','at','on','of','a','and','to','in','it','for',
    'that','as','with','was','were','be','this','by','an'
}
TOP_N = 50


def clean_text(text: str):
    """Lowercase, remove punctuation, split, remove stopwords."""
    text = text.lower()
    text = text.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
    return [w for w in text.split() if w and w not in STOPWORDS]


def read_all_words(folder: str):
    """Read all .txt files and return a Counter of words."""
    counter = Counter()

    try:
        files = os.listdir(folder)
    except Exception as e:
        print("Error reading folder:", e)
        return counter

    for file in files:
        if file.lower().endswith(".txt"):
            path = os.path.join(folder, file)

            try:
                with open(path, "r", encoding="utf-8") as f:
                    words = clean_text(f.read())
                    counter.update(words)
            except Exception as e:
                print(f"Skipping unreadable file: {file} ({e})")

    return counter


def write_csv(path, rows):
    """Write rows to CSV safely."""
    try:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Word", "Count"])
            writer.writerows(rows)
    except Exception as e:
        print(f"Failed to write {path}: {e}")


# ---- Main execution ----

# Check folder exists
if not os.path.isdir(FOLDER):
    print("Folder not found:", FOLDER)
    exit()

print("Reading folder:", FOLDER)

word_counts = read_all_words(FOLDER)

# Handle empty dataset safely
if not word_counts:
    print("No valid words found in text files.")
    exit()

sorted_counts = word_counts.most_common()

# Safe slicing (prevents IndexError automatically)
top_words = sorted_counts[:TOP_N]

print(f"\nTop {len(top_words)} keywords:")
for word, count in top_words:
    print(f"{word}: {count}")

# Write CSV files safely
write_csv("keyword_counts.csv", sorted_counts)
write_csv("top_keywords.csv", top_words)

# Stats (safe math)
total_words = sum(word_counts.values())
unique_words = len(word_counts)
avg_freq = total_words / unique_words if unique_words else 0

print("\nTotal words:", total_words)
print("Unique words:", unique_words)
print("Average frequency:", round(avg_freq, 2))

# Timing
elapsed = time.time() - start_time
print(f"\nTime taken: {elapsed:.2f} seconds")
print("Script is slow." if elapsed > 5 else "Good speed.")

# Output confirmation
outputs_exist = all(os.path.exists(f) for f in ("keyword_counts.csv", "top_keywords.csv"))
print("Output files generated successfully." if outputs_exist else "Error writing output files.")

print("---- END OF SCRIPT ----")
