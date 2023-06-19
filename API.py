import tkinter
from tkcalendar import Calendar
import matplotlib.pyplot as plt

from db_access import *
from tkinter import filedialog
from tkinter import ttk
from datetime import datetime
import tkinter as tk
import pandas as pd
#auxiliary functions

# temp_date = ''
show_db = Database()
# adding db record from GUI


def gui_add_entry(date: str, sp: int, dp: int, ht: int, strv, root):
    global main_db, show_db
    # check data correctness
    #TODO: dodać sprawdzanie poprawności danych (czy data ma poprawny format, a pozostałe dane mieszczą się w przedziałachn np. 40-210), dodać prompta!!!
    if sp is int and dp is int and ht is int:
        main_db.add_entry(date, sp, dp, ht)
        show_db = main_db
        refresh_trv(root, strv)
        strv.set(str(main_db))
    else:
        print("Błąd wprowadzanych danych")

    # main_db.add_entry(date, sp, dp, ht)
    # show_db = main_db
    # refresh_trv(root,strv)
    # strv.set(str(main_db))


def gui_delete_last_entry(strv):
    global main_db
    main_db.del_entry()
    strv.set(str(main_db))
    #TODO: zablokowac mozliwosc usuniecia ostatniego wpisu przy pustej bazie danych.


def new_file(root, strv=None):
    global main_db
    main_db = Database()
    refresh_trv(root, strv)
    if strv is not None:
        strv.set(str(main_db))


def select_file(root,strv):
    global main_db
    global show_db
    filetypes = [
        ('csv files', '*.csv')
    ]
    path = filedialog.askopenfilename(filetypes=filetypes)
    main_db = Database(path)
    show_db = main_db
    refresh_trv(root, strv)
    strv.set(str(main_db))
    

def save_file():
    global main_db
    filetypes = [
        ('csv files', '*.csv')
    ]
    path = filedialog.asksaveasfile(filetypes=filetypes,defaultextension="*.*")
    main_db.save(path.name)
    
# draw plot


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


# enter the date
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

# search in db
def search_db(root, type, variable, strv):
    global show_db
    print(type, variable)
    if type == "Data":
        show_db = main_db.filter(date=variable)
    elif type == "Ciśnienie skurczowe":
        show_db = main_db.filter(sp=int(variable))
    elif type == "Ciśnienie rozkurczowe":
        show_db = main_db.filter(dp=int(variable))
    elif type == "Tętno":
        show_db = main_db.filter(ht=int(variable))
    refresh_trv(root,strv)
    if strv is not None:
        strv.set(str(show_db))


def show_main_db(root,strv):
    global show_db
    show_db = main_db
    refresh_trv(root,strv)
    if strv is not None:
        strv.set(str(show_db))


def refresh_trv(root, show_frame_text):
    global show_db
    columns = ['date', 'dp', 'sp', 'ht']
    columns_width = [120, 40, 40, 40]
    trv = ttk.Treeview(root, selectmode='browse', height=10,
                       show='headings', columns=columns)
    trv.grid(row=4, column=4, columnspan=4, padx=10, pady=20)
    
    for i, col in enumerate(columns):
        trv.column(col, width=columns_width[i], anchor='c')
        trv.heading(col, text=str(col))
    for dt in show_db.to_numpy():
        v = [r for r in dt]
        trv.insert("", 'end', iid=v[0],values=v)
    show_frame = tk.LabelFrame(root, text="Pomiary ciśnienia", padx=10, pady=10)
    show_frame_text.set(str(show_db))
    left = tk.Label(show_frame, textvariable=show_frame_text)
    left.pack()

# def entry_window(root,show_frame_text):
#     global show_db
#     top = tk.Toplevel(root)
#     top.title("Pomiary")
#     top.geometry("400x400")
#     refresh_trv(top,show_frame_text)
