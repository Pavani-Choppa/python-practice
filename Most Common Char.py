word = input().strip().lower()

# Find and print the most common character
di = {}
for i in word:
  if i in di:
    di[i] += 1
  else:
    di[i] = 1
mc = 0
rc = None
for ch,c in di.items():
  if c > mc:
    mc = c
    rc = ch
print(rc)
    
  
