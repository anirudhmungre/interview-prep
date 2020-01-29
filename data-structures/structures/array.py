class Array(object):
    def __init__(self, size=0, data_type=str):
        self._size = size
        self._data = [None] * size
        self.data_type = data_type

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return self._size

    def __iter__(self):
        for value in self._data:
            yield value
    
    def __check_index(self, index):
        if abs(index) > len(self)-1:
            raise IndexError(f'Array of size {len(self)} has no index at {index}')
        return True
    
    def __check_type(self, value):
        if type(value) is not self.data_type:
            raise TypeError(f'This array is of type: {self.data_type}')
        return True

    def get(self, index):
        if self.__check_index(index):
            return self._data[index]

    def insert(self, index, value):
        if self.__check_index(index) and self.__check_type(value):
            self._data[index] = value

    def delete(self, index):
        if self.__check_index(index):
            self._data[index] = None
