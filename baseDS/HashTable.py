from baseDS.HashFunction import h
from baseDS.DataStructure import DataStructure, DataStructureElement
from typing import List


# TODO: Testare questa fantastica struttura dati (come hai fatto con le altre)

class Element(DataStructureElement):
    def __init__(self, key, value):
        super().__init__(key, value)
        self._deleted = False

    def isDeleted(self):
        return self._deleted

    def setDeleted(self, deleted: bool):
        self._deleted = deleted


class HashTable(DataStructure):

    def __init__(self):
        self._m = 2
        self._n = 0  # Size
        self._numberOfDeletedElement = 0
        self._table: List[Element] | List[None] = [
                                                      None] * self._m  # uso la lista di python perchè sì. Per inserire o accedere alla lista non uso i metodi di python ma [] perchè è tempo costante
        self._loadFactor = 0

    def _calcLoadFactor(self):
        """
        Calcola il fattore di carico non tenendo conto degli elementi cancellati.\n
        I tempi di ricerca non dipenderanno da questo fattore di carico visto che gli elementi cancellati
        non dovrebbero fare parte della tabella hash, ma non possono essere eliminati perchè interromperebbero
        la sequenza di ispezione.
        """
        self._loadFactor = self._n / self._m

    def _calcLoadFactorWithDeletion(self):
        """
        Calcola il fattore di carico tenendo conto anche degli elementi cancellati.\n
        Importante perchè i tempi di ricerca dipenderanno da questo fattore di carico
        invece che da self._loadFactor
        """
        self.loadFactorWithDeletion = (self._n + self._numberOfDeletedElement) / self._m

    def _moveToNewTable(self, newDimension):
        newTable = [None] * newDimension
        # inserimento di tutti gli elementi di self._table in newTable
        for item in self:
            i = 0
            inserted = False
            if item.isDeleted(): continue
            while not inserted:
                keyHash = h(item.getKey(), i, newDimension)
                if newTable[keyHash] is None:
                    newTable[keyHash] = item
                    inserted = True
                    i = 0
                else:
                    i += 1
        del self._table
        self._table = newTable
        self._m = newDimension

    def insert(self, element):
        """
        Funzione che inserisce un elemento nella hash table
        :param element: Elemento (tipo Element) da inserire
        """

        # Non posso seguire lo pseudocodice di pagina 387 perchè usando il doppio hash, voglio che m sia sempre una
        # potenza del 2
        if self._loadFactor > 0.5:  # quindi deve essere sempre minore di 0.7 (costante <1)
            self._moveToNewTable(self._m * 2)
        self._hashInsert(element)
        self._n += 1
        self._calcLoadFactor()
        self._calcLoadFactorWithDeletion()

    def delete(self, target):
        if self._hashDelete(target):
            if self._loadFactor < 0.35:
                self._moveToNewTable(int(self._m / 2))
            self._n -= 1
            self._numberOfDeletedElement += 1
            self._calcLoadFactor()
            self._calcLoadFactorWithDeletion()
        else:
            raise KeyError("The requested key is not in the table")

        """
        vai a ricevimento. Dato che è a indirizzamento aperto se facessi cancellazioni (senza riallocare)
        il tempo di ricerca non dipenderebbe più dal fattore di carico.
        (a questo punto) Chiedi anche se indirizzamento aperto e doppio hash ha senso (e se ha senso il mio doppio hash)
        """

    def _hashInsert(self, element):
        """
        helper function da usare nell'inserimento nella hash table (indirizzamento aperto)
        :param element: Elemento (tipo Element) da inserire
        """
        i = 0
        while i != self._m:
            keyHash = h(element.getKey(), i, self._m)
            if self._table[keyHash] is None or self._table[keyHash].isDeleted():
                if self._table[keyHash] is not None and self._table[keyHash].isDeleted():
                    self._numberOfDeletedElement -= 1
                self._table[keyHash] = element
                return
            else:
                i += 1
        # Non ci può essere il caso in cui non inserisce perchè è una tabella dinamica

    def _hashDelete(self, target):
        try:
            elementToDelete = self.search(target)
            self._numberOfDeletedElement += 1
            elementToDelete.setDeleted(True)
            return True
        except KeyError:
            return False

    def search(self, target):
        """
        Funzione che ricerca una chiave all'interno della tabella
        :param target: chiave dell'elemento da trovare
        :return: Posizione dell'elemento
        """

        for i in range(0, self._m):
            hashKey = h(target, i, self._m)
            if self._table[hashKey] is None or self._table[hashKey].isDeleted():
                raise KeyError
            elif self._table[hashKey].getKey() == target:
                return self._table[hashKey]

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self) -> Element:
        while self._current < len(self._table):
            current_value = self._table[self._current]
            self._current += 1
            if current_value is not None:
                return current_value
        raise StopIteration
