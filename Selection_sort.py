# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Selection sort with step printing
for i in range(n-1):
    mini = i
    for j in range(i+1,n):
      if numbers[j] < numbers[mini]:
      	mini = j
    numbers[i],numbers[mini] = numbers[mini],numbers[i]
    #if numbers != sorted(numbers):
    print(*numbers)
#print(*numbers)
