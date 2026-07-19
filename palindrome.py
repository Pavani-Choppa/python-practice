def is_palindrome(word):

    # Return True if word is a palindrome, False otherwise
  if word == word[::-1]:
    return "Yes"
  else:
    return "No"
wr = input("")
print(is_palindrome(wr))
