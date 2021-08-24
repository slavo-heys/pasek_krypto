# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 11:39:42 2021

@author: ilodz
"""

import requests
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3



class Program:
    def __init__(self):
        self.window = tk.Tk()
        
        self.add_baza_sql() # wywołanie funkcji tworzenia sql
        
    # %% czcionka
        self.krojCzcionki = "Comic Sans"  # Times New Roman, Tahoma, Comic Sans
        self.rozmiarCzcionki = 12
        
# %% definiowanie kolorów
        self.red = "#FF4500"
        self.green = "#00FF00"
        self.white = "white"
        self.black = "black"
        self.jNiebieski = "skyblue"
        
# %% definiowanie zmiennych
        self.dlugosc = tk.StringVar()
        self.szerokosc = tk.StringVar()
        self.polozenie_x = tk.StringVar()
        self.polozenie_y = tk.StringVar()
        self.geo = tk.StringVar()
        self.dlugOkna = tk.StringVar()
        self.szerOkna = tk.StringVar()
        self.poloX = tk.StringVar()
        self.poloY = tk.StringVar()
        self.geoOkna = tk.StringVar()
        self.jakaGielda= tk.StringVar()
        self.jakieOkno = tk.StringVar()
        self.jakaWalutaBinance = tk.StringVar()
        
        self.dic = dict()
        self.list = []
        
# Otwarcie i wybór okna okna
        conn = sqlite3.connect('program.db')
        c = conn.cursor()
        c.execute("SELECT * FROM geometria ORDER BY id DESC LIMIT 1")
        wynik = c.fetchall()
        for row in wynik:
            self.dlugosc.set(row[1])
            self.szerokosc.set(row[2])
            self.polozenie_x.set(row[3])
            self.polozenie_y.set(row[4])
            self.geo.set(row[5])
                        
        c.close()
        
        self.dlugOkna = self.dlugosc.get()
        self.szerOkna = self.szerokosc.get()
        self.poloX = self.polozenie_x.get()
        self.poloY = self.polozenie_y.get()
        self.geoOkna = self.geo.get()
        
        if self.geoOkna == "left_up":
            self.geometry = self.dlugOkna+"x"+self.szerOkna+"+"+self.poloX+"+"+self.poloY
            self.window.geometry(self.geometry)
            self.window.configure(background="black")
            self.window.overrideredirect(1) # wyłączenie nagłówka w oknie
        elif self.geoOkna == "right_up":
            self.geometry = self.dlugOkna+"x"+self.szerOkna+"+"+self.poloX+"+"+self.poloY
            self.window.geometry(self.geometry)
            self.window.configure(background="black")
            self.window.overrideredirect(1) # wyłączenie nagłówka w oknie
        elif self.geoOkna == "left_down":
            self.geometry = self.dlugOkna+"x"+self.szerOkna+"+"+self.poloX+"+"+self.poloY
            self.window.geometry(self.geometry)
            self.window.configure(background="black")
            self.window.overrideredirect(1) # wyłączenie nagłówka w oknie
        elif self.geoOkna == "right_down":
            self.geometry = self.dlugOkna+"x"+self.szerOkna+"+"+self.poloX+"+"+self.poloY
            self.window.geometry(self.geometry)
            self.window.configure(background="black")
            self.window.overrideredirect(1) # wyłączenie nagłówka w oknie
        else:
            self.geometry = self.dlugOkna+"x"+self.szerOkna+"+"+self.poloX+"+"+self.poloY
            self.window.geometry(self.geometry)
            self.window.configure(background="black")
            self.window.overrideredirect(1) # wyłączenie nagłówka w oknie
            
        
# %% otworzenie ramki programu
        self.rama = tk.LabelFrame(self.window, padx=5, pady=5)
        self.rama.configure(background="black")
        self.rama.pack(fill="both", expand="yes")
        
        # przyciski okna
        self.button_ustawienia = tk.Button(self.rama, text = "USTAWIENIA")
        self.button_ustawienia.configure(font = ("Arial", 7), bg = "silver", fg = "black")
        self.button_ustawienia.configure(command = self.setting)
        self.button_ustawienia.place(x= 280, y = 0)
        
        self.button_exit = tk.Button(self.rama, text = "EXIT")
        self.button_exit.configure(font = ("Arial", 7), bg = "silver", fg = "red")
        self.button_exit.configure(command = self.exit_program)
        self.button_exit.place(x = 350, y = 0)
        # symbol ceny
        self.linia_symbol = tk.Label(self.rama, bg = "black", fg = "skyblue")
        self.linia_symbol.configure(text = "BTC-USD", font = ("Arial", 5))
        self.linia_symbol.place(x = 0, y = 0)
        # oznaczenie giełdy
        self.linia_gielda = tk.Label(self.rama, bg = "black", fg = "gold")
        self.linia_gielda.configure(text = "BINANCE", font = ("Arial", 5))
        self.linia_gielda.place(x = 0, y = 9)
        # oznaczenie bid
        self.linia_bid = tk.Label(self.rama, bg = "black", fg = "skyblue")
        self.linia_bid.configure(text = "BID", font = ("Arial", 7))
        self.linia_bid.place(x = 50, y = 3)
         # oznaczenia ask
        self.linia_ask = tk.Label(self.rama, bg = "black", fg = "skyblue")
        self.linia_ask.configure(text = "ASK", font = ("Arial", 7))
        self.linia_ask.place(x = 165, y = 3)
        
        
# %%
        self.window.mainloop()
        
# %% definicje programu
    def add_baza_sql(self):
        conn = sqlite3.connect('program.db')
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS geometria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dlugosc text NOT NULL,
            szerokosc text NOT NULL,
            polozenie_x text NOT NULL,
            polozenie_y text NOT NULL,
            geo text NOT NULL
            );""")
        conn.commit()
        conn.close()
        
        conn = sqlite3.connect('program.db')
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS pary(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            para text NOT NULL
            );"""
        )
        conn.commit()
        conn.close()
        
        conn = sqlite3.connect('program.db')
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS gielda(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            n_gieldy text NOT NULL
            );"""
        )
        conn.commit()
        conn.close()
        
        # spradzanie czy baza jest pusta
        conn = sqlite3.connect('program.db')
        c = conn.cursor()
        c.execute("Select count(id) From geometria")
        self.wynik = c.fetchone()[0]
        c.close()

        # Jeśli rekord nie istnieje dodaj
        if self.wynik == 0:
            conn = sqlite3.connect('program.db')
            c = conn.cursor()
            c.execute("INSERT INTO geometria VALUES(NULL, :dlugosc, :szerokosc, :polozenie_x, :polozenie_y, :geo)",
                      {
                          'dlugosc': 390,
                          'szerokosc': 35,
                          'polozenie_x': 1,
                          'polozenie_y': 2,
                          'geo': "left_up"
                      })
            conn.commit()
            conn.close()
            
            conn = sqlite3.connect('program.db')
            c = conn.cursor()
            c.execute("INSERT INTO pary VALUES(NULL, :para)",
                      {
                          'para': "BTCUSD"
                      })
            conn.commit()
            conn.close()
            
            conn = sqlite3.connect('program.db')
            c = conn.cursor()
            c.execute("INSERT INTO gielda VALUES(NULL, :n_gieldy)",
                      {
                          'n_gieldy': "BINANCE"
                      })
            conn.commit()
            conn.close()

    def exit_program(self):
        self.window.destroy()
        
    def setting(self):
        self.top = tk.Toplevel()
        self.top.geometry("520x300+100+100")
        self.top.configure(background="black")
        self.top.title("Setting")
        
        self.linia_1 = tk.Label(self.top, text = "Wybież położenie okna:")
        self.linia_1.configure(font = (self.krojCzcionki, self.rozmiarCzcionki), bg = self.black, fg = self.jNiebieski)
        self.linia_1.place(x = 10, y = 11)
        
        
        
        self.combo = ttk.Combobox(self.top, textvariable = self.jakieOkno)
        self.combo['values'] = ('lewy górny róg',
                                'prawy górny róg',
                                'dolny lewy róg',
                                'dolny prawy róg',
                                'centralnie srodek')
        self.combo.current(0)
        #self.combobox.bind("<<ComboboxSelected>>", self.zapisz ustawienia)
        self.combo.place(x = 200, y = 12)
        
        #self.button_zapisz = tk.Button(self.top, text = "zapisz ustawienia")
        #self.button_zapisz.configure(command = self.zapisz_ustawienia)
        #self.button_zapisz.place(x = 400, y = 11)
        
        self.linia_2 = tk.Label(self.top, text = "Wybierz giełdę:")
        self.linia_2.configure(font = (self.krojCzcionki, self.rozmiarCzcionki), bg = self.black, fg = self.jNiebieski)
        self.linia_2.place(x= 10, y = 40)
        
        
        
        self.com = ttk.Combobox(self.top, textvariable = self.jakaGielda)
        self.com['values'] = ('BINANCE',
                              'BITBAY')
        self.com.current(0)
        self.com.place(x= 200, y = 42)
        
        self.linia_3 = tk.Label(self.top, text = "Wybież kryptowalutę:")
        self.linia_3.configure(font = (self.krojCzcionki, self.rozmiarCzcionki), bg = self.black, fg = self.jNiebieski)
        self.linia_3.place(x = 10, y = 72)
        
        

        self.readBinance = requests.get("https://fapi.binance.com/fapi/v1/ticker/bookTicker")
        self.taskBinance = self.readBinance.json()
        self.dic = (self.taskBinance)
        
        self.yBinance = len(self.dic)


        for x in range(0, self.yBinance):
            self.idBinance = (x)
            self.symbolBinance = self.dic[x]["symbol"]
            
            self.danaBinance = [self.idBinance,self.symbolBinance]
            self.list.append(self.danaBinance)
            
        
            
        self.combo3 = ttk.Combobox(self.top, textvariable = self.jakaWalutaBinance)
        self.combo3['values'] = (self.list)
        self.combo3.current(0)
        self.combo3.place(x= 200, y = 73)
        
        self.buttonZapisz = tk.Button(self.top, text = "zapisz ustawienia")
        self.buttonZapisz.configure(command = self.zapisz_ustawienia)
        self.buttonZapisz.place(x = 400, y = 71)
            
        
                                   
        #self.top.mainloop() 
        
        
    def zapisz_ustawienia(self):
        self.wynikOkno = self.jakieOkno.get()
        self.wynikGielda = self.jakaGielda.get()
        self.wynikWaluta = self.jakaWalutaBinance.get()
        
        if self.wynikOkno == 'lewy górny róg':
            conn = sqlite3.connect('program.db')
            c = conn.cursor()
            c.execute("INSERT INTO geometria VALUES(NULL, :dlugosc, :szerokosc, :polozenie_x, :polozenie_y, :geo)",
                      {
                          'dlugosc': 390,
                          'szerokosc': 35,
                          'polozenie_x': 1,
                          'polozenie_y': 2,
                          'geo': "left_up"
                      })
            conn.commit()
            conn.close()
            
            self.buttonZapisz.destroy()
            self.linia_info = tk.Label(self.top, text = "Ustawienia zapisane!")
            self.linia_info.configure(font=("Arial", 7), bg = "black", fg = "red")
            self.linia_info.place(x = 5, y= 200)
            
            self.linia_info1 = tk.Label(self.top, text = "Musisz zamknąć program i otworzyć ponownie.")
            self.linia_info1.configure(font=("Arial", 7), bg = "black", fg = "skyblue")
            self.linia_info1.place(x = 5, y= 215)
            
            self.button_zamknij = tk.Button(self.top, text = "zamnij program")
            self.button_zamknij.configure(command = self.exit_program)
            self.button_zamknij.place(x = 250, y = 205)
            
        elif self.wynikOkno == 'prawy górny róg':
            self.width = self.window.winfo_screenwidth()
            self.width = self.width - 400
            conn = sqlite3.connect('program.db')
            c = conn.cursor()
            c.execute("INSERT INTO geometria VALUES(NULL, :dlugosc, :szerokosc, :polozenie_x, :polozenie_y, :geo)",
                      {
                          'dlugosc': 390,
                          'szerokosc': 35,
                          'polozenie_x': self.width,
                          'polozenie_y': 2,
                          'geo': "right_up"
                      })
            conn.commit()
            conn.close()
            
            self.buttonZapisz.destroy()
            self.linia_info = tk.Label(self.top, text = "Ustawienia zapisane!")
            self.linia_info.configure(font=("Arial", 7), bg = "black", fg = "red")
            self.linia_info.place(x = 5, y= 200)
            
            self.linia_info1 = tk.Label(self.top, text = "Musisz zamknąć program i otworzyć ponownie.")
            self.linia_info1.configure(font=("Arial", 7), bg = "black", fg = "skyblue")
            self.linia_info1.place(x = 5, y= 215)
            
            self.button_zamknij = tk.Button(self.top, text = "zamnij program")
            self.button_zamknij.configure(command = self.exit_program)
            self.button_zamknij.place(x = 250, y = 205)
            
        elif self.wynikOkno == 'dolny lewy róg':
            self.height = self.window.winfo_screenheight()
            self.height = self.height - 100
            conn = sqlite3.connect('program.db')
            c = conn.cursor()
            c.execute("INSERT INTO geometria VALUES(NULL, :dlugosc, :szerokosc, :polozenie_x, :polozenie_y, :geo)",
                      {
                          'dlugosc': 390,
                          'szerokosc': 35,
                          'polozenie_x': 1,
                          'polozenie_y': self.height,
                          'geo': "left_down"
                      })
            conn.commit()
            conn.close()
            
            self.buttonZapisz.destroy()
            self.linia_info = tk.Label(self.top, text = "Ustawienia zapisane!")
            self.linia_info.configure(font=("Arial", 7), bg = "black", fg = "red")
            self.linia_info.place(x = 5, y= 200)
            
            self.linia_info1 = tk.Label(self.top, text = "Musisz zamknąć program i otworzyć ponownie.")
            self.linia_info1.configure(font=("Arial", 7), bg = "black", fg = "skyblue")
            self.linia_info1.place(x = 5, y= 215)
            
            self.button_zamknij = tk.Button(self.top, text = "zamnij program")
            self.button_zamknij.configure(command = self.exit_program)
            self.button_zamknij.place(x = 250, y = 205)
            
        elif self.wynikOkno == 'dolny prawy róg':
            self.width = self.window.winfo_screenwidth()
            self.width = self.width - 400
            self.height = self.window.winfo_screenheight()
            self.height = self.height - 100
            conn = sqlite3.connect('program.db')
            c = conn.cursor()
            c.execute("INSERT INTO geometria VALUES(NULL, :dlugosc, :szerokosc, :polozenie_x, :polozenie_y, :geo)",
                      {
                          'dlugosc': 390,
                          'szerokosc': 35,
                          'polozenie_x': self.width,
                          'polozenie_y': self.height,
                          'geo': "left_down"
                      })
            conn.commit()
            conn.close()
            
            self.buttonZapisz.destroy()
            self.linia_info = tk.Label(self.top, text = "Ustawienia zapisane!")
            self.linia_info.configure(font=("Arial", 7), bg = "black", fg = "red")
            self.linia_info.place(x = 5, y= 200)
            
            self.linia_info1 = tk.Label(self.top, text = "Musisz zamknąć program i otworzyć ponownie.")
            self.linia_info1.configure(font=("Arial", 7), bg = "black", fg = "skyblue")
            self.linia_info1.place(x = 5, y= 215)
            
            self.button_zamknij = tk.Button(self.top, text = "zamnij program")
            self.button_zamknij.configure(command = self.exit_program)
            self.button_zamknij.place(x = 250, y = 205)
            
        else:
            self.width = self.window.winfo_screenwidth()
            self.width = int((self.width/2)-195)
            self.height = self.window.winfo_screenheight()
            self.height = int((self.height/2)-12)
            conn = sqlite3.connect('program.db')
            c = conn.cursor()
            c.execute("INSERT INTO geometria VALUES(NULL, :dlugosc, :szerokosc, :polozenie_x, :polozenie_y, :geo)",
                      {
                          'dlugosc': 390,
                          'szerokosc': 35,
                          'polozenie_x': self.width,
                          'polozenie_y': self.height,
                          'geo': "centre"
                      })
            conn.commit()
            conn.close()
            
            self.buttonZapisz.destroy()
            self.linia_info = tk.Label(self.top, text = "Ustawienia zapisane!")
            self.linia_info.configure(font=("Arial", 7), bg = "black", fg = "red")
            self.linia_info.place(x = 5, y= 200)
            
            self.linia_info1 = tk.Label(self.top, text = "Musisz zamknąć program i otworzyć ponownie.")
            self.linia_info1.configure(font=("Arial", 7), bg = "black", fg = "skyblue")
            self.linia_info1.place(x = 5, y= 215)
            
            self.button_zamknij = tk.Button(self.top, text = "zamnij program")
            self.button_zamknij.configure(command = self.exit_program)
            self.button_zamknij.place(x = 250, y = 205)
            
    def zapisz_ustawienia_gielda(self):
        pass
        
    def zapisz_ustawienia_waluta(self):
        pass
    
    
        #self.top.mainloop()
        
prog = Program()