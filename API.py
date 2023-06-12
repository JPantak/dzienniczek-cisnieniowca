import matplotlib.pyplot as plt

from db_access import *
from tkinter import filedialog
import tkinter as tk
import pandas as pd
import copy
#auxiliary functions

#adding db record from GUI
def gui_add_entry (date: str, sp: int, dp: int, ht: int,strv):
    global main_db
    #check data correctness
    #TODO: dodać sprawdzanie poprawności danych (czy data ma poprawny format, a pozostałe dane mieszczą się w przedziałachn np. 40-210), dodać prompta!!!
    print(date)
    main_db.add_entry(date, sp, dp, ht)
    strv.set(str(main_db))

def gui_delete_last_entry(strv):
    global main_db
    main_db.del_entry()
    strv.set(str(main_db))
    #TODO: zablokowac mozliwosc usuniecia ostatniego wpisu przy pustej bazie danych.

def new_file(strv = None):
    global main_db
    main_db = Database()
    if(strv != None):
        strv.set(str(main_db))

def select_file(strv):
    global main_db
    filetypes = [
        ('csv files', '*.csv')
    ]
    path = filedialog.askopenfilename(filetypes=filetypes)
    main_db = Database(path)
    strv.set(str(main_db))
    

def save_file():
    global main_db
    filetypes = [
        ('csv files', '*.csv')
    ]
    path = filedialog.asksaveasfile(filetypes=filetypes,defaultextension="*.*")
    main_db.save(path.name)
    
#draw plot
def draw_plot(db, draw_sp, draw_dp, draw_ht):
    plot_x = main_db.get_values('date')
    plot_y2 = main_db.get_values('dp')
    plot_y1 = main_db.get_values('sp')
    fig = plt.figure()
    ax = fig.subplots()
    ax.plot(plot_x, plot_y1, color='tab:blue')
    ax.plot(plot_x, plot_y2, color='tab:red')
    plt.show()
