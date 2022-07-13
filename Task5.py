#Реализовать алгоритм перемешивания списка.

import random

n=int(input('Введите число N='))
sp=[]
i=0
while i<n+1:
    sp.append(i)
    i+=1
print(f'{sp} - Изначальный список')

random.shuffle(sp)
print(f'{sp} - Первый вариант перемешивания списка')

def rnd (sp,n):
    spn=[]
    spj=[]
    i=0
    while i <= n:
        j=random.randint(0,5)
        if j not in spj:           
            spj.append(j)
            spn.append(sp[j])
            i+=1            
    return spn
print(f'{rnd(sp,n)} - Второй вариант перемешивания списка')

