# Read the sentence
sentence = input().strip()

# Count and print the number of words
#print(len(sentence.split()),"words")
count = 0
w = False
for i in sentence:
  if i == ' ' or i == '\t' or i == '\n':
    w = False
  elif not w:
    count += 1
    w = True
print(count,"words")