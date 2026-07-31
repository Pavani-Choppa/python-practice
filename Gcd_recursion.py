def gcd(a, b):
    # Implement the Euclidean algorithm recursively
    if b == 0:
      return a
    return gcd(b,a%b)

a = int(input())
b = int(input())
print("GCD: " + str(gcd(a, b)))
