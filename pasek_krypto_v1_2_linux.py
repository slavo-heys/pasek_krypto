#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 09:08:06 2021

"Pasek Krypto" versja 1.2 Windows

@author: slavo heys 
@email: ilodz24hd@gmail.com
"""

import json
import requests
import tkinter as tk

class Program:
    def __init__(self):
        self.window = tk.Tk()

# %% deklaracja zmiennych
        self.dictionary = dict()
        self.lista = []

        self.waluta = tk.StringVar()
        self.bidPrice = tk.StringVar()
        self.askPrice = tk.StringVar()
        self.walutaBtc = tk.StringVar()
        self.bidPriceBtc = tk.StringVar()
        self.askPriceBtc = tk.StringVar()
        self.symbol = tk.StringVar()
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

        # czcionka
        self.krojCzcionki = "Comic Sans"  # Times New Roman, Tahoma, Comic Sans
        self.rozmiarCzcionki = 15
        # definicja kolorów
        self.red = "#FF4500"
        self.green = "#00FF00"
        self.white = "white"
        self.black = "black"

# %% otwarcie okna programu
        self.window.geometry("500x40+5+5")
        self.window.configure(background="black")
        self.window.overrideredirect(1)

# %% ramka okna programu
        self.rama = tk.LabelFrame(self.window, padx=5, pady=5)
        self.rama.configure(background="black")
        self.rama.pack(fill="both", expand="yes")

        self.button1 = tk.Button(self.rama, text="Exit", font=("Arial", 8),
                                 bg=self.white, fg=self.black, command=self.exit)
        self.button1.grid(row=0, column=7)

        self.nazwaWaluty = tk.Label(self.rama, bg=self.black)
        self.nazwaWaluty.grid(row=0, column=0)

        self.przerwa = tk.Label(self.rama, text=" - ", bg=self.black)
        self.przerwa.grid(row=0, column=1)

        self.liniaBidSymbol = tk.Label(self.rama, text="BID:", font=(
            "Arial", 8), bg=self.black, fg="#FFD700")
        self.liniaBidSymbol.grid(row=0, column=2)

        self.liniaBidBtc = tk.Label(self.rama, bg=self.black)
        self.liniaBidBtc.grid(row=0, column=3)

        self.przerwa1 = tk.Label(self.rama, text=" - ", bg=self.black)
        self.przerwa1.grid(row=0, column=4)

        self.liniaAskSymbol = tk.Label(self.rama, text="ASK:", font=(
            "Arial", 8), bg=self.black, fg="#FFD700")
        self.liniaAskSymbol.grid(row=0, column=5)

        self.liniaAskBtc = tk.Label(self.rama, bg=self.black)
        self.liniaAskBtc.grid(row=0, column=6)

# %% Wywołanie definicji
        self.api_binance_btc()

# %%
        self.window.mainloop()

# %% definicje
    def exit(self):
        self.window.destroy()

    def api_binance_btc(self):
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
            self.symbol.set(self.lista[0][0])
            self.cenaBidBtc.set(self.lista[0][1])
            self.cenaAskBtc.set(self.lista[0][2])

            self.nazwaWaluty.configure(text=self.symbol.get(), font=(
                self.krojCzcionki, self.rozmiarCzcionki), fg=self.white)
            self.liniaBidBtc.configure(text=self.cenaBidBtc.get(), font=(
                self.krojCzcionki, self.rozmiarCzcionki), fg=self.white)
            self.liniaAskBtc.configure(text=self.cenaAskBtc.get(), font=(
                self.krojCzcionki, self.rozmiarCzcionki), fg=self.white)

        x = len(self.lista)
        if x == 3:
            del self.lista[0]
            self.symbol.set(self.lista[0][0])
            self.staryBidBtc.set(self.lista[0][1])
            self.staryAskBtc.set(self.lista[0][2])
            self.nowyBidBtc.set(self.lista[1][1])
            self.nowyAskBtc.set(self.lista[1][2])

            self.staryBid = float(self.staryBidBtc.get())
            self.staryAsk = float(self.staryAskBtc.get())
            self.nowyBid = float(self.nowyBidBtc.get())
            self.nowyAsk = float(self.nowyAskBtc.get())

            if self.nowyBid > self.staryBid:
                self.nazwaWaluty.configure(text=self.symbol.get(), font=(
                    self.krojCzcionki, self.rozmiarCzcionki), fg=self.white)
                self.liniaBidBtc.configure(text=self.nowyBid, font=(
                    self.krojCzcionki, self.rozmiarCzcionki), fg="#FF0000")
            elif self.nowyBid < self.staryBid:
                self.nazwaWaluty.configure(text=self.symbol.get(), font=(
                    self.krojCzcionki, self.rozmiarCzcionki), fg=self.white)
                self.liniaBidBtc.configure(text=self.nowyBid, font=(
                    self.krojCzcionki, self.rozmiarCzcionki), fg="#00FF00")
            else:
                self.nazwaWaluty.configure(text=self.symbol.get(), font=(
                    self.krojCzcionki, self.rozmiarCzcionki), fg=self.white)
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

        self.window.after(1000, self.api_binance_btc)


prog = Program()
