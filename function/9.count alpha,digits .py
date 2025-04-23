def count_alpha_digit(s):
    counts= {"alphabates":0,"digit":0}

    for char in s:
        if char.isalpha():
            counts["alphabates"] += 1
        elif char.isdigit():
            counts["digit"] += 1
    return counts



print(count_alpha_digit("namarata1212parmar2006"))        
