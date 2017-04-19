"""
TSU data structures(part 1)
01-E-3
"""


def sumVer1(A, n):
    if n < 1:
        return 0
    else:
        return sumVer1(A, n-1) + A[n-1]


def sumVer2(A, lo, hi):
    if lo == hi:
        return A[lo]
    else:
        mi = (lo+hi) >> 1  # use >>1, for /2 will get a double in Python3
        return sumVer2(A, lo, mi) + sumVer2(A, mi+1, hi)


def testSumVer1():
    assert sumVer1([1, 2, 3, 4, 5], 5) == 15
    assert sumVer1([], 0) == 0
    assert sumVer1([1, 2, 3, 4, 5], 4) == 10


def testSumVer2():
    A = [1, 2, 3, 4]
    B = [1, 2, 3, 4, 5, 6, 7]
    assert sumVer2(A, 0, len(A)-1) == 10
#     try:
#         assert sumVer2([], 0, 0) == 0
#     except Exception as ae:
#         print(str(ae))
    assert sumVer2(B, 0, len(B)-1) == 28


def reverse(A, lo, hi):
    """ recursive version """
    if lo < hi:
        A[lo], A[hi] = A[hi], A[lo]
        reverse(A, lo+1, hi-1)
    else:
        return


def reverseVer2(A, lo, hi):
    """ While loop version """
    while lo < hi:
        A[lo], A[hi] = A[hi], A[lo]
        lo += 1
        hi -= 1


def testReverse(reverseFunc):
    print("test %s" % reverseFunc.__name__)
    A = [1, 2, 3, 4, 5]
    B = [1, 2, 3, 4, 5, 6]
    print("odd length")
    print("original: %r" % A)
    reverseFunc(A, 0, len(A)-1)
    print("reversed: %r" % A)
    print("---------------------------------")
    print("even length")
    print("original: %r" % B)
    reverseFunc(B, 0, len(B)-1)
    print("reversed: %r" % B)


testSumVer2()


# testReverse(reverse)
# testReverse(reverseVer2)
