from abc import ABC, abstractclassmethod
class LinkedList(ABC):
    @abstractclassmethod
    def insert_at_end(self, element):
        pass

    @abstractclassmethod
    def insert_at_head(self, element):
        pass

    @abstractclassmethod
    def delete(self, element):
        pass

    @abstractclassmethod
    def delete_at_head(self):
        pass

    @abstractclassmethod
    def search(self, element):
        pass

    @abstractclassmethod
    def is_empty(self):
        pass