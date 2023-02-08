

def is_subsequence(a, sub):
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
