def safe_print_division(a, b):
    try:
        quotient = (a / b)
        return(quotient)
    except:
        quotient = None
        return (None)
    finally:
        print("Inside result: {}".format(quotient))
