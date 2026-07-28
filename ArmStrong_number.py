n = int(input())

t = n
s = 0
while t > 0:
    re = t % 10
    s += re ** 3
    t //= 10
if n == s:
    print("Arm")
else:
    print("Not Arm")
