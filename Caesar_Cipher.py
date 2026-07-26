text = input().strip()
shift = int(input())

for ch in text:
    if 'a' <= ch <= 'z':
        new = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        print(new, end="")
    elif 'A' <= ch <= 'Z':
        new = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        print(new, end="")
    else:
        print(ch, end="")
