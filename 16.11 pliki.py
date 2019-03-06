try:
    with open('plik', 'r') as plik:
        for n, linia in enumerate(plik):
            print(repr(linia))
except FileNotFoundError:
    print('nie ma pliku')
#r strip
# format

import os.path
os.path.splitext('plik.txt')
base, ext = os.path.splitext('plik.txt')
wynik = base + 'dfgdfg' + ext

#picle
#json
#yaml

import pickle

dane = {'sdg':'sdfg', 'sdfg':'sdfg'}
with open('data.picle','wb') as store:
    pickle.dump(dane, store)

with open('data.picle','rb') as store:
    pickle.load(store)


eval