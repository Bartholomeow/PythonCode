def remove_duplicates(list):
    unique = set()
    i = 0
    while(i < len(list)):
        if not list[i] in unique:
            unique.add(list[i])
            i += 1
        else:
            list.pop(i)


list = [1, 2, 3, 3, 4, 5, 6, 5, 4, 3, 4, 2, 1, 2, 9, 5, 3, 11]
remove_duplicates(list)
print(list)
