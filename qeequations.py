#RÓWNANIE KWADRATOWE OKIENKO 0.1 - equations - równania
from math import *
from tkinter import *
from qeplot import *
from qeraddegr import *


def generalFormEquation(self,a,b,c): #Ogólna postać równania kwadratowego
    '''Ogólna postać równania kwadratowego'''
    if b == 0: b = 0.0
    if b < 0: b = -b; m = '-'
    else: m = '+'
    if c < 0: c = -c; n = '-'
    else: n = '+'
    self.general_txt.delete(0.0, END)   #wpis w polu postaci ogólnej równania
    self.general_txt.insert(0.0, 'f(x) = ' + str(a) + 'x² ' + m + ' ' + str(b) + 'x ' + n + ' ' + str(c))

def canonicalFormEquation(self,a,b,c):
    '''Postać kanoniczna równania.'''
    p = round(-b/(2*a),4)
    if p == -0.0:
        p=0.0
    q = round(- (b*b-4*a*c)/(4*a),4)
    if q == -0.0: q=0.0
    p1 = p; q1 = q

    if p1 < 0: p1 = -p1; m = '+'
    else: m = '-'
    if q1 < 0: q1 = -q1;n = '-'
    else: n = '+'
    self.canon_txt.delete(0.0, END)   #wpis w polu postaci kanonicznej równania
    self.canon_txt.insert(0.0, 'f(x) = ' + str(a) + ' *(x '+ m + ' ' + str(p1) \
                          + ')² ' + n + ' ' + str(q1))

    #Współrzedne wierzchołka funkcji
    self.function_vertex_txt.delete(0.0, END)   #wpis w polu wierzchołka funkcji kwadratowej (równania)
    self.function_vertex_txt.insert(0.0,'p = x = '+ str(p) + '\nq = y = ' + str(q))
        
    courseFunctionVariability(self,a,p) #Opis przebiegu zmienności funkcji

    plotQuadraticFunc(self,a,b,c,p,q)   #utworzenie wykresu funkcji kwadratowej (równania)

def productFormEquation(self,a,x1,x2,x12,delta):
    '''Postać iloczynowa równania'''

    if delta > 0:
        x_1d = x1
        x_2d = x2
        if x_1d < 0: x_1d = -x_1d; m = '+'
        else: m = '-'
        if x_2d < 0: x_2d = -x_2d; n = '+'
        else: n = '-'
        self.product_txt.delete(0.0, END)   #wpis w polu postaci iloczynowej równania
        self.product_txt.insert(0.0, 'f(x) = ' + str(a) + ' *(x ' \
                                + m + ' ' + str(x_1d) + ')*(x ' + n \
                                + ' ' + str(x_2d) + ')')
    elif delta == 0:
        x_12d = x12
        if x_12d < 0: x_12d = -x_12d; m = '+'
        else: m = '-'
        self.product_txt.delete(0.0, END)
        self.product_txt.insert(0.0, 'f(x) = ' + str(a) + ' *(x ' + m \
                                + ' ' + str(x_12d) + ')*(x'\
                                + m + str(x_12d) + ')')
    else:
        self.product_txt.delete(0.0, END)
        self.product_txt.insert(0.0, 'Postać iloczynowa równania nie istnieje')

def courseFunctionVariability(self,a,p):
    '''Opis przebiegu zmienności funkcji'''

    if a > 0: direct = 'do góry.'; direct_1 = 'malejąca'; direct_2 = 'rosnąca.'
    if a < 0: direct = 'w dół.'; direct_1 = 'rosnąca'; direct_2 = 'malejąca.'
    self.results_txt.delete(0.0, END)   #wpis w polu WYNIKI
    self.results_txt.insert(0.0, 'Funkcja ramionami skierowana jest ' + direct\
                            + '\nFunkcja w przedziale ( - ∞, x = ' + str(p) + ' >'\
                            + ' jest ' + direct_1 + '\nFunkcja w przedziale < x = ' \
                            + str(p) + ', + ∞ ) jest ' + direct_2)

def lineEquation(self,b,c):
    '''Równanie prostej - f(x) = bx + c'''

    self.cleanTextFrame()    #usunięcie wpisów z pól opisowych wyników obliczeń

    if b==0:
        #Prosta równoległa do osi OX')
        #i przechodząca przez punkt o współrzędnej y=',c)
        if c < 0: cl = -c; m = '-'; m0 = '-'
        elif c > 0: cl = c; m = '+'; m0 = '+'
        else: cl = c; m = '+'; m0 = ''

        #wypisanie opisu prostej w polu WYNIKI
        self.results_txt.insert(END, '\nPonieważ współczynniki równania '\
                                + 'a = 0 i b = 0 - jest równanie prostej ' \
                                + '- o postaci: \ny = ' + str(b) + ' x ' \
                                + m + ' ' + str(cl) + ' - równoległej do osi OX ' \
                                + 'i przechodzącej przez punkt o współrzędnej \n' \
                                + 'y = ' + m0 + ' ' + str(cl)+'  (c = ' + m0 + ' ' \
                                + str(cl)+ ')')

        #wygenerowanie wykresu prostej równoległej do osi OX
        plotLineHorizontal(self,b,c)

    #obliczenie kąta nachylenia prostej do osi OX
    else:
        x1=0.0; y1=c; y2=0.0; x2=round(-c/b,4)
        try:
            alfa = atan((y2-y1)/(x2-x1))
        except ZeroDivisionError:
        #prosta przechodzi przez poczatek układu x=0 i y=0
            alfa = atan(b) #obliczenie kąta nachylenia prostej do osi OX - w radianach

        #zamiana kąta nachylenia prostej do osi OX - z radianów na stopnie
        st_c_i, min_c_i, sek_i = radiansToDegrees(self,alfa)

        #Przypisanie wartości współrzędnych prostej do zmiennych tekstowych
        #w opisie prostej równoległej do osi OY 

        #zamiana formy wyświetlania znaków '0' - z '0' na 0.0'
        if min_c_i == 0: min_c_i = '00'
        if sek_i == 0:
            sek_i = '00'
            line_message_00 = '\nJest to prosta przechodząca przez punkt ' \
                              + 'o współrzędnych: x₁ = 0.0,  y₁ = 0.0,' \
                              + '\njest równoległa do osi OY (pokrywa się z osią OY) ' \
                              + "\ni nachylona do osi OX pod kątem:   90° 00'" + ' 00"'

        #Przypisanie wartości współrzędnych prostej do zmiennych tekstowych
        #w opisie prostej nierównoległej do osi OY 
        #alfa < 90 st
        x11 = x1; x21 = x2; y11 = y1; y21 = y2

        #alfa > 90 st
        if x2 < x1: x11 = x2; x21 = x1; y11 = y2; y21 = y1
        #prosta przechodząca przez początek układu współrzędnych x = 0 , y = 0
        if c == 0: x21 = '0.0'; y21 = '0.0'
            
        line_message_xx = '\nJest to prosta przechodząca przez punkt o współrzędnych: \nx₁ = ' \
                          + str(x11) + ',   y₁ = ' + str(y11) + ' ;   x₂ = ' +str(x21) \
                          + '   y₂ = ' + str(y21) + '\ni nachylona do osi OX pod kątem:   '\
                          + str(st_c_i) + '°  ' + str(min_c_i) + '\'  ' + str(sek_i) +'"'

        if st_c_i == 90 and min_c_i == '00' and sek_i == '00':
            line_message = line_message_00
        else:
            line_message = line_message_xx
        #wypisanie opisu prostej w polu WYNIKI
        self.results_txt.insert(END, line_message)
        #wygenerowanie wykresu prostej nachylonej do osi OX
        plotLine(self,b,c)
