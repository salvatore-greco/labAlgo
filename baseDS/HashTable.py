from HashFunction import h


class Element:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        #self._deleted = False su questo ci voglio ripensare

    def getKey(self):
        return self._key

    def getValue(self):
        return self._value

    def setKey(self, newKey):
        self._key = newKey

    def setValue(self, newValue):
        self._value = newValue


class HashTable:
    def __init__(self):
        self._m = 2
        self._n = 0
        self._table = [None] * self._m  # uso la lista di python perchè sì. Per inserire o accedere alla lista non uso i metodi di python ma [] perchè è tempo costante
        self._loadFactor = 0

    def _calcLoadFactor(self):
        self._loadFactor = self._n / self._m
