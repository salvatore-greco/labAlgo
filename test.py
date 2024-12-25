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


def testAverage(dictionary: Dictionary, function, keys, nIter,*args):
    """
    Ritorna una media dei tempi di esecuzione di una particolare funzione e la dimensione del dizionario
    La misura è fatta ogni volta su un nuovo dizionario
    :param dictionary: dizionario su cui fare il test
    :param function: funzione da testare
    :param parameter: eventuali parametri di function
    :param keys: chiavi da inserire nel dizionario
    :param nIter: quante volte prendere la misura
    :return:
    """
    result = {}
    time = 0
    for _ in range(nIter):
        dictionary.clear()
        for i in range(len(keys)):
            dictionary.insertKV(keys[i],1)
        start = timer()
        try:
            function(*args)
        except KeyError:
            pass
        finally:
            end = timer()
            time += (end-start)
            size = dictionary.size
    result['avgTime'] = time / nIter
    print(f'time/iter: {time/nIter}')
    result['size'] = size
    if isinstance(dictionary._baseDS, HashTable):
        (loadfactor, _) = dictionary._baseDS.getLoadFactors()
        result['loadFactor'] = loadfactor
    return result