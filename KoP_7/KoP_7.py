## Задание B ##
import pandas as pd

studentsPerf = pd.read_csv('C:/Users/admin/source/repos/KoP_Var2/KoP_7/StudentsPerformance.csv')

def crypt(students):
    cryptStr = []
    for i in students['parental level of education']:
        cryptStr.append(i.replace('a','*').replace('e','*').replace('i','+').replace('o','+'))
    return cryptStr

f = lambda x: crypt(x)

studentsPerf['crypted'] = f(studentsPerf)

print(studentsPerf)