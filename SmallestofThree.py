# Read three numbers
a = int(input())
b = int(input())
c = int(input())

# Find and print the smallest
#print("Smallest:",min(a,b,c))
if a < b and a < c:
	print("Smallest:",a)
elif b < a and b < c:
	print("Smallest:",b)
else:
	print("Smallest:",c)
