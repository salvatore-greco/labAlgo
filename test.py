from timeit import default_timer as timer
from baseDS.HashTable import HashTable

from dictionary import Dictionary

def testInsert(dictionary: Dictionary, dataK: [], dataV: []):
    times = []
    for (key, value) in zip(dataK, dataV):
        start = timer()
        dictionary.insertKV(key, value)
        end = timer()
        times.append(end - start)

    return times


def testSearch(dictionary: Dictionary, key):
    # Dobbiamo scindere 2 casi, ricerca con successo e senza successo
    # Dobbiamo plottare vari test fatti con un dizionario che si espande piano piano
    result = {}
    start = timer()
    try:
        dictionary.search(key)
        end = timer()
        result = {'time': end - start, 'success': True, 'size': dictionary.size}
        if isinstance(dictionary._baseDS, HashTable):
            (loadfactor,_) = dictionary._baseDS.getLoadFactors()
            result['loadFactor'] = loadfactor
    except KeyError:
        end = timer()
        result = {'time': end - start, 'success': False, 'size': dictionary.size}
        if isinstance(dictionary._baseDS, HashTable):
            (loadfactor,_) = dictionary._baseDS.getLoadFactors()
            result['loadFactor'] = loadfactor
    finally:
        return result


def testDelete(dictionary: Dictionary, key):
    # È di interesse solo la cancellazione con successo perchè in caso sia senza successo
    # i tempi sarebbero sovrapponibili a quelli della ricerca senza successo
    result = {}
    start = timer()
    try:
        dictionary.delete(key)
        end = timer()
        result = {'time': end - start, 'success': True, 'size': dictionary.size}
    except KeyError:
        end = timer()
        result = {'time': end - start, 'success': False, 'size': dictionary.size}
    finally:
        return result
