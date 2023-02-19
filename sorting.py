

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