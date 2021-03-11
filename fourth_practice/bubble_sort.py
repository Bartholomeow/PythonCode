def bubble_sort(list):
    for i in range(len(list) + 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


list = [6, 5, 3, 1, 8, 7, 2, 4]
print(list)
bubble_sort(list)
print(list)

# print('Введите набор чисел для сортировки через пробел')
# list1 = list(map(int, list(input().split(' '))))
# bubble_sort(list1)
# print(list1)
