# Лабораторная работа 7
# Даны списки, сортированные по возрастанию. Написать функцию, которая объединит списки в один отсортированный список и вернёт его.
def merge(*lists):
    new_line = [] # формируем новый список
    temporary_list = []

    for u in range(len(lists[0]) - 1, -1, -1):
        temporary_list = temporary_list + lists[0][u]

    while temporary_list:
        sort_num = min(temporary_list)
        while sort_num in temporary_list:
            new_line.append(sort_num)
            temporary_list.remove(sort_num)
            
    return new_line
