# from array import array
from random import randrange
class Hailstone(object):
    def __init__(self):
        pass
#         self.num = num
    def hailstonePath(self, n):
        if n <= 1:
            return [1]
        elif n%2 == 0:
            return [n] + self.hailstonePath(n//2)       
        else:
            return [n] + self.hailstonePath(n*3 + 1)
    
    def hailstone(self, n):
        while True:
            if n <= 1:
                return 1
            elif n % 2 == 0:
                n = n//2                
            else:
                n = n*3 + 1

nLst = [1, 2, 42]
h = Hailstone()
for n in nLst:
    print("hailstonePath(%d)" % n)
    print(h.hailstonePath(n))

# simple test - 10 times
for i in range(10):
    n = randrange(1, 100)
    try:
        print("hailstonePath(%d)" % n)
        print(h.hailstonePath(n))
    except Exception as e:
        print(str(e))
        continue

print("test")
print(h.hailstone(42))
# n = 2
# hailstone(2)
# n = 42
# hailstone(42)