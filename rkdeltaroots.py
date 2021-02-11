#RÓWNANIE KWADRATOWE OKIENKO 0.1 - validate - modulo - delta i pierwiastki
from math import *
#import numpy as np
#import matplotlib.pyplot as plt
from tkinter import *

from rkplot import *
from rkraddegr import *
from rkequatios import *
first = 0
last = 7 


def generalFormGetFactor_abc(self,a,b,c):
    '''Ustalenie formy równania: kwadratowe czy inne'''

    if a == 0:
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(END, 'Ponieważ podany współczynnik ' \
                                + 'a = 0 nie jest to równanie kwadratowe')
        lineEquation(self,b,c)      #funkcja równania prostej
    else:
        delta_abc(self,a,b,c)   #funkcja obliceznia delty 
        
def canonicalFormGetFactor_abc(self,ac,p,q):
    '''Obliczenie współczynników "b,c" z "p,q" postaci kanonicznej równania'''

    b = round(-2*ac*p,4)
    try:
        c = round(q + ((b*b)/(4*ac)),4)
    except ZeroDivisionError:
        c = 0
    if ac == 0 and p == 0 and q == 0:
        self.results_txt.delete(0.0, END)   #wpis w polu WYNIKI
        self.results_txt.insert(0.0, 'Ponieważ podane współczynniki ' \
                                + '\na = 0, p = 0 i q = 0  \nrozwiązaniem równania' \
                                + ' jest punkt o współrzednych \nx = 0.0 i y = 0.0')
        plotPoint(self,)   #wydruk wykresu punktu

    elif ac == 0:
        self.results_txt.delete(0.0, END)   #wpis w polu WYNIKI
        self.results_txt.insert(0.0, 'Ponieważ podany współczynnik ' \
                                + 'a = 0 nie jest to równanie kwadratowe')
        lineEquation(self,b,c)      #funkcja obliczenia równania prostej
    else:
        a = ac
        delta_abc(self,a,b,c)   #funkcja obliczenia delty 

def productFormGetFactor_abc(self,ap,x1p,x2p):
    '''Obliczenie współczynników "b,c" z "x1p,x2p" postaci iloczynowej równania'''

    if ap == 0 and x1p == 0 and x2p == 0:
        self.results_txt.delete(0.0, END)   #wpis w polu WYNIKI
        self.results_txt.insert(0.0, 'Ponieważ podane współczynniki ' \
                                + '\na = 0, x₁ = 0 i x₂ = 0  \nrozwiązaniem równania' \
                                + ' jest punkt o współrzędnych \nx = 0.0 i y = 0.0')
        plotPoint(self)   #wydruk wykresu - punkt 0,0

    elif ap == 0:
        try:
            b = round(ap*((x2p*x2p - x1p*x1p)/(x1p - x2p)),4)
        except ZeroDivisionError:
            b = 0
        c = round(-(ap*x1p*x1p + b*x1p),4)

        self.results_txt.delete(0.0, END)   #wpis w polu WYNIKI
        self.results_txt.insert(0.0, 'Ponieważ podany współczynnik ' \
                                + 'a = 0 nie jest to równanie kwadratowe')
        lineEquation(self,b,c)      #funkcja oblicznia równania prostej

    else:       #obliczenie współczynników b i c
        a = ap
        try:
            b = round(ap*((x2p*x2p - x1p*x1p)/(x1p - x2p)),4)
        except ZeroDivisionError:
            b = 0
        c = round(-(ap*x1p*x1p + b*x1p),4)
        delta_abc(self,a,b,c)   #funkcja obliczenia delty 






#==============================================================================

def delta_abc(self,a,b,c):
    '''Obliczenie delty.'''

    delta = round (b*b-4*a*c,6)
    self.delta_txt.delete(0.0, END)
    self.delta_txt.insert(0.0, ' Δ = ' + str(delta))

    if delta > 0:
        #delta > 0 - Równanie posiada 1 pierwiastek (miejsce zerowe)
        x1 = round(root_x_1(self,a,b,c),4)
        if x1 == -0.0:
            x1 = 0.0
        x2 = round(root_x_2(self,a,b,c),4)
        if x2 == -0.0:
            x2 = 0.0
        x12 = ''
        self.zero_place_txt.delete(0.0, END)
        self.zero_place_txt.insert(0.0, 'x₁ = ' + str(x1) + '\nx₂ = '+ str(x2))

    elif delta == 0:
        #delta = 0 - Równanie posiada 1 pierwiastek wspólny (miejsce zerowe)
        x12 = round(root_x_12(self,a,b,c),4)
        if x12==-0.0:   #usunięcie znaku '-' przed 0.0
            x12 = 0.0
        x1, x2 = '',''
        self.zero_place_txt.delete(0.0, END)
        self.zero_place_txt.insert(0.0,'\nx₁₂ = '+ str(x12))
    else:
        #delta < 0 - Równanie nie posiada pierwiastków (miejsc zerowych)
        x1, x2, x12 = '','',''
        self.zero_place_txt.delete(0.0, END)
        self.zero_place_txt.insert(0.0,'Równanie nie posiada' + '\nmiejsc zerowych')

    generalFormEquation(self,a,b,c)             #funkcja tworząca postać ogólną równania kwadratowego
    productFormEquation(self,a,x1,x2,x12,delta) #funkcja tworząca postać iloczynową równania kwadratowego
    canonicalFormEquation(self,a,b,c)           #funkcja tworząca postać kanoniczną równania kwadratowego


def root_x_1(self,a,b,c):
    '''Pierwiastek 1)'''
    x1 = (-b + sqrt(b*b-4*a*c))/(2*a)
    return x1

def root_x_2(self,a,b,c):
    '''Pierwiastek 2)'''
    x2 = (-b - sqrt(b*b-4*a*c))/(2*a)
    return x2

def root_x_12(self,a,b,c):
    '''Pierwiastek wspólny 1,2)'''
    x12 = -b /(2*a)
    return x12


