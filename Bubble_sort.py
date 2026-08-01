# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# Bubble sort with swap counting
count = 0
res=[]
for i in range(n):
    for j in range(n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j] , numbers[j+1] = numbers[j+1],numbers[j]
            count +=1
print(*numbers)
print("Swaps:",count)
