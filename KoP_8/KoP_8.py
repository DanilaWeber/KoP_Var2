## Задание 8 ##
import pandas as pd

filmsFile = pd.read_csv('C:/Users/admin/source/repos/KoP_Var2/KoP_8/films.csv')
filmsFrame = pd.DataFrame(filmsFile['original_title'])

wordSet = set()

for i in filmsFrame.original_title:
    for j in str(i).split(' '):
        wordSet.add(j)

print(len(wordSet))