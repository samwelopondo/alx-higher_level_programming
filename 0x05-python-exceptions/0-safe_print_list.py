def safe_print_list(my_list=[], x=0):
    count = 0  # variable to track the number of elements printed
    try:
        # Print the first x elements of the list
        for i in range(x):
            print(my_list[i], end=' ')  # print element followed by a space
            count += 1  # increment count
    except IndexError:
        # If there are not enough elements in the list, catch the exception
        pass
    print()  # print a new line after all elements have been printed
    return count  # return the number of elements printed
