class Array(object):
    def __init__(self, size=0, data_type=str):
        self._size = size
        self._data = [None] * size
        self.data_type = data_type

    def __str__(self) -> str:
        '''Returns the string representation of the array
        >>> str(a)
        '[None, None]'
        '''
        return str(self._data)

    def __len__(self) -> int:
        '''Returns the size of the array
        >>> len(a)
        2
        '''
        return self._size

    def __iter__(self):
        '''Yields generated values to iterate over
        >>> for value in a:
        ...     print(value)
        None
        None
        '''
        for value in self._data:
            yield value
    
    def _check_index(self, index) -> bool:
        '''Checks if the index is within the appropriate range for the array
        >>> a._check_index(1)
        True
        >>> a._check_index(5)
        Traceback (most recent call last):
        ...
        IndexError: Array of size 2 has no index at 5
        '''
        if abs(index) > len(self)-1:
            raise IndexError(f'Array of size {len(self)} has no index at {index}')
        return True
    
    def _check_type(self, value) -> bool:
        '''Checks if the type being added to the array is the correct type
        >>> a._check_type(1)
        True
        >>> a._check_type('NotAnInt')
        Traceback (most recent call last):
        ...
        TypeError: Cannot use <class 'str'> in array of type: <class 'int'>
        '''
        if type(value) is not self.data_type:
            raise TypeError(f'Cannot use {type(value)} in array of type: {self.data_type}')
        return True

    def get(self, index):
        '''Returns the value of an item at a specific index
        >>> a.insert(1, 5)
        >>> a.get(1)
        5
        '''
        if self._check_index(index):
            return self._data[index]

    def insert(self, index, value) -> None:
        '''Changes the value at a specified index
        >>> a.insert(1, 5)
        >>> print(a)
        [None, 5]
        '''
        if self._check_index(index) and self._check_type(value):
            self._data[index] = value

    def delete(self, index) -> None:
        '''Changes a value to None at a specified index
        >>> a.insert(1, 5)
        >>> a.delete(1)
        >>> print(a)
        [None, None]
        '''
        if self._check_index(index):
            self._data[index] = None

def _test():
    import doctest
    doctest.testmod(extraglobs={'a': Array(2, int)})

if __name__ == "__main__":
    _test()
    