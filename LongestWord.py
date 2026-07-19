# Read the sentence
sentence = input().strip()

# Find and print the longest word
res = sentence.split()
big = res[0]
for i in res:
  if len(i) > len(big):
    big = i
print(big)
  
