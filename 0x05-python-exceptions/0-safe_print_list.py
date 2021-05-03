def safe_print_list(my_list=[], x=0):
    size = 0
    try:
        for i in range(x):
            if size != x:
                print("{}".format(my_list[i]), end="")
                size = size + 1
        print()
        return(size)
    except:
        print()
        return(size)
