#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numbers = 0
    try:
        for i in range(x):
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
                    numbers += 1
            except ValueError:
                continue
    except IndexError:
        pass
    print("\nnb_print:", numbers)
    return numbers
