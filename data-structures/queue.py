class Queue(object):
    def __init__(self, data_type=str):
        self._data = list()
        self.data_type = data_type

    def __str__(self) -> str:
        return str(self._data)
    
    def __len__(self) -> int:
        return len(self._data)

    def _check_type(self, value) -> bool:
        if type(value) is not self.data_type:
            raise TypeError(f'Cannot use {type(value)} in Queue of type: {self.data_type}')
        return True

    def _check_has_data(self) -> bool:
        if self.is_Empty():
            raise IndexError('Empty Queue has no more data.')
        return True
    
    def enqueue(self, value) -> None:
        if self._check_type(value):
            self._data.insert(0, value)

    def dequeue(self):
        if self._check_has_data():
            return self._data.pop()

    def is_Empty(self) -> bool:
        return len(self._data) <= 0

    def top(self):
        if self._check_has_data():
            return self._data[-1]
