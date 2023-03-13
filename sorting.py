

def insertion_sort(array):
    """
    Write a function that takes in an array of integers and returns a sorted version of
    that array. Use the Insertion Sort algorithm to sort the array.

    Sample Input:
    array = [8, 5, 2, 9, 5, 6, 3]

    Sample Output:
    [2, 3, 5, 5, 6, 8, 9]

    Optimal Space & Time Complexity
    Best: O(n) time | O(1) space - where n is the length of the input array
    Average: O(n^2) time | O(1) space - where n is the length of the input array
    Worst: O(n^2) time | O(1) space - where n is the length of the input array

    :param array:
    :return:
    """
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
    """
    Write a function that takes in an array of integers and returns a sorted version of
    that array. Use the Quick Sort algorithm to sort the array.

    Sample Input:
    array = [8, 5, 2, 9, 5, 6, 3]

    Sample Output:
    [2, 3, 5, 5, 6, 8, 9]

    Optimal Space & Time Complexity
    Best: O(nlog(n)) time | O(log(n)) space - where n is the length of the input array
    Average: O(nlog(n)) time | O(log(n)) space - where n is the length of the input array
    Worst: O(n^2) time | O(log(n)) space - where n is the length of the input array

    :param array:
    :param start_idx:
    :param end_idx:
    :return:
    """
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
