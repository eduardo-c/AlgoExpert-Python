

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
