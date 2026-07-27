n = int(input())
count = 0
sum = 0
while n > 0:
    rem = n % 10
    if rem % 2 == 0:
        sum += rem
    n //= 10
print(sum)
