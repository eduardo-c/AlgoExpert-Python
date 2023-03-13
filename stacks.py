

def balanced_brackets(string):
    """
    Write a function that takes a string made up of brackets ('(', '[', '{', ')', ']' and '}')
    and other optional characters. The function should return a boolean representing
    whether the string is balanced with regards to brackets.

    A string is said to be balanced if it has as many opening brackets of a certain type
    as it has closing brackets of that type and if no bracket is unmatched. Note that an
    opening bracket can't match a corresponding closing bracket that comes before it, and
    similarly, a closing bracket can't match a corresponding opening bracket that comes after
    it. Also, brackets can't overlap each other as in '[(])'.

    Sample Input:
    string = "([])(){}(())()()"

    Sample Output:
    true

    Optimal Space & Time Complexity
    O(n) time | O(n) space - where n is the length of the input string

    :param string:
    :return:
    """
    stack = []
    open_bracket_set = ("[", "(", "{")
    closing_bracket_set = ("]", ")", "}")
    brackets_map = {"(": ")", "[": "]", "{": "}"}
    for i in string:
        if i in open_bracket_set:
            stack.append(i)
        elif i in closing_bracket_set:
            if len(stack) == 0 or brackets_map[stack[-1]] != i:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def balanced_brackets_test():
    string = "([])(){}(())()()"
    print(balanced_brackets(string))
