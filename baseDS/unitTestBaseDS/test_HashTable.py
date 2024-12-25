import unittest
from baseDS.HashTable import Element, HashTable
from baseDS.HashFunction import h

# Sti test son dei troiai. Non sono richiesti dall'esercizio, li faccio per vedere se ho implementato tutto correttamente

class HashFunctionTest(unittest.TestCase):
    def test_function(self):
        # ho fatto dei test su un foglio provando a simulare l'inserimento, riporto qui i valori fatti per testare
        self.assertEqual(h(10, 0, 2), 0)
        self.assertEqual(h(15, 0,2), 1)
        self.assertEqual(h(10,0,4), 2)
        self.assertEqual(h(2,0,4), 2)
        self.assertEqual(h(2,1,4), 3)
        self.assertEqual(h(2,2,4), 0)
        self.assertEqual(h(7,1,8), 6)
        self.assertEqual(h(7,2,8), 5)

class InsertTest(unittest.TestCase):
    def setUp(self):
        self.hashTable = HashTable()


    def test_insert(self):
        value = [10, 15, 2 , 1000, 7]
        for item in value:
            self.hashTable._insert(Element(item, 1))

        self.assertEqual(self.hashTable._n, len(value))
        self.assertEqual(self.hashTable._m, len(self.hashTable._table))


class OtherTest(unittest.TestCase):
    def setUp(self):
        self.hashTable = HashTable()
        value = [10, 15, 2, 1000, 7]
        for item in value:
            self.hashTable._insert(Element(item, 1))

    def test_search(self):
        self.hashTable.search(10)
        with self.assertRaises(KeyError):
            self.hashTable.search(9)

    def test_delete(self):
        self.hashTable.delete(10)
        with self.assertRaises(KeyError):
            self.hashTable.search(10)
        self.hashTable._insert(Element(23, 1))
        self.assertEqual(self.hashTable._table[h(23,0, self.hashTable._m)].getKey(), 23)

if __name__ == '__main__':
    unittest.main()
