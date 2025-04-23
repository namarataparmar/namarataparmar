def create_list(list1, list2):
    return list(set(list1) & set(list2)) #intersection can be done in set only and then list conversion


print(create_list([1, 2, 3, 4], [3, 4, 5, 6]))
