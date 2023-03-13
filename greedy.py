

def minimum_waiting_time(queries):
    """
    You're given a non-empty array of positive integers representing the amounts of time
    that specific queries take to execute. Only one query can be executed at a time,
    but the queries can be executed in any order.

    A query's waiting time is defined as the amount of time that it must wait before its
    execution starts. In other words, if a query is executed second, then its waiting time
    is the duration of the first query; if a query is executed third, then its waiting time
    is the sum of the durations of the first two queries.

    Write a function that returns the minimum amount of total waiting time for all of the
    queries. For example, if you're given the queries of durations [1, 4, 5], then the total
    waiting time if the queries were executed in the order of [5, 1, 4] would be
    (0) + (5) + (5 + 1) = 11. The first query of duration 5  would be executed immediately,
    so its waiting time would be 0, the second query of duration 1 would have to wait 5 seconds
    (the duration of the first query) to be executed, and the last query would have to wait the
    duration of the first two queries before being executed.

    Note: you're allowed to mutate the input array.

    Simple Input:
    queries = [3, 2, 1, 2, 6]

    Sample Output:
    17

    Optimal Space & Time Complexity
    O(nlogn) time | O(1) space - where n is the number of queries

    :param queries: array of integers representing spending time of every query in a queue
    :return: The minimum waiting time for given array
    """
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
