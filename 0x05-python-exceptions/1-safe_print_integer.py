def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # print the integer using format string
        return True  # return True if the value was correctly printed
    except ValueError:
        # if the value cannot be formatted as an integer, catch the exception
        return False  # return False
