"""
Longest Common Subsequence(LCS)

Dynamic
"""


def lcs(A, n, B, m):
    """
    01XC-7: LCS
    O(2^n)
    """
    if n == -1 or m == -1:
        return 0
    elif A[n] == B[m]:
        return lcs(A, n-1, B, m-1)+1  # decrease and conqure
    else:
        l1, l2 = lcs(A, n-1, B, m), lcs(A, n, B, m-1)
        if l1 < l2:
            return l2
        return l1


def testLcs():
    A = "advice"
    B = "advantage"
    print("A = %r\tB = %r" % (A, B))
    print("LCS = %r" % lcs(A, len(A)-1, B, len(B)-1))


testLcs()
