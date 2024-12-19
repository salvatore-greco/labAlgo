import numpy as np


# https://stackoverflow.com/questions/8505651/non-repetitive-random-number-in-numpy
class DataGenerator:
    def __init__(self):
        self._generator = np.random.default_rng()

    def generateKey(self, size):
        """
        Genera una sequenza pseudo casuale di interi senza ripetizione.
        :param size: dimensione dell'array di numeri casuali da generare
        :return: numpy.ndarray di dimensione size con i numeri generati casualmente
        """
        upper_bound = size*3
        arr = self._generator.choice(upper_bound, size=size, replace=False)
        self._generator.shuffle(arr)
        return arr

    def generateValue(self, size):
        """
        Genera una sequenza pseudocasuale di interi, con possibile ripetizione
        :param size: dimensione dell'array di numeri casuali da generare
        :return: numpy.ndarray di dimensione size con i numeri generati casualmente
        """
        upper_bound = size*3

        return self._generator.integers(low=0, high=upper_bound, size=size)
