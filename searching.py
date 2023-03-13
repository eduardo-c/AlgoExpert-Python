

def binary_search_aux(array, target, head, tail):
    half = int((head + tail) / 2)
    if array[half] == target:
        return half
    if head >= tail:
        return None
    if array[half] < target:
        return binary_search_aux(array, target, half + 1, tail)
    else:
        return binary_search_aux(array, target, head, half - 1)


def binary_search(array, target):
    """
    Write a function that takes in a sorted array of integers as well as a target integer.
    The function should use the Binary Search algorithm to determine if the target integer
    is contained in the array and should return its index if it is, otherwise -1.

    Sample Input
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33

    Sample Output
    3

    Optimal Space & Time Complexity
    O(log(n)) time | O(1) space - where n is the length of the input array

    :param array: array to be searched
    :param target: target nomber to find in array
    :return: index position of target on array
    """
    head = 0
    tail = len(array) - 1
    half = int((head + tail) / 2)
    if array[half] == target:
        return half
    if array[half] < target:
        return binary_search_aux(array, target, half + 1, tail)
    else:
        return binary_search_aux(array, target, head, half - 1)


def binary_search_test():
    array = [1, 2, 3, 4, 5]
    target = 2
    print(binary_search(array, target))
    array = [0, 1, 21, 33, 45, 45, 61, 71, 73, 73]
    target = 33
    print(binary_search(array, target))


def find_three_largest_numbers(array):
    """
    Write a function that takes in an array of at least three integers and, without sorting
    the input array, returns a sorted array of the three largest integers in the input array.

    The function should return duplicate integers if necessary; for example, it should return
    [10, 10, 12] for an input array of [10, 5, 9, 10, 12]

    Sample Input:
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

    Sample Output:
    [18, 141, 541]

    Optimal Space & Time Complexity
    O(n) time | O(1) space - where n is the length of the input array

    :param array:
    :return: array with the 3 largest numbers in the input array
    """
    largest = array[0:3]
    for i in array[3:len(array)]:
        if i > min(largest):
            largest[largest.index(min(largest))] = i
    print(sorted(largest))


def find_three_largest_numbers_test():
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    find_three_largest_numbers(array)
