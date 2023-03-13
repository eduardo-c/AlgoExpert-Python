

def is_palindrome(s):
    """
    Write a function that takes in a non-empty string and that returns a boolean representing
    whether the string is a palindrome.

    A palindrome is defined as a string that's written the same forward and backward.
    Note that single-character strings are palindromes.

    Sample Input:
    string = "abcdcba"

    Sample Output:
    true

    Optimal Space & Time Complexity:
    O(n) time | O(1) space - where n is the length of the input string

    :param s:
    :return:
    """
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def is_palindrome_test():
    s = "hello"
    print(is_palindrome(s))
    s = "abcdcba"
    print(is_palindrome(s))


def first_non_repeating_char(s):
    """
    Write a function that takes in a string of lowercase English-alphabet letters and
    returns the index of the string's first non-repeating character.

    The first non-repeating character is the first character in a string that occurs only once.

    If the input string doesn't have any non-repeating characters, your function should
    return -1.

    Sample Input:
    string = "abcdcaf"

    Sample Output:
    1

    Optimal Space & Time Complexity
    O(n) time | O(1) space - where n is the length of the input string The constant space
    is because the input string only has lowercase English-alphabet letters; thus, our
    hash table will never have more than 26 character frequencies.

    :param s: string
    :return: index position of the first character that doesn't repeat in string
    """
    char_dict = {}
    for i in s:
        if i in char_dict:
            # False if this char is repeated, True otherwise
            char_dict[i] = False
        else:
            char_dict[i] = True
    for i in range(0, len(s)):
        if s[i] in char_dict and char_dict[s[i]]:
            return i
    return -1


def first_non_repeating_char_test():
    s = "abcdcaf"
    print(s)
    print(first_non_repeating_char(s))


def run_length_encoding(s):
    """
    Write a function that takes in a non-empty string and returns its run-length encoding.

    From Wikipedia, "run-length encoding is a form of lossless data compression in which
    runs of data are stored as a single data value and count, rather than as the original
    run." For this problem, a run of data is any sequence of consecutive, identical
    characters. So the run "AAA" would be run-length-encoded as "3A".

    To make things more complicated, however, the input string can contain all sorts of
    special characters, including numbers. And since encoded data must be decodable, this
    means that we can't naively run-length-encode long runs. For example, the run
    "AAAAAAAAAAAA" (12 A's), can't naively be encoded as "12A", since this string can be
    decoded as either "AAAAAAAAAAAA" or "1AA". Thus, long runs (runs of 10 or more characters)
    should be encoded in a split fashion; the aforementioned run should be encoded as "9A3A".

    Sample Input
    string = "AAAAAAAAAAAAABBCCCCDD"

    Sample Output:
    "9A4A2B4C2D"

    Optimal Space & Time Complexity
    O(n) time | O(n) space - where n is the length of the input string

    :param s:
    :return:
    """
    last_char = s[0]
    count = 1
    result = ""
    for i in range(1, len(s)):
        if s[i] != last_char:
            mod = count % 9
            div = int(count / 9)
            for j in range(0, div):
                result += "{}{}".format(9, last_char)
            if mod > 0:
                result += "{}{}".format(mod, last_char)
            count = 1
        else:
            count += 1
        last_char = s[i]
    if count == 1:
        result += "1{}".format(last_char)
    else:
        mod = count % 9
        div = int(count / 9)
        for j in range(0, div):
            result += "{}{}".format(9, last_char)
        if mod > 0:
            result += "{}{}".format(mod, last_char)
    return result


def run_length_encoding_test():
    message = "AAAAAAAAAAAAABBCCCCDD"
    print(message)
    encoded = run_length_encoding(message)
    print(encoded)
    message = "aA"
    print(message)
    encoded = run_length_encoding(message)
    print(encoded)
    message = "........______=========AAAA   AAABBBB   BBB"
    print(message)
    encoded = run_length_encoding(message)
    print(encoded)
