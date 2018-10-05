class Array:
    def __init__(self, array):
        self.__array = array[::]

    def __repr__(self):
        return self.__array.__repr__()

    def __str__(self):
        return self.__array.__str__()

    def map(self, function):
        for k in range(len(self.__array)):
            el = self.__array[k]
            new_el = function(el)
            self.__array[k] = new_el
        return self

    def filter(self, function):
        new_array = []
        for k in range(len(self.__array)):
            el = self.__array[k]
            if (function(el)):
                new_array.append(el)
        self.__array = new_array
        return self

    def reduce(self, function):
        return 0
