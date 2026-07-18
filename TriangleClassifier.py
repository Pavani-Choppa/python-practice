# Read three sides
a = int(input())
b = int(input())
c = int(input())

# Classify and print
if (a+b > c) and (b+c > a) and (a+c > b):
  if a == b == c:
    print("Equilateral")
  elif a == b or b == c or c == a:
    print("Isosceles")
  else:
    print("Scalene")
else:
  print("Not a triangle")
