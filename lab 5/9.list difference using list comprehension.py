list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]


list3 = [num for num in list1 if num not in list2]
print("Numbers in list1 but not in list2:", list3)

list3 = [num for num in list1 if num in list2]
print("Numbers in list1 but not in list2:", list3)

