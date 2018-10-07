import math

class Array:
    def __init__(self, array):
        self.__array = array[::]

    def __repr__(self):
        return self.__array.__repr__()

    def __str__(self):
        return self.__array.__str__()

    @classmethod
    def range(cls, int):
        arr = []
        for k in range(int):
            arr.append(k)
        return cls(arr)

    @classmethod
    def empty(cls, int):
        arr = []
        for k in range(int):
            arr.append(None)
        return cls(arr)

    def each(self, function):
        new_array = []
        for k in range(len(self.__array)):
            el = self.__array[k]
            new_array.append(el)
            function(el)
        return Array(new_array)

    def map(self, function):
        new_array = []
        for k in range(len(self.__array)):
            el = self.__array[k]
            new_el = function(el)
            new_array.append(new_el)
        return Array(new_array)

    def filter(self, function):
        new_array = []
        for k in range(len(self.__array)):
            el = self.__array[k]
            if (function(el)):
                new_array.append(el)
        return Array(new_array)

    def reject(self, function):
        new_array = []
        for k in range(len(self.__array)):
            el = self.__array[k]
            if (not function(el)):
                new_array.append(el)
        return Array(new_array)

    def reduce(self, function, initialValue):
        acc = initialValue
        for k in range(len(self.__array)):
            el = self.__array[k]
            acc = function(acc, el)
        return acc

    def find(self, function):
        for k in range(len(self.__array)):
            el = self.__array[k]
            if (function(el)):
                return el
        return None

    def find_index(self, function):
        for k in range(len(self.__array)):
            el = self.array[k]
            if (function(el)):
                return k
        return -1

    def every(self, function):
        for k in range(len(self.__array)):
            el = self.array[k]
            if (not function(el)):
                return False
        return True

    def some(self, function):
        for k in range(len(self.__array)):
            el = self.__array[k]
            if (function(el)):
                return True
        return False

    def contains(self, value):
        for k in range(len(self.__array)):
            el = self.__array[k]
            if (el == value):
                return True
        return False

    def max(self, function):
        max = -math.inf
        for k in range(len(self.__array)):
            el = self.__array[k]
            score = function(el)
            if (score > max):
                max = score
        return max

    def min(self, function):
        min = math.inf
        for k in range(len(self.__array)):
            el = self.__array[k]
            score = function(el)
            if (score < min):
                min = score
        return min
