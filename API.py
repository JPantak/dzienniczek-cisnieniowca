import tkinter
from tkcalendar import Calendar
import matplotlib.pyplot as plt

from db_access import *
from tkinter import filedialog
from datetime import datetime
import tkinter as tk
import pandas as pd
import copy
#auxiliary functions

# temp_date = ''

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
def draw_plot(draw_sp, draw_dp, draw_ht):
    if draw_sp == 1 or draw_dp == 1 or draw_ht == 1:
        labels = []
        ylabel = []
        time_labels = []
        plot_x = main_db.get_values('date')
        plot_y3 = main_db.get_values('ht')
        plot_y2 = main_db.get_values('dp')
        plot_y1 = main_db.get_values('sp')
        plot_xticks = main_db.get_date()

        fig = plt.figure(layout='constrained')
        ax = fig.subplots()
        if draw_sp == 1:
            ax.plot(plot_x, plot_y1, color='tab:blue')
            labels.append('Ciś. Skurczowe')
        if draw_dp == 1:
            ax.plot(plot_x, plot_y2, color='tab:red')
            labels.append('Ciś. Rozkurczowe')

        if draw_dp == 1 or draw_sp == 1: ylabel.append('Ciśnienie [mmHg]')

        if draw_ht == 1:
            ax.plot(plot_x, plot_y3, color='tab:green')
            labels.append('Tętno')
            ylabel.append('Tętno [BPM]')


        ax.legend(labels, title='Zmienne')
        ax.set_ylabel(ylabel)
        ax.set_xlabel('Data')
        plt.xticks(plot_x, plot_xticks, rotation=45)
        plt.show()

#enter the date
# def enter_date():
#     top = tkinter.Toplevel()
#     top.title("Date enter")
#
#     date_frame = tk.LabelFrame(top, text="Wprowadź datę:", padx=10, pady=10)
#     date_frame.pack()
#     cal = Calendar(date_frame, selectmode='day', date_pattern='dd/mm/YYYY')
#     time_input_frame = tk.LabelFrame(date_frame, text="Czas", padx=10, pady=10)
#     time_input_frame.columnconfigure(0, weight=1)
#     time_input_frame.columnconfigure(1, weight=1)
#     sec_input_frame = tk.Label(time_input_frame, text="sekundy")
#     sec_input_frame.grid(row=0, column=0, )
#     sec = tk.Spinbox(time_input_frame, from_=0, to=60)
#     sec.grid(row=0, column=1)
#     min_input_frame = tk.Label(time_input_frame, text="minuty")
#     min_input_frame.grid(row=1, column=0)
#     min = tk.Spinbox(time_input_frame, from_=0, to=60)
#     min.grid(row=1, column=1)
#
#     hour_input_frame = tk.Label(time_input_frame, text="godziny")
#     hour_input_frame.grid(row=2, column=0)
#     hour = tk.Spinbox(time_input_frame, from_=0, to=24)
#     hour.grid(row=2, column=1)
#
#     def change_date():
#         global temp_date
#         temp_date = f'{cal.get_date()} {hour.get()}:{min.get()}:{sec.get()}'
#         top.destroy()
#
#     button_change_date = tk.Button(date_frame, text="Zapisz date", command=lambda: change_date())
#     button_change_date.grid(row=3)
#
#
#     for widget in date_frame.winfo_children():  # pętla ustawiająca padx i pady dla
#         widget.grid_configure(padx=10, pady=5)  # wszystkich widgetów w pressure_input_frame

