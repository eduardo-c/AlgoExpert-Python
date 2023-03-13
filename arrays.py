

def is_subsequence(a, sub):
    """
    Given two non-empty arrays of integers, write a function that determines
    whether the second array is a subsequence of the first one.

    A subsequence of an array is a set of numbers that aren't necessarily adjacent
    in the array but that are in the same order as they appear in the array. For
    instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4],
    and so do the numbers [2, 4]

    Note that a single number in an array and the array itself are both valid
    subsequences of the array.

    Sample Input: a = [5, 1, 22, 25, 6, -1, 8, 10] sub = [1, 6, -1, 10]
    Sample Output: True

    Optimal Space & Time Complexity:
    O(n) time | O(1) space - where n is the length of the array

    :param a: array
    :param sub: array under test to know if it's sub array of a
    :return: True if sub is sub array of a, False Otherwise
    """
    cont = 0
    is_subs = False
    for i in a:
        if sub[cont] == i:
            cont += 1
            if cont == len(sub):
                is_subs = True
                break
    return is_subs


def subsequence_test():
    # Sample Input 1
    a = [1, 2, 3, 4]
    sub = [1, 4]
    print(is_subsequence(a, sub))
    # Sample Input 2
    a = [5, 1, 22, 25, 6, -1, 8, 10]
    sub = [1, 6, -1, 10]
    print(is_subsequence(a, sub))
    # Sample Input 2
    a = [5, 1, 22, 25, 6, -1, 8, 10]
    sub = [1, -1, 6, 10]
    print(is_subsequence(a, sub))


def two_number_sum(a, n):
    """
    Write a function that takes in a non-empty array of distinct integers and an
    integer representing a target sum. If any two numbers in the input array sum
    up to the target sum, the function should return them in an array, in any
    order. If no two numbers sum up to the target sum, the function should return
    an empty array.

    Note that the target sum has to be obtained by summing two different integers
    in the array; you can't add a single integer to itself in order to obtain the
    target sum.

    You can assume that there will be at most one pair of numbers summing up to
    the target sum.

    Sample Input: a = [3, 5, -4, 8, 11, 1, -1, 6] n = 10
    Sample Output: [-1, 11]

    Optimal Space & Time Complexity:
    O(n) time | O(n) space - where n is the length of the input array

    :param a: array
    :param n: target sum
    :return: array with the couple of numbers which make the target sum
    """
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == n:
                return [a[i], a[j]]
    return []


def two_number_sum_test():
    # Sample Input 1
    a = [3, 5, -4, 8, 11, 1, -1, 6]
    n = 10
    print(two_number_sum(a, n))