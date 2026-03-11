import re
from collections import Counter

def analyze_text(text):
    # Clean text (lowercase + remove punctuation)
    cleaned_text = re.sub(r"[^\w\s]", "", text.lower())

    # Word list
    words = cleaned_text.split()

    # Counts
    word_count = len(words)

    # Character count excluding whitespace
    char_count = len(re.sub(r"\s+", "", text))

    # Sentence count
    sentence_count = len(re.findall(r"[.!?]", text))

    # Most common words
    common_words = Counter(words).most_common(5)

    return {
        "Words": word_count,
        "Characters (no spaces)": char_count,
        "Sentences": sentence_count,
        "Top 5 Words": common_words
    }


# ---- Prompt mode ----
print("Enter a paragraph for text analysis:")
user_text = input()   # user enters text here

results = analyze_text(user_text)

print("\n--- Text Analysis Result ---")
for key, value in results.items():
    print(f"{key}: {value}")
