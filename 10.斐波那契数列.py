# coding=utf-8
"""
求斐波那契数列数列的第n项
"""


def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iteration(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    number1 = 0
    number2 = 1
    numbern = 0
    for i in range(2, n + 1):
        numbern = number1 + number2
        number1 = number2
        number2 = numbern

    return numbern


def fibonacci_formula(n):
    root_five = 5 ** 0.5
    result = (((1 + root_five) / 2) ** n - (
            (1 - root_five) / 2) ** n) / root_five
    return int(result)


def fibonacci_matrix(n):
    def mul(a, b):
        return ((a[0][0] * b[0][0] + a[0][1] * b[1][0],
                 a[0][0] * b[0][1] + a[0][1] * b[1][1]),
                (a[1][0] * b[0][0] + a[1][1] * b[1][0],
                 a[1][0] * b[0][1] + a[1][1] * b[1][1]))

    def power(x, n):
        if n == 1:
            return x
        ans = power(mul(x, x), n / 2)
        if n % 2 == 1:
            ans = mul(x, ans)
        return ans

    if n == 0:
        return 0
    if n == 1:
        return 1
    q = ((1, 1), (1, 0))
    return power(q, n - 1)[0][0]


def fibonacci_matrix_iteration(n):
    def mul(a, b):
        return ((a[0][0] * b[0][0] + a[0][1] * b[1][0],
                 a[0][0] * b[0][1] + a[0][1] * b[1][1]),
                (a[1][0] * b[0][0] + a[1][1] * b[1][0],
                 a[1][0] * b[0][1] + a[1][1] * b[1][1]))

    def power(x, n):
        if n == 1:
            return x
        y = ((1, 0), (0, 1))
        while n > 1:
            if n % 2:
                y = mul(x, y)
            x = mul(x, x)
            n /= 2
        return mul(x, y)

    if n == 0:
        return 0
    if n == 1:
        return 1
    q = ((1, 1), (1, 0))
    return power(q, n - 1)[0][0]


"""
题目二:青蛙跳台阶问题
一只青蛙可以跳上一级台阶,也可以跳上2级台阶.
求该青蛙跳上一个n级的台阶总共有多少种跳法.
"""


def get_jump_count(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return get_jump_count(n - 2) + get_jump_count(n - 1)


"""
题目三:
可以用2X1的小矩形横着或者竖着去覆盖的矩形,请问用8个2X1的小矩形无重叠地覆盖一个2X8的大矩形
总共有多少种方法.f(8) = f(7) + f(6)
"""
