

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


def run_length_encoding(s):
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
