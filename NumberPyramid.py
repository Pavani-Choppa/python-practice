# Read N
n = int(input())

# Print the number pyramid
for i in range(n+1):
  for j in range(i):
    print(j+1,end=" ")
  print()
