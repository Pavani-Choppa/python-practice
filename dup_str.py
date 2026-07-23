s = "abcabded"
li =  ""

for i in range(len(s)):
  count = 0
  for j in range(len(s)):
    if s[i] == s[j]:
      count += 1
  if count > 1 and s[i] not in li:
    print(s[i])
    li += s[i]
