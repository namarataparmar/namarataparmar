def ispalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())  
    return s == s[::-1]

print(ispalindrome("A man a plan a canal Panama"))  
print(ispalindrome("Hello")) 
