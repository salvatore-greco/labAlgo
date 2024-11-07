# Chissà se questo type checking sarà giusto
class Element:
    def __init__(self, key, value):
        self._key = key  # dato che devo implementare un dizionario, suppongo (ai fini del dizionario appunto) che questa chiave sia unica
        self._value = value
        self._next: Element | None = None
        self._prev: Element | None = None

    def getKey(self):
        return self._key

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setNext(self, newNext):
        self._next = newNext

    def getPrev(self):
        return self._prev

    def setPrev(self, newPrev):
        self._prev = newPrev


class LinkedList:
    # Ipotizziamo che non abbiamo il puntatore alla fine della lista.
    def __init__(self):
        self.head: Element | None = None

    def insert(self, element: Element):
        if self.head is None:
            self.head = element
        else:
            element.setNext(self.head)
            self.head.setPrev(element)
            self.head = element

    def search(self, target) -> Element:
        x = self.head
        while x is not None and x.getKey() != target:
            x = x.getNext()
        if x is None: raise KeyError
        return x  # se x è none significa che l'elemento non è presente (potrei lanciare un eccezione ma boh)

    def delete(self, target):
        """
        chiama da sè self.search!
        :param target: chiave da eliminare
        """
        x = self.search(target)  # l'eccezione voglio che venga gestita da chi chiama delete
        if x is self.head:
            x.getNext().setPrev(None)
            self.head = x.getNext()
        else:
            x.getPrev().setNext(x.getNext())
            if x.getNext() is not None:
                x.getNext().setPrev(x.getPrev())
