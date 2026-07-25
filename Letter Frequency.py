s = input().strip().lower()

# Count and print letter frequencies
visited = []
s = sorted(s)
# print()
for ch in s:
    if ch not in visited:   
        print(f"{ch}:{s.count(ch)}")
        visited.append(ch)
