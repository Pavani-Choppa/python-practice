# Read the number as a string
num = input().strip()

# Count and print digit frequenciesvisit = []
visit = []
num = sorted(num)

for i in num:
  if i not in visit:
    print(f"{i}:{num.count(i)}")
    visit.append(i)
