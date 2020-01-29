class Stack(object):
    def __init__(self, data_type=str):
        self._data = list()
        self.data_type = data_type

    def __str__(self) -> str:
        '''Returns the string representation of the Stack starting from bottom to top of stack
        >>> s = Stack(int)
        >>> str(s)
        '[>'
        >>> s.push(1)
        >>> s.push(2)
        >>> str(s)
        '[1, 2>'
        '''
        string = '['
        try:
            if self._check_has_data():
                string += f'{self._data[0]}'
        except IndexError as err:
            return '[>'
        finally:
            for value in self._data[1:]:
                string += f', {value}'
            string += '>'
            return string
    
    def __len__(self) -> int:
        '''Returns the amount of items in the Stack
        >>> s = Stack(int)
        >>> len(s)
        0
        >>> s.push(1)
        >>> len(s)
        1
        '''
        return len(self._data)
    
    def _check_type(self, value) -> bool:
        '''Verifies that the sent value type is correct
        >>> s = Stack(int)
        >>> s._check_type(5)
        True
        >>> s._check_type('NotAnInt')
        Traceback (most recent call last):
        ...
        TypeError: Cannot use <class 'str'> in Stack of type: <class 'int'>
        '''
        if type(value) is not self.data_type:
            raise TypeError(f'Cannot use {type(value)} in Stack of type: {self.data_type}')
        return True
    
    def _check_has_data(self) -> bool:
        '''Verifies that the Stack has data available
        >>> s = Stack(int)
        >>> s._check_has_data()
        Traceback (most recent call last):
        ...
        IndexError: Empty Stack has no more data.
        >>> s.push(1)
        >>> s._check_has_data()
        True
        '''
        if self.isEmpty():
            raise IndexError('Empty Stack has no more data.')
        return True

    def isEmpty(self) -> bool:
        '''Returns boolean that says if there is no more data in the stack
        >>> s = Stack(int)
        >>> s.isEmpty()
        True
        >>> s.push(1)
        >>> s.isEmpty()
        False
        '''
        return len(self._data) <= 0

    def push(self, value) -> None:
        '''Adds an element to the stack
        >>> s = Stack(int)
        >>> s.push(1)
        >>> print(s)
        [1>
        '''
        if self._check_type(value):
            self._data.append(value)
    
    def pop(self):
        '''Removes and returns the last element in the Stack
        >>> s = Stack(int)
        >>> s.push(1)
        >>> s.pop()
        1
        '''
        if self._check_has_data():
            return self._data.pop()

    def top(self):
        '''Returns the top element value in the Stack
        >>> s = Stack(int)
        >>> s.push(1)
        >>> s.top()
        1
        '''
        if self._check_has_data():
            return self._data[-1]

def _test():
    import doctest
    doctest.testmod(extraglobs={'s': Stack(int)})

if __name__ == "__main__":
    _test()
