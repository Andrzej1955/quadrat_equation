#RÓWNANIE KWADRATOWE OKIENKO 0.1 - wykresy

from math import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *


def plotPoint(self):
    '''Wykres - punkt położny na początku układu wsółrzęnych - x - 0, y = 0'''
    fig, ax = plt.subplots(figsize=(9, 4.5))
    #ustalenie parametrów zakresu osi wykresu
            
    ax.axis([-8, 8, -3, 3])
    #rysunek punktun na początku układu wsółrzęnych - x - 0, y = 0
    ax.plot([0], [0], 'o')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    fig.savefig('fig_1.png', dpi=72)
    graph(self)

def plotLineHorizontal(self,b,c):
    '''Wykres prostej przechodzącej przez punkt y = c - równoległej do osi OX'''

    x = np.arange(-8,+9,1) # lista argumentów x
    y = []
    y = [c for i in x]

    fig, ax = plt.subplots(figsize=(9, 4.5))

    #ustalenie parametrów zakresu osi wykresu
    if c > 0: yu = c+3; yd = -3
    elif c < 0: yu = 3; yd = c-3
    else: yu = 3; yd = -3
    
    ax.axis([-8, 8, yd, yu])

    plt.plot(x, y)
    plt.title('Wykres f(x) = b*x + c')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    fig.savefig('fig_1.png', dpi=72)
    graph(self)

def plotLine(self,b,c):
    '''Wykres prostej przechodzącej przez punkt x=0, y=0'''
    y1 = np.arange(c-12,c+13,1) # lista argumentów x
    x = []  # lista wartości
    y = []
    x = [(i-c)/b for i in y1]
    y = [(float(i)) for i in y1]
    
    fig, ax = plt.subplots(figsize=(9, 4.5))

    #ustalenie parametrów zakresu osi wykresu
    if c > 0: yu = c+6; yd = -6; xu = c+12; xd = -12
    elif c < 0: yu = 6; yd = c-6; xu = c+12; xd = -12
    else: yu = 6; yd = -6; xu = c+12; xd = -12

    ax.axis([xd, xu, yd, yu])

    #ustalenie elementów treści tytułu wykresu
    if b < 0: b = -b; n = '- '; r = '*'
    else: n = ''; r = '*'
    if fabs(b) == 1: b = ''; r = ''
    if b == 0: b = ''; n = ''

    if c < 0: c = -c; o = '- '
    else: o = '+ '
    if c == 0: o = ''; c = ''

    plt.plot(x, y)
    plt.title('Wykres f(x) = ' + n + str(b) + r +' x ' + o + str(c))
    plt.grid(True)
    plt.xlabel('oś x')
    plt.ylabel('oś y')
    fig.savefig('fig_1.png', dpi=72)
    graph(self)

def plotQuadraticFunc(self,a,b,c,p,q):
    '''Wykres funkcji "f(x) = ax²+bx+c" '''
    x_1 = p -20
    x_2 = p +21
    x = np.arange(x_1, x_2, 0.05) # lista argumentów x
    y = []
    y = [a*i*i+b*i+c for i in x]

    q0 = a
    q1 = q

    #ustalenie elementów treści tytułu wykresu
    if a < 0: a = -a; m = '- '
    else: m = '+ '

    if fabs(a) == 1: a = ''

    if b < 0: b = -b; n = '- '
    else: n = '+ '

    if fabs(b) == 1: b = ''

    if c < 0: c = -c; o = '- '
    else: o = '+ '

    fig, ax = plt.subplots(1,2, figsize=(9, 4.5))
    
    #ustalenie parametrów zakresu osi wykresu
    if q0 > 0: xu = 140; xd = - 40
    else: xu = 40; xd = -140

    if q0 > 0: x1u = 12; x1d = - 2
    else: x1u = 2; x1d = -12

    ax[0].axis([p - 65, p + 65, q1 + xd, q1 + xu])
    ax[1].axis([p - 5.5, p + 5.5, q1 + x1d, q1 + x1u])

    #parametry wykresu funkcji
    ax[0].plot(x, y, color='green', linewidth=1, alpha=1.0)
    #parametry tytułu wykresu funkcji
    title_0 = ('Wykres f(x) = ' + str(m)  + str(a) + ' x² ' + str(n) + str(b) + ' x '\
               + str(o) + str(c) + '\n dla x∈ <'+ str(x_1) + ' ; ' + str(x_2-1) +  '>')
    #parametry siatki wykresu funkcji
    ax[0].grid(True)

    #parametry wykresu funkcji
    ax[1].plot(x, y, color='blue', linewidth=1, alpha=1.0)
    #parametry siatki wykresu funkcji
    ax[1].grid(True)
    #ustalenie parametrów i treści tekstu na wykresie
    t = 'Wierzchołek\nfunkcji' + '\nx = ' + str(p) +'\ny = ' + str(q)
    ax[0].text(p - 55, q-10, t, style='italic', color='red', fontsize=7,
               bbox={'facecolor': 'white', 'alpha': 0.8, 'pad': 5})
    ax[0].set_xlabel('oś x', color='green', fontsize=6)
    ax[0].set_ylabel('oś y', color='green', fontsize=6)
    ax[1].set_xlabel('oś x', color='blue', fontsize=6)
    ax[1].set_ylabel('oś y', color='blue', fontsize=6)

    #parametry tytułu wykresu funkcji

    fig.suptitle(title_0, color='green', fontsize=9)
    fig.savefig('fig_1.png', dpi=72)
    graph(self)

def graph(self):
    # wstawienie obrazu wykresu do etykiety
    wzor = PhotoImage (file = "fig_1.png")
    self.obraz_6 = Label(self, image = wzor)
    self.obraz_6.image = wzor
    self.obraz_6.grid(row = 28, rowspan = 30, column = 1, columnspan = 20)




