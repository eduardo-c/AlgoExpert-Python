

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
    largest = array[0:3]
    for i in array[3:len(array)]:
        if i > min(largest):
            largest[largest.index(min(largest))] = i
    print(sorted(largest))


def find_three_largest_numbers_test():
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    find_three_largest_numbers(array)
