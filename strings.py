

def is_palindrome(s):
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

