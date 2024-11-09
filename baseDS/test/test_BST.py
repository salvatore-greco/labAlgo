import unittest

from baseDS.BST import BST, BSTNode


class InsertTest(unittest.TestCase):
    def setUp(self):
        self.tree = BST()

    def helper_traverse_tree(self, root): #è tipo una preorder ma che ritorna le chiavi, ganzo
        if root is not None:
            yield root.getKey()
            yield from self.helper_traverse_tree(root.getLeft())
            yield from self.helper_traverse_tree(root.getRight())

    def test_insert(self):
        # L'albero l'ho scritto sulla mia fantastica lavagnetta, lo riporto con la notazione parentesizzata
        # 50(20(10,30(25,31)),80(79,90(89,91)))
        #se insert funziona lo reinserisco nel setup della prossima fixture :)
        values = [50,20,10,30,25,31,80,79,90,89,91]
        for value in values:
            self.tree.insertKeyValue(value, 1)
        #self.tree.rootInorderTreeWalk()

        #controlliamo sulla struttura dell'albero è corretta
        root = self.tree.getRoot()
        iter_value = iter(values)
        for key in self.helper_traverse_tree(root):
            self.assertEqual(key, next(iter_value))


class OtherTest(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        values = [50, 20, 10, 30, 25, 31, 80, 79, 90, 89, 91]
        for value in values:
            self.tree.insertKeyValue(value, 1)

    def test_search(self):
        with self.assertRaises(KeyError):
            self.tree.search(100)
        self.tree.search(30)
        node = BSTNode(92,1)
        self.tree.insert(node)
        foundNode = self.tree.search(92)
        self.assertIs(node, foundNode)

    def test_minimum(self):
        self.assertEqual(10, self.tree.treeMinimum().getKey())
        node = self.tree.search(80)
        self.assertEqual(79, self.tree.treeMinimum(node).getKey())

    def test_delete(self):
        self.tree.delete(20)
        with self.assertRaises(KeyError):
            self.tree.search(20)

    def test_successor(self):
        key = self.tree.treeSuccessor()
        if key is not None: key = key.getKey()
        self.assertEqual(key, 79)
        key = self.tree.treeSuccessor(self.tree.search(79))
        if key is not None: key = key.getKey()
        self.assertEqual(key, 80)
        key = self.tree.treeSuccessor(self.tree.search(91))
        if key is not None: key = key.getKey()
        self.assertIsNone(key)

    def helper_inorder_tree(self, root):
        if root is not None:
            yield from self.helper_inorder_tree(root.getLeft())
            yield root.getKey()
            yield from self.helper_inorder_tree(root.getRight())

    def test_iterator(self):
        l = []
        for i in self.tree:
            l.append(i.getKey())

        #print (l)
        iterator = iter(l)
        for item in self.helper_inorder_tree(self.tree.getRoot()):
            self.assertEqual(item, next(iterator))


if __name__ == '__main__':
    unittest.main()
