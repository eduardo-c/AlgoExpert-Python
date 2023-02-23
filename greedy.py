

def minimum_waiting_time(queries):
    queries = sorted(queries)
    waiting_count = len(queries) - 1
    total = 0
    for i in queries:
        total += i * waiting_count
        waiting_count -= 1
    return total


def minimum_waiting_time_test():
    queries = [3, 2, 1, 2, 6]
    print(queries)
    print(minimum_waiting_time(queries))
