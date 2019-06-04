def bubble_sort(array):
    index = len(array) - 1
    while index >= 0:
        for j in range(index):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        index -= 1
    return array
