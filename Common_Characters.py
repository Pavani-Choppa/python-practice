a = input().strip()
b = input().strip()

# Find and print common characters in sorted order
set_a = set(a)
set_b = set(b)
si = set_a & set_b
if not si:
  print("none")
else:
  print(''.join(sorted(si)))
