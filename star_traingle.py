# Read N
n = int(input())

# Print the star triangle
for i in range(n+1):
  for j in range(i):
    print("*",end="")
  print()
