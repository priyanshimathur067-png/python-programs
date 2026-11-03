class MyList:
    def __init__(self, arr):
        self.arr = arr

    def __contains__(self, val):
        return val in self.arr

obj = MyList([10, 20, 30, 40])

print(20 in obj)
print(50 in obj)