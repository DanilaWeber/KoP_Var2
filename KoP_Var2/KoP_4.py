## Часть А ##
#text = 'стол букет стол букет ваза букет'.split()
text = input('Введите текст\n').split()

wordDict = {}.fromkeys(set(text),0)

for i in text:
    wordDict.update({i:wordDict[i]+1})

print(wordDict.items(),end = '\n\n')

## Часть B ##
import json

with open('C:/Users/admin/source/repos/KoP_Var2/KoP_Var2/data.json','r') as file:
    data = json.load(file)

actionsCount = 0

for i in data['events_data']:
    if i['client_id'] == 60459:
        actionsCount += 1

print(actionsCount)