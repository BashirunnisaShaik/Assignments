def palindrome(n):
    if str(n)==str(n)[::-1]:
        return "Palindrome"
    return "Not Palindrome"

print(palindrome(121))