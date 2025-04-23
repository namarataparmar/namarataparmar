def frequency(s):
    words = s.split()
    freq = {}
    for i in words:
        freq[i] = freq.get(i, 0) + 1
    return dict(sorted(freq.items()))  

print(frequency("apple banana apple mango banana apple")) 
    
