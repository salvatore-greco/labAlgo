from random import random, randint

import numpy as np

from dictionary import Dictionary
from baseDS.HashTable import HashTable
from baseDS.BST import BST
from baseDS.LinkedList import LinkedList
from baseDS.DataStructure import DataStructureElement
from dataGenerator import DataGenerator
from tester import Tester
import pickle

if __name__ == '__main__':

    tester = Tester(LinkedList())
    tester.runAllTest()

    tester = Tester(HashTable())
    tester.runAllTest()

    tester = Tester(BST())
    tester.runAllTest()

    # Search test con successo

    # plt.show()

    # keyR = np.arange(1,10000)
    # times = testInsert(dictionary,keyR, value)
    # plt.figure()
    # plt.plot(range(0, len(times)), times)
    # plt.show()


