# coding=utf-8
"""
题目:
实现函数Power(base, exponent),求base的exponent次方
"""


def power_with_unsigned_exponent(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    result = power_with_unsigned_exponent(base, exponent / 2)
    result *= result
    if exponent % 2 == 1:
        result *= base
    return result


def power(base, exponent):
    if base == 0 and exponent <= 0:
        raise ValueError()
    result = power_with_unsigned_exponent(base, abs(exponent))
    if exponent < 0:
        result = 1.0 / result
    return result

if __name__ == '__main__':
    print pow(2,-1)