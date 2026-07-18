# Read the sentence
sentence = input().strip()

# Capitalize first letter of each word and print
st = sentence.split()
cap = [i.capitalize() for i in st]
print(' '.join(cap))
