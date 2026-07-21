def double_all(numbers):
  res = []
  for n in numbers:
    res.append(n*2)
  return res

n = int(input())
numbers = []
for _ in range(n):
  numbers.append(int(input()))

print(*(double_all(numbers)))

# list compresion Version
#def double_all(numbers):
#  return [x*2 for x in numbers]
#n = int(input())
#numbers = [int(input()) for _ in range(n)]
#print(*double_all(numbers))
