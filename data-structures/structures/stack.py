class Stack(object):
    def __init__(self, data_type=str):
        self._data = list()
        self.data_type = data_type

    def __str__(self):
        return str(self._data)
    
    def __len__(self):
        return len(self._data)
    
    def __check_type(self, value):
        if type(value) is not self.data_type:
            raise TypeError(f'Cannot use {type(value)} in stack of type: {self.data_type}')
        return True
    
    def __check_has_data(self):
        if self.isEmpty():
            raise IndexError('Empty stack has no more data.')
        return True

    def isEmpty(self):
        return len(self._data) <= 0

    def push(self, value):
        if self.__check_type(value):
            self._data.append(value)
    
    def pop(self):
        if self.__check_has_data():
            return self._data.pop()

    def top(self):
        if self.__check_has_data():
            return self._data[-1]
