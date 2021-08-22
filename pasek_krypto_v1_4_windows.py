# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 09:08:06 2021
"Pasek Krypto" versja 1.4 Windows 10
@author: slavo heys 
@email: ilodz24hd@gmail.com
"""

import requests
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3


class Program:
    def __init__(self):
        self.window = tk.Tk()
        
# %% deklaracja zmiennych
        self.szerOkna = tk.StringVar()
        self.dlugOkna = tk.StringVar()
        self.poloX = tk.StringVar()
        self.poloY = tk.StringVar()
        self.koloOkna = tk.StringVar()
        self.dlugosc = tk.StringVar()
        self.szerokosc = tk.StringVar()
        self.polozenie_x = tk.StringVar()
        self.polozenie_y = tk.StringVar()
        self.kolor = tk.StringVar()
        self.kolor_pen = tk.StringVar()
        self.kolorPen = tk.StringVar()
        self.waluta = tk.StringVar()
        self.bidPrice = tk.StringVar()
        self.askPrice = tk.StringVar()
        self.walutaBtc = tk.StringVar()
        self.bidPriceBtc = tk.StringVar()
        self.askPriceBtc = tk.StringVar()
        self.cenaBidBtc = tk.StringVar()
        self.cenaAskBtc = tk.StringVar()
        self.staryBidBtc = tk.StringVar()
        self.staryAskBtc = tk.StringVar()
        self.nowyBidBtc = tk.StringVar()
        self.nowyAskBtc = tk.StringVar()
        self.staryBid = tk.StringVar()
        self.staryAsk = tk.StringVar()
        self.nowyBid = tk.StringVar()
        self.nowyAsk = tk.StringVar()
        
        self.lista = []
        self.dictionary = dict()
        
# %% czcionka
        self.krojCzcionki = "Comic Sans"  # Times New Roman, Tahoma, Comic Sans
        self.rozmiarCzcionki = 12
        
# %% definicja kolorów
        self.red = "#FF4500"
        self.green = "#00FF00"
        self.white = "white"
        self.black = "black"

# %% wywolanie bazy sqlite
        self.baza_sql()
        
# %% otwarcie okna programu
        conn = sqlite3.connect('program.db')
        c = conn.cursor()
        c.execute("SELECT * FROM geometria ORDER BY id DESC LIMIT 1")
        wynik = c.fetchall()
        for row in wynik:
            self.dlugosc.set(row[1])
            self.szerokosc.set(row[2])
            self.polozenie_x.set(row[3])
            self.polozenie_y.set(row[4])
            self.kolor.set(row[5])
            self.kolor_pen.set(row[6])
            
        c.close()
        
        self.dlugOkna = self.dlugosc.get()
        self.szerOkna = self.szerokosc.get()
        self.poloX = self.polozenie_x.get()
        self.poloY = self.polozenie_y.get()
        self.koloOkna = self.kolor.get()
        self.kolorPen = self.kolor_pen.get()
        
        self.geometry = self.dlugOkna+"x"+self.szerOkna+"+"+self.poloX+"+"+self.poloY
        self.window.geometry(self.geometry)
        self.window.configure(background="black")
        self.window.overrideredirect(1)
        
# %% otworzenie ramki programu
        self.rama = tk.LabelFrame(self.window, padx=5, pady=5)
        self.rama.configure(background="black")
        self.rama.pack(fill="both", expand="yes")
        
        # przyciski okna
        #self.button_ustawienia = tk.Button(self.rama, text = "USTAWIENIA", font = ("Arial", 7), bg = "silver", fg = "black")
        #self.button_ustawienia.configure(command = self.setting)
        #self.button_ustawienia.place(x= 330, y = 0)
        
        self.button_exit = tk.Button(self.rama, text = "EXIT", font = ("Arial", 7), bg = "silver", fg = "red")
        self.button_exit.configure(command = self.exit_program)
        self.button_exit.place(x = 280, y = 0)
        # symbol ceny
        self.linia_symbol = tk.Label(self.rama, bg = "black", fg = self.kolorPen)
        self.linia_symbol.configure(text = "BTC-USD", font = ("Arial", 5))
        self.linia_symbol.place(x = 0, y = 0)
        # oznaczenie giełdy
        self.linia_gielda = tk.Label(self.rama, bg = "black", fg = "gold")
        self.linia_gielda.configure(text = "BINANCE", font = ("Arial", 5))
        self.linia_gielda.place(x = 0, y = 9)
        # oznaczenie bid
        self.linia_bid = tk.Label(self.rama, bg = "black", fg = self.kolorPen)
        self.linia_bid.configure(text = "BID", font = ("Arial", 7))
        self.linia_bid.place(x = 50, y = 3)
        # linia bid binance
        self.liniaBidBtc = tk.Label(self.rama, bg = "black")
        self.liniaBidBtc.place(x = 80, y = 0)
        # oznaczenia ask
        self.linia_ask = tk.Label(self.rama, bg = "black", fg = self.kolorPen)
        self.linia_ask.configure(text = "ASK", font = ("Arial", 7))
        self.linia_ask.place(x = 165, y = 3)
        # linia ask binance
        self.liniaAskBtc = tk.Label(self.rama, bg = "black")
        self.liniaAskBtc.place(x = 190, y = 0)
        
        
        
# %% Wywołanie definicji
        self.gielda_binance()

# %%
        self.window.mainloop()
        
# %% definicje programu
    def baza_sql(self):
        conn = sqlite3.connect('program.db')
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS geometria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dlugosc text NOT NULL,
            szerokosc text NOT NULL,
            polozenie_x text NOT NULL,
            polozenie_y text NOT NULL,
            kolor_tla text NOT NULL,
            kolor_pen text NOT NULL,
            ksztalt text NOT NULL);"""
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
            c.execute("INSERT INTO geometria VALUES(NULL, :dlugosc, :szerokosc, :polozenie_x, :polozenie_y, :kolor_tla, :kolor_pen, :ksztalt)",
                      {
                          'dlugosc': 320,
                          'szerokosc': 35,
                          'polozenie_x': 1,
                          'polozenie_y': 2,
                          'kolor_tla': "black",
                          'kolor_pen': "skyblue",
                          'ksztalt': "pojedyńcza linia pozioma"
                      })
            conn.commit()
            conn.close()

    def exit_program(self):
        self.window.destroy()  
        
    def setting(self):
        pass
    
    def gielda_binance(self):
        self.readBinance = requests.get(
            "https://fapi.binance.com/fapi/v1/ticker/bookTicker")
        self.task = self.readBinance.json()
        self.dictionary = (self.task)

        self.waluta.set(self.dictionary[0]["symbol"])
        self.bidPrice.set(self.dictionary[0]["bidPrice"])
        self.askPrice.set(self.dictionary[0]["askPrice"])

        self.walutaBtc = self.waluta.get()
        self.bidPriceBtc = self.bidPrice.get()
        self.askPriceBtc = self.askPrice.get()

        self.lista.append([self.walutaBtc, self.bidPriceBtc, self.askPriceBtc])

        y = len(self.lista)
        if y <= 2:
            self.cenaBidBtc.set(self.lista[0][1])
            self.cenaAskBtc.set(self.lista[0][2])

            self.liniaBidBtc.configure(text=self.cenaBidBtc.get(), font=(
                self.krojCzcionki, self.rozmiarCzcionki), fg=self.white)
            self.liniaAskBtc.configure(text=self.cenaAskBtc.get(), font=(
                self.krojCzcionki, self.rozmiarCzcionki), fg=self.white)

        x = len(self.lista)
        if x == 3:
            del self.lista[0]
            
            self.staryBidBtc.set(self.lista[0][1])
            self.staryAskBtc.set(self.lista[0][2])
            self.nowyBidBtc.set(self.lista[1][1])
            self.nowyAskBtc.set(self.lista[1][2])

            self.staryBid = float(self.staryBidBtc.get())
            self.staryAsk = float(self.staryAskBtc.get())
            self.nowyBid = float(self.nowyBidBtc.get())
            self.nowyAsk = float(self.nowyAskBtc.get())

            if self.nowyBid > self.staryBid:
                self.liniaBidBtc.configure(text=self.nowyBid, font=(
                    self.krojCzcionki, self.rozmiarCzcionki), fg="#FF0000")
            elif self.nowyBid < self.staryBid:
                self.liniaBidBtc.configure(text=self.nowyBid, font=(
                    self.krojCzcionki, self.rozmiarCzcionki), fg="#00FF00")
            else:
                self.liniaBidBtc.configure(text=self.nowyBid, font=(
                    self.krojCzcionki, self.rozmiarCzcionki), fg="#C0C0C0")

            if self.nowyAsk > self.staryAsk:
                self.liniaAskBtc.configure(text=self.nowyAsk, font=(
                    self.krojCzcionki, self.rozmiarCzcionki), fg="#FF0000")
            elif self.nowyAsk < self.staryAsk:
                self.liniaAskBtc.configure(text=self.nowyAsk, font=(
                    self.krojCzcionki, self.rozmiarCzcionki), fg="#00FF00")
            else:
                self.liniaAskBtc.configure(text=self.nowyAsk, font=(
                    self.krojCzcionki, self.rozmiarCzcionki), fg="#C0C0C0")

        self.window.after(1000, self.gielda_binance)
        
    
        
        
        
        
prog = Program()