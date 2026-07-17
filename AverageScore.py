# Read count
n = int(input())

# Read scores and calculate average
sum = 0
for i in range(n):
  num = int(input())
  sum += num
avg = sum/n
# Print the average
print("Average:",format(avg,".1f"))
