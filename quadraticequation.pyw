#RÓWNANIE KWADRATOWE OKIENKO 0.1 - validate - modulo
from tkinter import *
from math import *

from rkplot import *
from rkraddegr import *
from rkequatios import *
from rkdeltaroots import *
first = 0
last = 7 


#==============================================================================
#POCZĄTEK OKNA
class Application(Frame):
    """ Aplikacja z GUI, która oblicza parametry równania kweadratowego. """
    def __init__(self, master):

        """ Inicjalizuj ramkę. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()
        self.master.geometry('+350+15')

    def create_widgets(self):
        """
        Utwórz widżety potrzebne do pobrania informacji podanych przez
        użytkownika i wyświetlenia wyniku.
        """
        # etykieta z tytułem
        self.title_lbl = Label(self, font = ('calibri', 11),
              text =
'"RÓWNANIE KWADRATOWE"\n\
Podaj współczynniki równania kwadratowego\n \
      "a,  b,  c"    lub    "a,  p,  q"    lub    "a,  x₁,  x₂".\n'
              ).grid(row = 0, column = 1, columnspan = 25)

        # etykieta z obrazem LOGO PYTHON
        logo = PhotoImage (file = "logo.gif")
        self.obraz = Label(self, image = logo)
        self.obraz.image = logo
        self.obraz.grid(row = 0, column = 0, sticky = N)

#==============================================================================
        #a b c 
        #wiersz pobrania współczynników postaci ogółnej - a, b, c
        #etykieta i pole znakowe służące do wpisania współczynnika 'a'

        self.lbl = Label(self, font = ('calibri', 11),
                               text = 'a', foreground = 'blue'
                               ).grid(row = 2, column = 2)

        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'b', foreground = 'blue'
                         ).grid(row = 2, column = 4)

        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'c', foreground = 'blue'
                         ).grid(row = 2, column = 6)


        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'f(x) = '
                         ).grid(row = 3, column = 1)

        sv = StringVar()
        self.ag = Entry(self,
                        width = 8,
                        justify = CENTER,
                        font = ('calibri', 11),
                        foreground = 'blue',
                        textvariable = sv
                        )
        self.ag.grid(row = 3, column = 2)     
        sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var)) #walidacja wprowadzanych danych

        self.lbl = Label(self, font = ('calibri', 11), 
                         text = 'x²  +'
                         ).grid(row = 3, column = 3, sticky = W)

        # etykieta i pole znakowe służące do wpisania współczynnika 'b'
        sv = StringVar()
        self.b = Entry(self,
                       width = 8,
                       justify = CENTER,
                       font = ('calibri', 11),
                       foreground = 'blue',
                       textvariable = sv
                       )
        self.b.grid(row = 3, column = 4)
        sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var)) #walidacja wprowadzanych danych

        self.lbl = Label(self, font = ('calibri', 11),
              text = 'x   +'
              ).grid(row = 3, column = 5, sticky = W)

        # etykieta i pole znakowe służące do wpisania współczynnika 'c'
        sv = StringVar()
        self.c = Entry(self,
                       width = 8,
                       justify = CENTER,
                       font = ('calibri', 11),
                       foreground = 'blue',
                       textvariable = sv
                       )
        self.c.grid(row = 3, column = 6)
        sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var)) #walidacja wprowadzanych danych


        # utwórz przycisk - Przycisk 'OK' - oblicz równanie
        self.wykonaj = Button(self,
                              text = 'Oblicz',
                              font = ('calibri',11),
                              padx = 130,
                              state = 'active'
                              )
        self.wykonaj.bind("<Return>",self.generalFormGetFactor) #uruchonminie działania klawisza enter
        self.wykonaj.bind("<Button>",self.generalFormGetFactor) #uruchonminie działania lewego przycisku myszy
        self.wykonaj.grid(row = 4, column = 1,columnspan = 6)	

#==============================================================================
        #a p q
        #wiersz pobrania współczynników postaci kanonicznej - a, p, q
        # etykieta i pole znakowe służące do wpisania współczynnika 'a'
        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'a', foreground = 'blue'
                         ).grid(row = 2, column = 9)
        
        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'p', foreground = 'blue'
                         ).grid(row = 2, column = 11)

        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'q', foreground = 'blue'
                         ).grid(row = 2, column = 13)

        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'f(x) = '
                         ).grid(row = 3, column = 8)

        sv = StringVar()
        self.ac = Entry(self,
                        width = 8,
                        justify = CENTER,
                        font = ('calibri', 11),
                        foreground = 'blue',
                        textvariable = sv
                        )
        self.ac.grid(row = 3, column = 9)
        sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var)) #walidacja wprowadzanych danych

        self.lbl = Label(self, font = ('calibri', 11),
                         text = '* (x -'
                         ).grid(row = 3, column = 10, sticky = W)

        # etykieta i pole znakowe służące do wpisania współczynnika 'p'
        sv = StringVar()
        self.p = Entry(self,
                       width = 8,
                       justify = CENTER,
                       font = ('calibri', 11),
                       foreground = 'blue',
                       textvariable = sv
                       )
        self.p.grid(row = 3, column = 11)
        sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var)) #walidacja wprowadzanych danych

        self.lbl = Label(self, font = ('calibri', 11),
                         text = ')²  +  '
                         ).grid(row = 3, column = 12, sticky = W)

        # etykieta i pole znakowe służące do wpisania współczynnika 'q'
        sv = StringVar()
        self.q = Entry(self,
                       width = 8,
                       justify = CENTER,
                       font = ('calibri', 11),
                       foreground = 'blue',
                       textvariable = sv
                       )
        self.q.grid(row = 3, column = 13)
        sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var)) #walidacja wprowadzanych danych

        # utwórz przycisk - Przycisk 'OK' - oblicz równanie
        self.wykonaj = Button(self,
                              text = "Oblicz",
                              font = ('calibri',11),
                              padx = 130
                              )
        self.wykonaj.grid(row = 4, column = 8, columnspan = 6)
        self.wykonaj.bind("<Return>",self.canonicalFormGetFactor)  #uruchonminie działania klawisza enter
        self.wykonaj.bind("<Button>",self.canonicalFormGetFactor)  #uruchonminie działania lewego przycisku myszy

#==============================================================================
        #a x1 x2
        #wiersz pobrania współczynników postaci ilo zynowej - a, x1, x2
        # etykieta i pole znakowe służące do wpisania współczynnika 'a'
        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'a', foreground = 'blue'
                         ).grid(row = 2, column = 16)

        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'x₁', foreground = 'blue'
                         ).grid(row = 2, column = 18)

        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'x₂', foreground = 'blue'
                         ).grid(row = 2, column = 20)

        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'f(x) = '
                         ).grid(row = 3, column = 15)

        sv = StringVar()
        self.ap = Entry(self,
                        width = 8,
                        justify = CENTER,
                        font = ('calibri', 11),
                        foreground = 'blue',
                        textvariable = sv
                        )
        self.ap.grid(row = 3, column = 16)
        sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var)) #walidacja wprowadzanych danych

        self.lbl = Label(self, font = ('calibri', 11),
                         text = '* (x -'
                         ).grid(row = 3, column = 17, sticky = W)

        # etykieta i pole znakowe służące do wpisania współczynnika 'x1'
        sv = StringVar()
        self.x1p = Entry(self,
                         width = 8,
                         justify = CENTER,
                         font = ('calibri', 11),
                         foreground = 'blue',
                         textvariable = sv
                         )
        self.x1p.grid(row = 3, column = 18)
        sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var)) #walidacja wprowadzanych danych

        self.lbl = Label(self, font = ('calibri', 11),
                         text = ') * (x -'
                         ).grid(row = 3, column = 19, sticky = W)

        # etykieta i pole znakowe służące do wpisania współczynnika 'x2'
        sv = StringVar()
        self.x2p = Entry(self,
                         width = 8,
                         justify = CENTER,
                         font = ('calibri', 11),
                         foreground = 'blue',
                         textvariable = sv
                         )
        self.x2p.grid(row = 3, column = 20)
        sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var)) #walidacja wprowadzanych danych

        self.lbl = Label(self, font = ('calibri', 11),
              text = ')'
              ).grid(row = 3, column = 21, sticky = W)

        # utwórz przycisk - Przycisk 'OK' - oblicz równanie
        self.wykonaj = Button(self,
                              text = "Oblicz",
                              font = ('calibri',11),
                              padx = 130
                              )
        self.wykonaj.grid(row = 4, column = 15, columnspan=7)
        self.wykonaj.bind("<Return>",self.productFormGetFactor)
        self.wykonaj.bind("<Button>",self.productFormGetFactor)

#==============================================================================
        # etykieta z widokiem do wyświetlenia informacji o wpisanych błędnie liczbach
        self.inst_lbl = Label(self, font = ('calibri', 14),
                              text = "     UWAGI     ",
                              height = 2,
                              background = 'yellow',
                              foreground = 'red',
                              justify = 'right',
                              relief = 'ridge',
                              bd = 4
                              ).grid(row = 5, column = 3, columnspan = 3)

       # widżet Text do wyświetlenia informacji o wpisanych liczbach
        self.comment_txt = Text(self,
                                width = 82,
                                height = 3,
                                font = ('calibri', 11),
                                background ="yellow",
                                foreground = 'red',
                                bd = 4,
                                relief = 'ridge',
                                wrap = WORD,
                                padx = 5,
                                pady = 5)
        self.comment_txt.grid(row = 5, column = 6, columnspan = 21, sticky = W)

#==============================================================================
        #DELTA
        # etykieta z widokiem delty
        self.lbl = Label(self, font = ('calibri', 11),
                         text = "Delta:",
                         justify='left',
                         ).grid(row = 6, column = 1, columnspan = 3, sticky = W)
        
       # widżet Text do wyświetlenia wyniku delty
        self.delta_txt = Text(self, width = 25, height = 1, font = ('calibri', 11))
        self.delta_txt.grid(row = 6, column = 6, columnspan=4, sticky = W)

        # etykieta z obrazem wzoru delta
        wzor = PhotoImage (file = "wzory_delta.gif")
        self.obraz_6 = Label(self, image = wzor)
        self.obraz_6.image = wzor
        self.obraz_6.grid(row = 7, column = 2, columnspan = 2)

#==============================================================================
        #PIERWIASTKI
        # etykieta z widokiem pierwiastków równania
        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'Pierwiastki równania \n(miejsca zerowe):  ',
                         justify='left',
                         height=2
                         ).grid(row = 9, column = 1, columnspan=5,  sticky = W)
        
       # widżet Text do wyświetlenia wartości pierwiastków równania
        self.zero_place_txt = Text(self, width = 25, height = 2, font = ('calibri', 11))
        self.zero_place_txt.grid(row = 9, column = 6, columnspan=4, sticky = W)
     
        # etykieta z obrazem wzorów pierwiastków x1, x2 i wspólnego x1=x2
        wzor = PhotoImage (file = "wzory_x1_x2_x12.gif")
        self.obraz_1 = Label(self, image = wzor)
        self.obraz_1.image = wzor
        self.obraz_1.grid(row = 10, column = 1, columnspan=3, sticky = W)

#==============================================================================
        #WIERZCHOŁEK
        # etykieta z widokiem współrzednych wierzchołka funkcji
        self.lbl = Label(self, font = ('calibri', 11),
                         text = 'Współrzędne wierzchołka \nfunkcji:  ',
                         justify='left',
                         height=2,
                         ).grid(row = 14, column = 1, columnspan=4,  sticky = W)
        
       # idżet Text do wyświetlenia współrzednych wierzchołka funkcji
        self.function_vertex_txt = Text(self, width = 25, height = 2, font = ('calibri', 11))
        self.function_vertex_txt.grid(row = 14, column = 6, columnspan = 4, sticky = W)

        # etykieta z obrazem wzorów p i q
        wzor = PhotoImage (file = 'wzory_p_q.gif')
        self.obraz_4 = Label(self, image = wzor)
        self.obraz_4.image = wzor
        self.obraz_4.grid(row = 15, column = 1, columnspan=4, sticky = W)

#==============================================================================
        # etykieta z pustą linią ' '
        self.linia = Label(self, font = ('calibri', 11),
                           text = "\n",
                           height =1
                           ).grid(row = 16, column = 1)

#==============================================================================
        # etykieta z widokiem postaci ogólnej równania
        self.lbl = Label(self, font = ('calibri', 11),
                              text = "Postać ogólna:  ", justify='left',
                              ).grid(row = 6, column = 11, columnspan=20,  sticky = W)
        
       # utwórz widżet Text do wyświetlenia postaci kanonicznej równania
        self.general_txt = Text(self, width = 45, height = 1)
        self.general_txt.grid(row = 6, column = 14, columnspan=14, sticky = W)

        # etykieta z widokiem postaci kanonicznej równania
        self.lbl = Label(self, font = ('calibri', 11),
                              text = "Postać kanoniczna:  ", justify='left',
                              ).grid(row = 7, column = 11, columnspan=20,  sticky = W)
        
       # utwórz widżet Text do wyświetlenia postaci kanonicznej równania
        self.canon_txt = Text(self, width = 45, height = 1)
        self.canon_txt.grid(row = 7, column = 14, columnspan=14, sticky = W)
        
        # etykieta z widokiem postaci iloczynowej równania
        self.inst_lbl = Label(self, font = ('calibri', 11),
                              text = "Postać iloczynowa:  ",
                              justify='left'
                              ).grid(row = 8, column = 11, columnspan=20,  sticky = W)
        
       # utwórz widżet Text do wyświetlenia wartości pierwiastków równania
        self.product_txt = Text(self, width = 45, height = 1)
        self.product_txt.grid(row = 8, column = 14, columnspan=14, sticky = W)#  

#==============================================================================
        # etykieta z widokiem do wyświetlenia informacji o przebiegu funkcji - góra/dół
        self.lbl = Label(self, font = ('calibri', 11),
                                       text = "WYNIKI                           ",
                                       ).grid(row = 10, column = 11, columnspan = 20, sticky = N)
       # widżet Text do wyświetlenia informacji o wikach obliczeń
        self.results_txt = Text(self,
                                width = 74,
                                height = 7,
                                font = ('calibri', 11),
                                wrap = WORD,
                                padx = 5,
                                pady = 5)
        self.results_txt.grid(row = 10, column = 11, rowspan = 7, columnspan = 20, sticky = W)

#==============================================================================
        # etykieta z pustą linią '0' -'' - lewa ramka - kolumna '0'
        self.linia = Label(self, font = ('CourieNew', 11),
              text = "            "
              ).grid(row = 70, column = 0)
        # etykieta z pustą kolumną '2' '' - środkowa kolumna '7'
        self.linia = Label(self, font = ('CourieNew', 11),
              text = "            "
              ).grid(row = 70, column = 7)
        # etykieta z pustą kolumną '3' '' - środkowa kolumna '14'
        self.linia = Label(self, font = ('CourieNew', 11),
              text = "            "
              ).grid(row = 70, column = 14)
        # etykieta z pustą kolumną '3' '' - prawa ramka - kolumna '22'
        self.linia = Label(self, font = ('CourieNew', 11),
              text = "            "
              ).grid(row = 70, column = 24)
        # etykieta z z pustą linią nad przyciskiem QUIT
        self.linia = Label(self, font = ('CourierNew', 11),
                           text = " ",
                           height = 1,
                           ).grid(row = 69, column = 1)

#==============================================================================
        #przycisk zamknięcia okna - zakończnenia aplikacji
        self.koniec_ost = Button(self,
                                 text = "(:   QUIT   :)",
                                 font = ('calibri',13),
                                 padx = 135,
                                 pady = 10,
                                 command = root.destroy)
        self.koniec_ost.grid(row = 70, column = 1,columnspan = 20)

#==============================================================================
        # etykieta z pustą linią pod przyciskiem QUIT
        self.linia = Label(self, font = ('CourierNew', 11),
                           text = " ",
                           height = 1,
                           ).grid(row = 71, column = 1)

#==============================================================================
    #Sprawdzenie poprawności wprowadzenia liczby zmiennoprzecinkowej
    def validate_float(self,var):
        '''
        Sprawdzenie poprawności wprowadzenia liczby zmiennoprzecinkowej
        w polu "Entry":
            sv = StringVar()
            self.ac = Entry(self, .... , textvariable = sv)
          self.ac.grid(row = 3, column = 9)
          sv.trace('w', lambda nm, idx, mode, var=sv: self.validate_float(var))
        '''
        validate_old_value = ''
        new_value = var.get()
        try:
            new_value == '-' or new_value == '-.' or new_value == '.' \
                      or new_value == '' or new_value == float(new_value) 
            validate_old_value = new_value
        except:
            var.set(validate_old_value)    

#==============================================================================
         
    def generalFormGetFactor(self,Button):
        '''Pobieranie współczynników a, b, c równania kwadratowego - postać ogólna''' 

        self.comment_txt.delete(0.0, END)   #usunięcie wpisów z pola UWAGI 

        #walidacja współczynnika 'a'
        try: a = float(self.ag.get())
        except: self.comment_txt.insert(0.0, 'Ponieważ nie wpisano żadnej liczby' \
                ' przyjęto współczynnik a = 0'); a = 0

        #walidacja współczynnika 'b'
        try: b = float(self.b.get())
        except: self.comment_txt.insert(END, '\nPonieważ nie wpisano żadnej liczby' \
                ' przyjęto współczynnik b = 0'); b = 0

        #walidacja współczynnika 'c'
        try: c = float(self.c.get())
        except: self.comment_txt.insert(END, '\nPonieważ nie wpisano żadnej liczby' \
                ' przyjęto współczynnik c = 0'); c = 0

        self.cleanEntryCanonForm()   #usunięcie wpisów z pól pobierania współczynników postaci kanonicznej równania
        self.cleanEntryProductForm() #usunięcie wpisów z pól pobierania współczynników postaci iloczynowej równania
        self.cleanTextFrame()        #usunięcie wpisów z pól opisowych wyników obliczeń

        #Ustalenie formy równania: kwadratowe czy inne
        generalFormGetFactor_abc(self,a,b,c)


    def canonicalFormGetFactor(self,Button):
        '''Pobieranie współczynników a, p, q równania kwadratowego - postać kanoniczna''' 
        '''Obliczenie współczynników b i c z postaci kanonicznej równania'''

        self.comment_txt.delete(0.0, END)   #usunięcie wpisów z pola UWAGI 

        #walidacja współczynnika 'a'
        try: ac = float(self.ac.get())
        except: self.comment_txt.insert(END, 'Ponieważ nie wpisano żadnej liczby' \
                ' przyjęto współczynnik a = 0'); ac = 0

        #walidacja współczynnika 'p'
        try: p = float(self.p.get())
        except: self.comment_txt.insert(END, '\nPonieważ nie wpisano żadnej liczby' \
                ' przyjęto współczynnik p = 0'); p = 0

        #walidacja współczynnika 'q'
        try: q = float(self.q.get())
        except: self.comment_txt.insert(END, '\nPonieważ nie wpisano żadnej liczby' \
               ' przyjęto współczynnik q = 0'); q = 0

        self.cleanEntryGeneralForm() #usunięcie wpisów z pól pobierania współczynników postaci ogólnej równania
        self.cleanEntryProductForm() #usunięcie wpisów z pól pobierania współczynników postaci iloczynowej równania
        self.cleanTextFrame()        #usunięcie wpisów z pól opisowych wyników obliczeń

        #Obliczenie współczynników "b,c" z "p,q" postaci kanonicznej równania
        canonicalFormGetFactor_abc(self,ac,p,q)

  
    def productFormGetFactor(self,Button):
        '''Pobieranie współczynników a, x₁, x₂ równania kwadratowego - postać iloczynowa''' 
#        '''Obliczenie współczynników b i c z postaci iloczynowej równania'''

        self.comment_txt.delete(0.0, END)   #usunięcie wpisów z pola UWAGI 

        #walidacja współczynnika 'ap'
        try: ap = float(self.ap.get())
        except: self.comment_txt.insert(END, 'Ponieważ nie wpisano żadnej liczby' \
                ' przyjęto współczynnik a = 0'); ap = 0

        #walidacja współczynnika 'x1p'
        try: x1p = float(self.x1p.get())
        except: self.comment_txt.insert(END, '\nPonieważ nie wpisano żadnej liczby' \
                ' przyjęto współczynnik x₁ = 0'); x1p = 0

        #walidacja współczynnika 'x2p'
        try: x2p = float(self.x2p.get())
        except: self.comment_txt.insert(END, '\nPonieważ nie wpisano żadnej liczby' \
                ' przyjęto współczynnik x₂ = 0'); x2p = 0

        self.cleanEntryGeneralForm() #usunięcie wpisów z pól pobierania współczynników postaci ogólnej równania
        self.cleanEntryCanonForm()   #usunięcie wpisów z pól pobierania współczynników postaci kanonicznej równania
        self.cleanTextFrame()        #usunięcie wpisów z pól opisowych wyników obliczeń
        
        #Obliczenie współczynników  "b,c" z "x1p,x2p" postaci iloczynowej równania
        productFormGetFactor_abc(self,ap,x1p,x2p)


    def cleanEntryGeneralForm(self):
        '''Usuwanie znaków z pól Entry postaci ogólnej równania - a, b, c '''
        self.ag.delete(first,last)
        self.b.delete(first,last)
        self.c.delete(first,last)

    def cleanEntryCanonForm(self):
        '''Usuwanie znaków z pól Entry postaci kanonicznej równania - a, p, q '''
        self.ac.delete(first,last)
        self.p.delete(first,last)
        self.q.delete(first,last)

    def cleanEntryProductForm(self):
        '''Usuwanie znaków z pól Entry postaci iloczynowej równania - a, x1, x2 '''
        self.ap.delete(first,last)
        self.x1p.delete(first,last)
        self.x2p.delete(first,last)

    def cleanTextFrame(self):
        '''Usuwanie znaków z pól tekstowych '''
        self.delta_txt.delete(0.0, END)
        self.zero_place_txt.delete(0.0, END)
        self.general_txt.delete(0.0, END)
        self.canon_txt.delete(0.0, END)
        self.product_txt.delete(0.0, END)
        self.function_vertex_txt.delete(0.0, END)

#==============================================================================

# część główna
root = Tk()
root.title('RÓWNANIE KWADRATOWE')
app = Application(root)
root.mainloop()
