def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    for number in range(start, stop+1):
        print(number)

    count = start
    while count <= stop:
        print(count)
        count += 1

    count = start
    if start > stop:
        while count >= stop:
            print(count)
            count -= 1
    elif start < stop:
        while count <= stop:
            print(count)
            count += 1

    if start > stop:
        for count in range(start, stop-1, -1):
            print(count)
    else:
        for count in range(start, stop+1, +1):
            print(count)
    return


count_up(5, 3)
count_up(10, 12)
