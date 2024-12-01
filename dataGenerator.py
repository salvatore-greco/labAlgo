import numpy as np

# https://stackoverflow.com/questions/8505651/non-repetitive-random-number-in-numpy
class DataGenerator:
    def __init__(self):
        self._generator = np.random.default_rng()

    def generateKey(self, size,upper_bound=100000):
        """
        Genera una sequenza pseudo casuale di interi senza ripetizione.
        :param size: dimensione dell'array di numeri casuali da generare
        :param upper_bound: dimensione dell'intervallo di generazione
        :return: numpy.ndarray di dimensione size con i numeri generati casualmente
        """
        arr = self._generator.choice(upper_bound, size=size,replace=False)
        self._generator.shuffle(arr)
        return arr

    def generateValue(self, size,upper_bound=100000):
        """
        Genera una sequenza pseudocasuale di interi, con possibile ripetizione
        :param size: dimensione dell'array di numeri casuali da generare
        :param upper_bound: dimensione dell'intervallo di generazione
        :return: numpy.ndarray di dimensione size con i numeri generati casualmente
        """
        return self._generator.integers(low=0, high=upper_bound, size=size)