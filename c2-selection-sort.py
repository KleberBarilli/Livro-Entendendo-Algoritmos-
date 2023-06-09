def search_lowest(arr):
    lowest = arr[0]
    lowest_index = 0

    for i in range(1,len(arr)):
        if(arr[i] < lowest):
            lowest = arr[i]
            lowest_index = i
    return lowest_index


def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        lowest = search_lowest(arr)
        new_arr.append(arr.pop(lowest))
    return new_arr

print(selection_sort([5, 3, 6, 2, 10, 11, 15, 1]))
