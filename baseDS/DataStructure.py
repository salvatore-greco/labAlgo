from abc import ABC, abstractmethod


class DataStructure(ABC):
    @abstractmethod
    def insert(self, element):
        """Insert element in the data structure"""

    @abstractmethod
    def search(self, target):
        """Search target in the data structure"""

    @abstractmethod
    def delete(self, target):
        """delete the element from the data structure"""