"""
Bubble sort:
Access/Descent order
"""

class BubbleSort(object):
    def __init__(self, array):
        self.array = array
    
    # sorting in access/descent order.         
    # TODO: opt = operator.__lt__ and operator.__gt__ encontered bug - WHY?
    def sort(self, accessFlag=True):
        if accessFlag:
            opt = lambda x, y : x < y
        else:
            opt = lambda x, y : x > y
        # bubble sort 
        for i in range(len(self.array)):
            for j in range(1, len(self.array)-i):
                if opt(self.array[j], self.array[j-1]):  # if access order, swap if array[j] < array[i], v.v
                    self.array[j-1], self.array[j] = self.array[j], self.array[j-1]  # swap 
            print(self.array)
                    
    def sortAccess(self):
        self.sort(accessFlag=True)
            
    def sortDescent(self):
        self.sort(accessFlag=False)

    def getArray(self):
        return self.array

# Simple test
def simpleTest(array):
    bs = BubbleSort(array)  
    print("sort (access order)")
    bs.sortAccess()
    print(bs.getArray())
    print("sort (descent order)")
    bs.sortDescent()
    print(bs.getArray())


simpleTest([1, 2, 3, 5, 4])
simpleTest([11, 23, 19, 7, 17, 5, 3, 13, 2, 29])

