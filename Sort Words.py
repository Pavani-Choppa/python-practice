# Read input
n = int(input())
words = []
for i in range(n):
    words.append(input().strip())

# Sort and sorted()
sort = sorted(words)
for i in sort:
  print(i)
