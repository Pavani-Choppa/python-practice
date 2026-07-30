sentence = input().strip().lower()

# Count and print word frequencies
# Split into words
words = sentence.split()

# Count frequencies
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Print in alphabetical order
for word in sorted(freq):
    print(f"{word}:{freq[word]}")
