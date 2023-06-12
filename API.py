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

def gui_delete_last_entry():

    #TODO: dodać usuwanie ostatniego wpisu!!!
    pass

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
    
    
