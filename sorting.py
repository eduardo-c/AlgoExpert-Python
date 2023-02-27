

def insertion_sort(array):
    for i in range(1, len(array)):
        inserted = i
        while inserted > 0 and array[inserted] < array[inserted - 1]:
            aux = array[inserted]
            array[inserted] = array[inserted - 1]
            array[inserted - 1] = aux
            inserted -= 1


def insertion_sort_test():
    array = [8, 5, 2, 9, 5, 6, 3]
    print(array)
    insertion_sort(array)
    print(array)


def quick_sort(array, start_idx, end_idx):
    if start_idx >= end_idx:
        return
    pivot = start_idx
    l_pointer = start_idx + 1
    r_pointer = end_idx
    while r_pointer >= l_pointer:
        if array[l_pointer] > array[pivot] and array[pivot] > array[r_pointer]:
            swap(l_pointer, r_pointer, array)
        if array[l_pointer] <= array[pivot]:
            l_pointer += 1
        if array[r_pointer] >= array[pivot]:
            r_pointer -= 1
    swap(pivot, r_pointer, array)
    quick_sort(array, start_idx, r_pointer - 1)
    quick_sort(array, r_pointer + 1, end_idx)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def quick_sort_test():
    a = [8, 5, 2, 9, 5, 6, 3]
    print(a)
    quick_sort(a, 0, len(a) - 1)
    print(a)
