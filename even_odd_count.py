n = int(input())
ce , co = 0 , 0
sum = 0
while n > 0:
    rem = n % 10
    if rem % 2 == 0:
        ce +=1
    else:
        co += 1
    n //= 10
print(f"Even Count : {ce} \nOdd Count : {co}")
