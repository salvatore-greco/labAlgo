# Chissà se questo type checking sarà giusto
from baseDS.DataStructure import DataStructureElement, DataStructure


class Element(DataStructureElement):
    def __init__(self, key, value):
        super().__init__(key,value)
        self._next: Element | None = None
        self._prev: Element | None = None

    def getNext(self):
        return self._next

    def setNext(self, newNext):
        self._next = newNext

    def getPrev(self):
        return self._prev

    def setPrev(self, newPrev):
        self._prev = newPrev


class LinkedList(DataStructure):

    # Ipotizziamo che non abbiamo il puntatore alla fine della lista.
    def __init__(self):
        self._head: Element | None = None

    def getHead(self):
        return self._head

    def insertKV(self, key, value):
        self._insert(Element(key, value))

    def _insert(self, element: Element):
        if self._head is None:
            self._head = element
        else:
            element.setNext(self._head)
            self._head.setPrev(element)
            self._head = element

    def search(self, target) -> Element:
        x = self._head
        while x is not None and x.getKey() != target:
            x = x.getNext()
        if x is None: raise KeyError
        return x

    def delete(self, target):
        """
        chiama da sè self.search!
        :param target: chiave da eliminare
        """
        x = self.search(target)  # l'eccezione voglio che venga gestita da chi chiama delete
        if x is self._head:
            x.getNext().setPrev(None)
            self._head = x.getNext()
        else:
            x.getPrev().setNext(x.getNext())
            if x.getNext() is not None:
                x.getNext().setPrev(x.getPrev())

    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        current = self._current
        self._current = self._current.getNext()
        return current

    def __str__(self):
        return 'Linked List'
