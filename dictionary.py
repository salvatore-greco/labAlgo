from baseDS.DataStructure import DataStructure, DataStructureElement


class Dictionary(DataStructure):

    def __init__(self, baseDS:DataStructure):
        self._baseDS :DataStructure = baseDS

    def insert(self, element: DataStructureElement):
        self._baseDS.insert(element)

    def search(self, target):
        return self._baseDS.search(target) #gestire l'eccezione

    def delete(self, target):
        self._baseDS.delete(target) #gestire l'eccezione

    def __iter__(self):
        self._iterator = iter(self._baseDS)
        return self._iterator

    def __next__(self):
        return next(self._iterator)
