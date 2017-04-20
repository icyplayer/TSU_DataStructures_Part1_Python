"""
fibonacci:
iteration; dynamic
"""


def fib0(n):
    """ Iteration """
    fibPrev1, fibPrev2 = 1, 0
    result = 0
    if n == 1:
        result = fibPrev1
    elif n == 0:
        result = fibPrev2
    while n > 1:
        result = fibPrev1 + fibPrev2
        fibPrev2 = fibPrev1
        fibPrev1 = result
        n -= 1
    return result


def fib1(n):
    """ Dynamic: 01XC-5 """
    f, g = 0, 1
    if n == 0:
        return f
    while n > 1:  # from fib(1), g is valid
        g = g+f
        f = g-f
        n -= 1
    return g

#     result = 1
#     fibPrev = 0
#     while n > 0:
#         result += fibPrev
#         fibPrev = result
#         print("result=%d, fibPrev=%d" % (result, fibPrev))
#         n -= 1
#     return result


def testFibBasic(fibFunc):
    for i in range(10):
        print("fib(%d) = %d" % (i, fibFunc(i)))


testFibBasic(fib0)
testFibBasic(fib1)