"""
Michael Patel
November 2019

https://www.kaggle.com/colinmorris/hello-python

"""
#####################################################


#####################################################
def least_difference(a, b, c):
    """
    :param a:
    :param b:
    :param c:
    :return: the smallest difference between any two numbers among a, b, c
    """

    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)

    return min(diff1, diff2, diff3)


# define docstring first, so that help() will display docstring
help(least_difference)
