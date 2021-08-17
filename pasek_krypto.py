
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:08:06 2021

@author: slavo
"""

import json
import requests
# import datetime as dt  # dla obsługi daty i czasu
import tkinter as tk
import sqlite3
from time import strftime


class Application:
    def __init__(self):
        self.window = tk.Tk()

        # deklaracja zmiennych
        self.lista = []
        self.ostatniRekord = tk.StringVar()
        self.przedostatniRekord = tk.StringVar()
        self.btc = tk.StringVar()
        self.btcUsd = tk.StringVar()
        self.rekord1 = tk.StringVar()
        self.rekord2 = tk.StringVar()
        self.data = tk.StringVar()
        self.godzina = tk.StringVar()

        # czcionka
        self.krojCzcionki = "Comic Sans"  # Times New Roman, Tahoma, Comic Sans
        self.rozmiarCzcionki = 15
        # definicja kolorów
        self.red = "#FF4500"
        self.green = "#00FF00"
        self.white = "white"
        self.black = "black"

        self.window.geometry("467x40+5+5")
        self.window.configure(background="black")
        self.window.title("Kryptowaluty - ceny USD")
        self.window.overrideredirect(1)

        self.rama = tk.LabelFrame(self.window, padx=5, pady=5)
        self.rama.configure(background="black")
        self.rama.pack(fill="both", expand="yes")

        self.linia1 = tk.Label(self.rama, text="BTC", font=(self.krojCzcionki, self.rozmiarCzcionki), bg=self.black, fg=self.white)
        self.linia1.grid(row=0, column=0)        

        self.linia2 = tk.Label(self.rama, font=(self.krojCzcionki, self.rozmiarCzcionki))
        self.linia2.grid(row=0, column=1)

        self.linia3 = tk.Label(self.rama, text=" USD ", font=(self.krojCzcionki, self.rozmiarCzcionki), bg=self.black, fg=self.white)
        self.linia3.grid(row=0, column=3)

        self.linia4 = tk.Label(self.rama, text="Ostatnia aktualizacja: ", font=("Arial", 8), bg=self.black,fg=self.white)
        self.linia4.grid(row=0, column=4)

        self.linia5=tk.Label(self.rama, font=("Arial", 8), bg=self.black, fg=self.white)
        self.linia5.grid(row=0, column=5)

        self.linia6=tk.Label(self.rama, font=("Arial", 8), bg=self.black, fg=self.white)
        self.linia6.grid(row=0, column=6)

        self.button1 = tk.Button(self.rama, text=" Exit ", font=("Arial", 8), bg=self.white, fg=self.black, command=self.zamkniecie_programu)
        self.button1.grid(row=0, column=7)        

        

        # wywołanie definicji
        self.binance_krypto()
        self.odczyt_listy()
        self.odczyt_listy()
        self.odczyt_czasu()

        self.window.mainloop()

    #definicje
    def zamkniecie_programu(self):
        exit()

    def binance_krypto(self):
        self.readBTC = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        self.taskBTC = self.readBTC.json()
        self.btcUsd.set(self.taskBTC["price"])
        self.btc = self.btcUsd.get()
        self.btc = float(self.btc)
        self.lista.append(self.btc)
        self.window.after(5000, self.binance_krypto)

    def odczyt_listy(self):
        self.ostatniRekord = len(self.lista)
        self.ostatniRekord = self.ostatniRekord - 1
        

        if len(self.lista) <= 3:
            self.linia2.configure(text=self.lista[self.ostatniRekord], bg=self.black, fg=self.white)
        elif len(self.lista) > 3:
            self.przedostatniRekord = self.ostatniRekord - 2
            self.rekord1=self.lista[self.ostatniRekord]
            self.rekord2=self.lista[self.przedostatniRekord]

            self.rekord1 = int(self.rekord1)
            self.rekord2 = int(self.rekord2)
            if self.rekord1 > self.rekord2:
                self.linia2.configure(text=self.lista[self.ostatniRekord], bg=self.black, fg=self.green)
            elif self.rekord1 < self.rekord2:
                self.linia2.configure(text=self.lista[self.ostatniRekord], bg=self.black, fg=self.red)
            else:
                self.linia2.configure(text=self.lista[self.ostatniRekord], bg=self.black, fg=self.white)
        
        self.window.after(5000, self.odczyt_listy)

    def odczyt_czasu(self):
        self.linia5.configure(text=strftime("%d-%m-%Y"))
        self.linia6.configure(text=strftime("%H:%M:%S"))

        self.window.after(5000, self.odczyt_czasu)
    
    

apl = Application()
