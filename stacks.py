

def balanced_brackets(string):
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
