from collections import Counter
reviews = ["Great product", "Not great but good", "Good quality product"]
words = " ".join(reviews).lower().split()
frequency = Counter(words)
print(frequency)
