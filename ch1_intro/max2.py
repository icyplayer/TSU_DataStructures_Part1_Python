""" select maximun 2 number from an array """
from copy import deepcopy
from random import randrange


def max2bs(A):
    """ bubble sort: access order """
    if len(A) < 2:
        return
    B = deepcopy(A)
    for i in range(2):
        for j in range(1, len(B)-i):
            if B[j] < B[j-1]:
                B[j-1], B[j] = B[j], B[j-1]
    return B[-1], B[-2]


def max2bf(A, lo, hi):
    """ Bruce force method according to 01E-8 1st example """
    x1, x2 = lo, lo
    for i in range(lo, hi):
        if A[x1] < A[i]:
            x1 = i
    for i in range(lo, x1):
        if A[x2] < A[i]:
            x2 = i
    for i in range(x1+1, hi):
        if A[x2] < A[i]:
            x2 = i
    return A[x1], A[x2]


def max2Ver3(A, lo, hi):
    """ Improved iterating approach according to 01E-8 2nd example """
    if len(A) < 2:
        return
    x1, x2 = lo, lo+1
    if A[x1] < A[x2]:
        x1, x2 = x2, x1  # swap
    for i in range(lo+2, hi):
        if A[i] > A[x2]:
            x2 = i
            if A[x1] < A[x2]:
                x1, x2 = x2, x1  # swap
    return A[x1], A[x2]


def max2GetIdxVer1(A, lo, hi):
    """
    Helper function for divide and conqure approach,
    inspired by 01E-09 1st example
    T(n) = 2*T(n/2) + 3
    """
    if hi-lo == 1:
        x1, x2 = lo, None  # not good
        return x1, x2
    elif hi-lo == 2:
        x1, x2 = lo, lo+1
        if A[x2] > A[x1]:
            x1, x2 = x2, x1
        return x1, x2
    mi = (lo+hi) >> 1
    lx1, lx2 = max2GetIdxVer1(A, lo, mi)
    rx1, rx2 = max2GetIdxVer1(A, mi, hi)
    if A[lx1] > A[rx1]:
        x1 = lx1
        if lx2:
            if A[lx2] > A[rx1]:
                x2 = lx2
            else:
                x2 = rx1
        else:  # lx2 is None
            x2 = rx1
    else:  # rx1 > lx1
        x1 = rx1
        if rx2:
            if A[rx2] > A[lx1]:
                x2 = rx2
            else:
                x2 = lx1
        else:  # rx2 is None
            x2 = lx1
    return x1, x2


def max2GetIdx(A, lo, hi):
    """
    Helper function for divide and conqure approach in 01E-09 1st example
    Improved impl based on max2GetIdxVer1
    T(n) = 2*T(n/2) + 2
    """
    if hi-lo == 1:
        raise IndexError("Array size too small: (lo=%d, hi=%d)" % (lo, hi))
    elif hi-lo == 2:
        x1, x2 = lo, lo+1
        if A[x2] > A[x1]:
            x1, x2 = x2, x1
        return x1, x2
    elif hi-lo == 3:
        x1, x2 = lo, lo+1
        if A[lo+2] > A[x1]:
            x2 = x1
            x1 = lo+2
        elif A[lo+2] > A[x2]:  # A[x2] < A[lo+2] <= A[x1]
            x2 = lo+2
        return x1, x2

    mi = (lo+hi) >> 1
    lx1, lx2 = max2GetIdx(A, lo, mi)
    rx1, rx2 = max2GetIdx(A, mi, hi)
    if A[lx1] > A[rx1]:
        x1 = lx1
        if A[lx2] > A[rx1]:
            x2 = lx2
        else:
            x2 = rx1
    else:  # rx1 > lx1
        x1 = rx1
        if A[rx2] > A[lx1]:
            x2 = rx2
        else:
            x2 = lx1
    return x1, x2


def max2Ver4(A, lo, hi):
    if hi-lo < 2:
        return
    x1, x2 = max2GetIdxVer1(A, lo, hi)
    return A[x1], A[x2]


def max2Ver5(A, lo, hi):
    """ divide and conqure approach in 01E-09 1st example """
    if hi-lo < 2:
        return
    x1, x2 = max2GetIdx(A, lo, hi)
    return A[x1], A[x2]


#===============================================================================
# test functions
#===============================================================================
def testMax2(max2Func):
    A = [1, 4, 2, 9, 7, 5]
    print(max2Func(A, 0, len(A)))


def testMax2MultVer(max2Func, arrays):
    for A in arrays:
        print(max2Func(A, 0, len(A)))


#===============================================================================
# run tests
#===============================================================================
A = [1, 4, 2, 9, 7, 5]
B = [1, 2]
C = [randrange(20) for i in range(20)]

print("A = %r" % A)
print("B = %r" % B)
print("C = %r" % C)

# print(max2bs(A))

# testMax2(max2bf)
# testMax2(max2Ver3)
testMax2MultVer(max2Ver5, [A, B, C])
