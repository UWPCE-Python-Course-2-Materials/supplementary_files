"""
recursion
"""


def my_fun(n):
    if n <= 1:
        return n
    return n + my_fun(n / 2)


if __name__ == '__main__':
    n = 100
    print(my_fun(n))


"""
        ---^|v
    ---^|v
---^|v

"""
