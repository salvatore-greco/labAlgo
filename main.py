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
    tester = Tester(LinkedList(), keys=False, filename='keys24.p')
    tester.runAllAvgTest()

    tester = Tester(HashTable(), keys=False, filename='keys24.p')
    tester.insert()
    tester.searchAvg(False)
    tester.deleteAvg(False)

    tester = Tester(BST(), keys=False, filename='keys24.p')
    tester.runAllAvgTest()
    tester.insertAvg(ordered=True, points=False)


    print('Finito!')
