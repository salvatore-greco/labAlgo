"""
N.B: QUESTI NON SONO I TEST PREVISTI PER IL LABORATORIO!!
SONO UNIT TEST PER TESTARE SE L'IMPLEMENTAZIONE DELLE STRUTTURE DATI "DI BASE" SONO CORRETTE
(vabbè questi non li mando)(forse)
"""
import unittest

from baseDS.LinkedList import LinkedList, Element


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()
        self.list.insert(element=Element(1, 2))
        self.list.insert(element=Element(3, 2))

    def test_insert(self):
        self.assertEqual(self.list._head.getKey(), 3)
        self.list.insert(element=Element(4, 2))
        self.assertEqual(self.list._head.getKey(), 4)
        self.assertEqual(self.list._head.getNext().getKey(), 3)

    def test_search(self):
        with self.assertRaises(KeyError):
            self.list.search(2)
        x = self.list.search(1)
        self.assertEqual(x.getKey(), 1)

    def test_delete(self):
        self.list.delete(3)
        self.assertEqual(self.list._head.getKey(), 1)
        self.list.insert(element=Element(3, 2))
        self.list.delete(1)
        with self.assertRaises(KeyError):
            self.list.search(1)

    def helperTraverseLinkedList(self, item):
        if item is not None:
            yield item.getKey()
            yield from self.helperTraverseLinkedList(item.getNext())

    def test_iteration(self):
        l = []
        for i in self.list:
            l.append(i)

        iterator = iter(l)
        for item in self.helperTraverseLinkedList(self.list.getHead()):
            self.assertEqual(item, next(iterator).getKey())

if __name__ == '__main__':
    unittest.main()
