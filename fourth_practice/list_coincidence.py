def sets_are_equal(list1, list2):
    """Return True if sets of lists are equal or false if not equal"""
    set1 = set(list1)
    set2 = set(list2)
    return set1 == set2


list1 = [1, 2, 2, 3, 5, 7, 7, 8, 9]
list2 = [1, 1, 9, 8, 7, 5, 3, 2]


print(sets_are_equal(list1, list2))


list3 = [1, 2, 2, 3, 5, 7, 7, 8, 9]
list4 = [1, 1, 9, 8, 7, 5, 3, 2, 4]


print(sets_are_equal(list3, list4))
