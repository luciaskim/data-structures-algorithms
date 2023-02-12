def merge_two_sorted_lists(list1, list2):
    sorted_list = []
    len_1 = len(list1)
    len_2 = len(list2)

    i = j = 0
    while i < len_1 and j < len_2:
        if list1[i] <= list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1


    while i < len_1:
        sorted_list.append(list1[i])
        i += 1

    while j < len_2:
        sorted_list.append(list2[j])
        j += 1
    
    
    return sorted_list

if __name__ == '__main__':
    a = [5, 8, 12, 56, 89, 100]
    b = [7, 9, 45, 51]
    print(merge_two_sorted_lists(a, b))