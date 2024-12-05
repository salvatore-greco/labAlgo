from abc import ABC, abstractmethod


class DataStructureElement:

    def __init__(self, key, value):
        self._key = key
        self._value = value

    def getKey(self):
        return self._key

    def getValue(self):
        return self._value

    def setKey(self, newKey):
        self._key = newKey

    def setValue(self, newValue):
        self._value = newValue


class DataStructure(ABC):
    @abstractmethod
    def insert(self, element: DataStructureElement):
        """Insert element in the data structure"""

    @abstractmethod
    def search(self, target) -> DataStructureElement:
        """Search target in the data structure"""

    @abstractmethod
    def delete(self, target):
        """delete the element from the data structure"""

    @abstractmethod
    def __iter__(self):
        """Returns the iterator of the data structure"""

    @abstractmethod
    def __next__(self):
        """Return the next element of the data structure from the iterator"""
