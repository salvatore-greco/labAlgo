from dataGenerator import DataGenerator
from test import *
from dictionary import Dictionary
import matplotlib.pyplot as plt
from random import randint

"""
Qui ci scrivo le funzioni per effettivamente testare le prestazioni del dizionario
Generano i grafici
"""


class Tester:
    def __init__(self, baseDS, insertSize=10000, searchSize=100000, deleteSize=100000, minSize=10, nIter=20):
        self.dictionary = Dictionary(baseDS)
        self.dataGenerator = DataGenerator()
        self.insertSize = insertSize
        self.searchSize = searchSize
        self.deleteSize = deleteSize
        self.minSize = minSize
        self.step = 1000
        self.stepAvg = 3
        self.nIter = nIter

    def clearDictionary(self):
        baseDS = type(self.dictionary._baseDS)()
        self.dictionary = Dictionary(baseDS)

    def insert(self):
        key = self.dataGenerator.generateKey(self.insertSize)
        value = self.dataGenerator.generateValue(self.insertSize)
        plot_name = f"{self.dictionary._baseDS}_insert.png"
        plot_title = f'Inserimento {self.dictionary._baseDS}'
        # Insert test
        insertTimes = testInsert(self.dictionary, key, value)

        generatePlot(range(len(insertTimes)), insertTimes, plot_title, plot_name)

    def search_helper(self, searchTimes, success: bool):
        for size in range(self.minSize, self.searchSize, self.step):
            self.clearDictionary()
            keys = self.dataGenerator.generateKey(size)
            for key in np.nditer(keys):
                self.dictionary.insertKV(key, 1)
            if success:
                searchTimes.append(testSearch(self.dictionary, keys[randint(0, len(keys) - 1)]))
            else:
                searchTimes.append(testSearch(self.dictionary, -1))

    def search(self):
        searchTimes = []
        searchTimesNoSuccess = []
        plot_name = f"{self.dictionary._baseDS}_search.png"

        # Ricerca con successo
        self.search_helper(searchTimes, True)

        # Ricerca senza successo
        self.search_helper(searchTimesNoSuccess, False)

        fig, ax = plt.subplots()
        ax.set_title(f'Ricerca {self.dictionary._baseDS}')
        dimSuccess = [i['size'] for i in searchTimes]
        timeSuccess = [i['time'] for i in searchTimes]
        dimNoSuccess = [i['size'] for i in searchTimesNoSuccess]
        timeNoSuccess = [i['time'] for i in searchTimesNoSuccess]

        fig, ax = plt.subplots()
        ax.set_title(f'Ricerca {self.dictionary._baseDS}')

        ax.plot(dimSuccess, timeSuccess, label='Con successo')
        ax.plot(dimNoSuccess, timeNoSuccess, label='Senza successo')

        ax.set_xlabel('Numero di elementi')
        ax.set_ylabel('Tempo')
        ax.legend()
        print(f"Generating plot {plot_name}")
        plt.savefig(f"../plot/{plot_name}")
        if isinstance(self.dictionary._baseDS, HashTable):
            loadFSucc = [1 / (1 - i['loadFactor']) for i in searchTimes]
            loadFNoSucc = [(1 / i['loadFactor']) * (math.log(1 / i['loadFactor'], math.e)) for i in
                           searchTimesNoSuccess]
            fig1, ax1 = plt.subplots()
            ax1.plot(dimSuccess, loadFSucc, label='load f succ')
            ax1.plot(dimSuccess, loadFNoSucc, label='load f no succ')
            ax1.legend()
            plt.savefig(f'../plot/prova_load_factor')

    def delete(self):
        deleteTime = []
        plot_name = f"{self.dictionary._baseDS}_delete.png"
        plot_title = f'Cancellazione {self.dictionary._baseDS}'
        self.delete_helper(deleteTime)
        dim = [i['size'] for i in deleteTime]
        time = [i['time'] for i in deleteTime]

        generatePlot(dim, time, plot_title, plot_name)

    def delete_helper(self, deleteTime):
        size = 10
        while size <= self.deleteSize:
            self.clearDictionary()
            keys = self.dataGenerator.generateKey(size)
            for key in np.nditer(keys):
                self.dictionary.insertKV(key, 1)
            deleteTime.append(testDelete(self.dictionary, keys[randint(0, len(keys) - 1)]))
            size *= self.step

        fig, ax = plt.subplots()
        ax.set_title(f'Cancellazione {self.dictionary._baseDS}')
        dim = [i['size'] for i in deleteTime]
        time = [i['time'] for i in deleteTime]

        ax.plot(dim, time)
        ax.set_xlabel('Numero di elementi')
        ax.set_ylabel('Tempo')

        print(f"Generating plot {plot_name}")
        plt.savefig(f"../plot/{plot_name}")

    def runAllTest(self):
        self.insert()
        self.search()
        self.delete()