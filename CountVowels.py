text = input().strip().lower()

# Count vowels and print
count = 0
for c in text:
  if c in 'aeiou':
    count += 1
print("Vowels:",count)
  
  
