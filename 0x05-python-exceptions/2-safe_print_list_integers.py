#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    size = 0
    try:
        for i in range(x):
            if size <= x:
                if (isinstance(my_list[i], int)) is False:
                    continue
                else:
                    print("{:d}".format(my_list[i]), end="")
                    size = size + 1
        print()
        return(size)
    except:
        return(None)
