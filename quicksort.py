some_list = [2, 5, 0, 3, 1, 12, -1, 4, 4, 4, -23]
empty_list = []


def sort(list_to_be_sorted):
    return quicksort(list_to_be_sorted, [], 0, len(list_to_be_sorted)-1)


def quicksort(list_to_be_sorted, helper_list, start_index, end_index):
    if len(list_to_be_sorted) <= 1 or end_index <= start_index:
        return list_to_be_sorted
    else:
        pivot = list_to_be_sorted[start_index]
        for i in range(start_index, end_index+1):
            # print(i)
            if list_to_be_sorted[i] < pivot:
                helper_list.append(i)
        lower_sublist_length = len(helper_list)
        for i in helper_list:
            tmp = list_to_be_sorted[i]
            del list_to_be_sorted[i]
            list_to_be_sorted.insert(start_index, tmp)

        helper_list.clear()

        sorted_lower_half = quicksort(list_to_be_sorted, helper_list, start_index, start_index + lower_sublist_length-1)
        sorted_upper_half = quicksort(list_to_be_sorted, helper_list, start_index + lower_sublist_length+1, end_index)

        for i in range(len(list_to_be_sorted)):
            if start_index <= i < start_index + lower_sublist_length:
                list_to_be_sorted[i] = sorted_lower_half[i]
            elif start_index + lower_sublist_length < i <= end_index:
                list_to_be_sorted[i] = sorted_upper_half[i]

        return list_to_be_sorted


# print(sort(some_list))
