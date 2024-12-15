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
    def __init__(self, baseDS):
        self.dictionary = Dictionary(baseDS)
        self.dataGenerator = DataGenerator()

    def clearDictionary(self):
        baseDS = type(self.dictionary._baseDS)()
        self.dictionary = Dictionary(baseDS)

    def insert(self, size=10000):
        key = self.dataGenerator.generateKey(size, upper_bound=2000000)
        value = self.dataGenerator.generateValue(size)
        plot_name = f"{self.dictionary._baseDS}_insert.png"
        # Insert test
        insertTimes = testInsert(self.dictionary, key, value)

        # plot oo style
        fig, ax = plt.subplots()
        ax.plot(range(len(insertTimes)), insertTimes)
        ax.set_xlabel('Numero di elementi')
        ax.set_ylabel('Tempo')
        ax.set_title(f'Inserimento {self.dictionary._baseDS}')
        print(f"Generating plot {plot_name}")
        plt.savefig(f"../plot/{plot_name}")


    def search(self, maxSize=100000):
        searchTimes = []
        searchTimesNoSuccess = []
        plot_name = f"{self.dictionary._baseDS}_search.png"

        # Ricerca con successo
        size = 10
        while size <= maxSize:
            self.clearDictionary()
            keys = self.dataGenerator.generateKey(size)
            for key in np.nditer(keys):
                self.dictionary.insertKV(key, 1)
            searchTimes.append(testSearch(self.dictionary, keys[randint(0, len(keys) - 1)]))
            size *= 10

        # Ricerca senza successo
        size = 10
        while size <= maxSize:
            self.clearDictionary()
            keys = self.dataGenerator.generateKey(size)
            for key in np.nditer(keys):
                self.dictionary.insertKV(key, 1)
            searchTimesNoSuccess.append(
                testSearch(self.dictionary, -1))  # Metto -1 perchè so che non viene mai generato dal dataGenerator
            size *= 10

        fig, ax = plt.subplots()
        ax.set_title(f'Ricerca {self.dictionary._baseDS}')
        dimSuccess = [i['size'] for i in searchTimes]
        timeSuccess = [i['time'] for i in searchTimes]
        dimNoSuccess = [i['size'] for i in searchTimesNoSuccess]
        timeNoSuccess = [i['time'] for i in searchTimesNoSuccess]

        ax.plot(dimSuccess, timeSuccess, label='Con successo')
        ax.plot(dimNoSuccess, timeNoSuccess, label='Senza successo')
        ax.set_xlabel('Numero di elementi')
        ax.set_ylabel('Tempo')
        ax.legend()
        print(f"Generating plot {plot_name}")
        plt.savefig(f"../plot/{plot_name}")

    def delete(self, maxSize=100000):
        deleteTime = []
        plot_name = f"{self.dictionary._baseDS}_delete.png"

        size = 10
        while size <= maxSize:
            self.clearDictionary()
            keys = self.dataGenerator.generateKey(size)
            for key in np.nditer(keys):
                self.dictionary.insertKV(key, 1)
            deleteTime.append(testDelete(self.dictionary, keys[randint(0, len(keys) - 1)]))
            size *= 10

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