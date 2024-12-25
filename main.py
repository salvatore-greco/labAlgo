from baseDS.HashTable import HashTable
from baseDS.BST import BST
from baseDS.LinkedList import LinkedList
from tester import Tester

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
