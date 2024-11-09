# Voglio usare il doppio hash quindi qui ci sarà la funzione hash da utilizzare per fare ciò

def h(k,i, m):
    def _h1():
        return k%m
    def _h2():
        return (2*_h1())+1 #da ricontrollare a ricevimento col professore perchè voglio usare un doppio hash
    #h2 deve generare sempre un numero dispari in modo che sia sempre primo rispetto a m
    return (_h1()+(i*_h2()))%m