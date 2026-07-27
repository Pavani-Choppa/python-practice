s = input()
count = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        print("".join(s[i]+ str(count)),end="")
        count = 1

# Print the last character count
print("".join(s[-1]+ str(count)))
