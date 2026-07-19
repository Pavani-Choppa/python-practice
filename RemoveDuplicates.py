# Read the string
text = input().strip()

# Remove consecutive duplicates and print
#res = text[0]
#for i in range(1,len(text)):
 # if text[i] != text[i-1]:
  #  res += text[i]
#print(res)

res = ""
for ch in text:
  if ch not in res:
    res += ch
print(res)
