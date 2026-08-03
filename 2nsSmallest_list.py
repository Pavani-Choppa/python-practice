n = int(input())

li = [int(input()) for _ in range(n)]
small = float('inf')
ss = float('inf')

for i in li:
    if i < small:
        ss = small
        small = i
    elif i < ss and i != small:
        ss = i
print(ss)
