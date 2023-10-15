from string import punctuation
from collections import defaultdict


def words_count(text: str) -> dict:
    for ch in punctuation:
        text = text.replace(ch, "")
    freq = defaultdict(int)
    for word in text.lower().split():
        freq[word] += 1
    return freq


if __name__ == "__main__":
    print(
        words_count("This is a very very simple simple txt")
    )
