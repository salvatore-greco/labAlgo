from HashFunction import h
from baseDS.DataStructure import DataStructure
from typing import List

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


class HashTable(DataStructure):

    def __init__(self):
        self._m = 2
        self._n = 0 #Size
        self._table : List[Element] | List[None] = [None] * self._m  # uso la lista di python perchè sì. Per inserire o accedere alla lista non uso i metodi di python ma [] perchè è tempo costante
        self._loadFactor = 0

    def _calcLoadFactor(self):
        self._loadFactor = self._n / self._m

    def insert(self, element):
        """
        Funzione che inserisce un elemento nella hash table
        :param element: Elemento (tipo Element) da inserire
        """
        # Non posso seguire lo pseudocodice di pagina 387 perchè usando il doppio hash, voglio che m sia sempre una potenza del 2
        if self._loadFactor > 0.7: # quindi deve essere sempre minore di 0.7 (costante <1)
            newTable = [None] * (2*self._m)
            #inserimento di tutti gli elementi di self._table in newTable
            for item in self:
                i = 0
                inserted = False
                while not inserted:
                    keyHash = h(item.getKey(), i, 2*self._m)
                    if newTable[keyHash] is None:
                        newTable[keyHash] = item
                        inserted = True
                        i = 0
                    else: i += 1
            del self._table
            self._table = newTable
            self._m *= 2
        self._hashInsert(element)
        self._n += 1
        self._calcLoadFactor()

    def delete(self, target):
        pass
        """
        vai a ricevimento. Dato che è a indirizzamento aperto se facessi cancellazioni (senza riallocare)
        il tempo di ricerca non dipenderebbe più dal fattore di carico.
        (a questo punto) Chiedi anche se indirizzamento aperto e doppio hash ha senso (e se ha senso il mio doppio hash)         
        """

    def __iter__(self):
        for i in range(0, len(self._table)):
            if self._table[i] is not None :
                self._current = i
        return self

    def __next__(self) -> Element :
        if self._current is None: raise StopIteration
        for i in range (self._current, len(self._table)):
            if self._table[i] is not None:
                self._current = i
                return self._table[i]
        raise StopIteration

    def _hashInsert(self, element):
        """
        helper function da usare nell'inserimento nella hash table (indirizzamento aperto)
        :param element: Elemento (tipo Element) da inserire
        """
        i = 0
        while i != self._m:
            keyHash = h(element.getKey(), i, self._m)
            if self._table[keyHash] is not None:
                self._table[keyHash] = element
                return
            else: i += 1
        # Non ci può essere il caso in cui non inserisce perchè è una tabella dinamica


    def search(self, target):
        """
        Funzione che ricerca una chiave all'interno della tabella
        :param target: chiave dell'elemento da trovare
        :return: Posizione dell'elemento
        """

        for i in range(0, self._m):
            hashKey = h(target, i, self._m)
            if self._table[hashKey].getKey() == target:
                return hashKey
            if self._table[hashKey] is None:
                raise KeyError