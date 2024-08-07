#!/usr/bin/python3
""" A function that calculate the minimum
operation of a given task
"""


def minOperations(n):
    """
        Calculates the minimum number of operations required
        to perform the given task.

        Parameters: n (int): An integer specifying the task
        to perform.

        Returns: int: The minimum number of operations required
            to perform the task.
    """
    # checking if n is a number
    if not isinstance(n, int):
        return 0

    ops_count = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            # paste
            done += clipboard
            ops_count += 1
    return ops_count
