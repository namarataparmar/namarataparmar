def convert(s):
    words = set(s.split())  
    return " ".join(sorted(words))  


print(convert("banana apple orange apple mango banana"))
