# Read a text file, count the frequency of each word, and print the top 10 most frequent words along with their counts.
from collections import Counter

file_path = 'data.txt' 
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
words = text.split()
word_counts = Counter(words)
top_words = word_counts.most_common(10)
print("Top 10 most frequent words:")
for word, count in top_words:
    print(f"{word}: {count}")
