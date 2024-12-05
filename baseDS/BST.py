from baseDS.BSTNode import BSTNode
from baseDS.DataStructure import DataStructure


# Gran parte del codice è gentilmente copiato (e adattato) dal libro :)

class BST(DataStructure):
    def __init__(self):
        self._root = None

    def getRoot(self):
        return self._root

    def insert(self, node: BSTNode):
        """
        Helper function per inserire un nodo già fatto nell'ABR
        :param node: BSTNode
        :return:
        """
        y = None
        x = self._root
        while x is not None:
            y = x
            if node.getKey() < x.getKey():
                x = x.getLeft()
            else:
                x = x.getRight()
        node.setP(y)
        if y is None:
            self._root = node
        elif node.getKey() < y.getKey():
            y.setLeft(node)
        else:
            y.setRight(node)

    def insertKeyValue(self, key, value):
        """
        Inserisce un nodo nell'ABR
        :param key: chiave del nodo da inserire
        :param value: dato satellite
        :return:
        """
        node = BSTNode(key, value)
        self.insert(node)

    def search(self, target):
        """
        Ricerca nell'ABR
        :param target: chiave da ricercare nell'albero
        """
        current = self._root
        while current is not None and target != current.getKey():
            if target < current.getKey():
                current = current.getLeft()
            else:
                current = current.getRight()
        if current is None: raise KeyError
        return current

    def inorderTreeWalk(self, current):
        if current is not None:
            self.inorderTreeWalk(current.getLeft())
            print(current.getKey())
            self.inorderTreeWalk(current.getRight())

    def rootInorderTreeWalk(self):
        self.inorderTreeWalk(self._root)

    def treeMinimum(self, current: BSTNode | None = None):
        if current is None: current = self._root
        while current.getLeft() is not None:
            current = current.getLeft()
        return current

    def transplant(self, u, v):
        """
        Trapianta il sottoalbero con radice in u con il sottoalbero con radice in v
        :param u: radice del sottoalbero destinazione
        :param v: radice del sottoalbero sorgente
        :return:
        """
        if u.getP() is None:
            self._root = v
        elif u == u.getP().getLeft():
            u.getP().setLeft(v)
        else:
            u.getP().setRight(v)
        if v is not None:
            v.setP(u.getP())

    def deleteNode(self, targetNode: BSTNode):
        """
        elimina un nodo dall'albero
        :param targetNode: nodo da eliminare
        :return:
        """
        if targetNode.getLeft() is None:
            self.transplant(targetNode, targetNode.getRight())
        elif targetNode.getRight() is None:
            self.transplant(targetNode, targetNode.getLeft())
        else:
            y = self.treeMinimum(targetNode.getRight())
            if y.getP() is not targetNode:
                self.transplant(y, y.getRight())
                y.setRight(targetNode.getRight())
                y.getRight().setP(y)
            self.transplant(targetNode, y)
            y.setLeft(targetNode.getLeft())
            y.getLeft().setP(y)

    def delete(self, key):
        """
        elimina un nodo data la chiave
        può lanciare un eccezione KeyError se la chiave non è presente
        :param key: chiave del nodo da eliminare
        :return:
        """
        node = self.search(key)  # non gestisco l'eccezione, la faccio gestire al chiamante
        self.deleteNode(node)

    def treeSuccessor(self, start: BSTNode | None = None):
        if start is None: start = self._root
        if start.getLeft() is not None:
            return self.treeMinimum(start.getRight())
        else:
            y = start.getP()
            while y is not None and start is y.getRight():
                start = y
                y = start.getP()  # non vorrei cambiasse anche il valore di start...
            return y

    # definisco iteratore e next per scorrere l'albero (in senso inorder) per scorrere il dizionario successivamente
    def __iter__(self):
        self._current = self.treeMinimum()
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        oldCurrent = self._current
        self._current = self.treeSuccessor(self._current)
        return oldCurrent
