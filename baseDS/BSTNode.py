from baseDS.DataStructure import DataStructureElement


class BSTNode(DataStructureElement):
    def __init__(self, key, value):
        super().__init__(key, value)
        self._p = None
        self._left = None
        self._right = None

    def get(self):
        return self._key, self._value

    def set(self, key, value=None):
        self._key = key
        if value is not None: self._value = value

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def getP(self):
        return self._p

    def setLeft(self, left):
        self._left = left

    def setRight(self, right):
        self._right = right

    def setP(self, p):
        self._p = p
