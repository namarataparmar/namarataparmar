import string

def ispangram(s):
    s = s.lower()
    return set(string.ascii_lowercase) <= set(s)


test_str1 = "The quick brown fox jumps over the lazy dog"
test_str2 = "Crazy Fredrick bought many very exquisite opal jewels"
print(ispangram(test_str1))  
print(ispangram(test_str2))  


