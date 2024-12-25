from baseDS.DataStructure import DataStructure, DataStructureElement


class Dictionary(DataStructure):

    def __init__(self, baseDS: DataStructure):
        self._baseDS: DataStructure = baseDS
        self.size = 0

    def clear(self):
        self._baseDS = type(self._baseDS)()
        self.size = 0

    def _insert(self, element: DataStructureElement):
        self._baseDS._insert(element)
        self.size += 1

    def insertKV(self, key, value):
        self._baseDS.insertKV(key, value)
        self.size += 1

    def search(self, target):
        return self._baseDS.search(target)  # gestire l'eccezione

    def delete(self, target):
        self._baseDS.delete(target)  # gestire l'eccezione
        self.size -= 1

    def __iter__(self):
        self._iterator = iter(self._baseDS)
        return self._iterator

    def __next__(self):
        return next(self._iterator)
