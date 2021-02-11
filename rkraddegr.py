#RÓWNANIE KWADRATOWE OKIENKO 0.1 - radiansToDegrees
from math import *

def radiansToDegrees(self,alfa):
    '''Zamiana kąta w radianach na kąt w stopniach'''

    #modf(x) - zwraca część ułamkową i całkowita 'x' w postaci krotki
    #modf(x) --> (cz. ułamowa, cz. całkowita)
    alfa = degrees(alfa)
    st = alfa
    if st < 0:
        st = 180 + st
    st_cu = modf(st) 
    st_c = st_cu[1]         #część całkowita stopni
    st_u = st_cu[0]         #część ułamkowa (dziesiętna) stopni
    min_ = st_u*60          #wyliczenie minut stopniowych
    min_cu = modf(min_)
    min_c = min_cu[1]       #część całkowita minut
    min_u = min_cu[0]       #część ułamkowa (dziesiętna) minut
    sek = min_u * 60        #wyliczenie sekund stopniowych
    sek = round(sek,0)      #zaokrąglenie sekund stopniowych do '00'
    if sek == 60:           #dodanie 1 min. przy zaokrąglaniu sekund do 60
        sek = 0
        min_c +=1
    if min_c == 60:         #dodanie 1 st. przy zaokrąglaniu minut do 60
        min_c = 0
        st_c +=1
    st_c_i = int(st_c)      #stopnie - liczba całkowita (int)
    min_c_i = int(min_c)    #minuty - liczba całkowita (int)
    sek_i = int(sek)        #sekundy - liczba całkowita (int)

    return st_c_i, min_c_i, sek_i

