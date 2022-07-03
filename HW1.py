
"""декоратор печатающий на экран время работы функции"""

from time import sleep
import datetime

def outer(funk):
    def inter(*args,**kwargs):
        start = datetime.datetime.now()
        funk()
        finish = datetime.datetime.now()
        print (finish - start)
    return inter()

@outer
def funkt():
    sleep(5)




"""функция для вычисления очередного числа Фибоначчи"""
def fibb(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        l = [0,1]+[0]*(n-2)
        for k in range(2,n):
            l[k]=l[k-1]+l[k-2]
        return l[n-1]
#
# print(fibb(20))


"""функция, принимающая 3 позиционных аргумента и возвращающая сумму двух наименьших из них"""

def summ_min(a,b,c, *args):
    return a+b+c-max(a,b,c)
#
# print(summ_min(17,23,150,250))

"""добавил домашку в новую ветку"""