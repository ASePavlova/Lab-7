# Лабораторная работа 7
# Даны списки, сортированные по возрастанию. Написать функцию, которая объединит списки в один отсортированный список и вернёт его.
def rot(num):
    str_num = str(num)
    length = len(str_num)
    for u in range(0, length):
        if str_num[u] == '6':
            num = num - 6 * (10 ** (length - u - 1)) + 9 * (10 ** (length - u - 1))
            return num
    return num
