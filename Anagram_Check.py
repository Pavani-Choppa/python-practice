a = input().strip().lower()
b = input().strip().lower()

# Check if anagrams and print
if sorted(a) == sorted(b):
    print("Yes")
else:
    print("No")
