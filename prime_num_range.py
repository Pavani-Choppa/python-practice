s = int(input())
e = int(input())

for n in range(s,e+1):
  if n > 1:
    ip = True
    for i in range(2,n):
      if n % i == 0:
        ip = False
        break
    if ip:
      print(n,end=" ")
