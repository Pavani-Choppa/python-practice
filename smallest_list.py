n = int(input())
small = 0
li = [int(input()) for _ in range(n)]

for i in li:
    if i < small:
        small = i
print(small)
