#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import ttk, Menu, IntVar
from tkcalendar import Calendar

import API
from API import *
import matplotlib.pyplot as plt
import numpy as np


def donothing():
   pass

# okno
root = tk.Tk()
root.title("Dziennik ciśnieniowca")
main_db = Database()
# menu głowne
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
# new_file(show_frame)
filemenu.add_command(label="New", command=lambda: new_file(show_frame,show_frame_text))
filemenu.add_command(label="Open", command=lambda : select_file(show_frame,show_frame_text))
filemenu.add_command(label="Save", command=lambda: save_file())
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

# głowny frame w oknie
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack()

frame_left = tk.Frame(main_frame, padx=10, pady=10)
frame_left.grid(row=0, column=0)

frame_right = tk.Frame(main_frame, padx=10, pady=10)
frame_right.grid(row=0, column=1)

# frame do wprowadzania pomiarów
pressure_input_frame = tk.LabelFrame(frame_left, text="Wprowadzanie nowych pomiarów ciśnienia", padx=10, pady=10)
pressure_input_frame.grid(row=0, column=0)
# ciśnienie skurczowe label i entry
label_systolic_pressure = tk.Label(pressure_input_frame, text="Ciśnienie skurczowe:", anchor="w")
label_systolic_pressure.grid(row=0, column=0, sticky="w")
entry_systolic_pressure = tk.Entry(pressure_input_frame)
entry_systolic_pressure.grid(row=1, column=0)

# ciśnienie rozkurczowe label i entry
label_diastolic_pressure = tk.Label(pressure_input_frame, text="Ciśnienie rozkurczowe:", anchor="w")
label_diastolic_pressure.grid(row=0, column=1, sticky="w")
entry_diastolic_pressure = tk.Entry(pressure_input_frame)
entry_diastolic_pressure.grid(row=1, column=1)

# tętno label i entry
label_heart_rate = tk.Label(pressure_input_frame, text="Tętno:")
label_heart_rate.grid(row=0, column=2, sticky="w")
entry_heart_rate = tk.Entry(pressure_input_frame)
entry_heart_rate.grid(row=1, column=2)

#wprowadzana data
# date_entry_text = tk.StringVar()
# date_entry_text.set(temp_date)
# label_date = tk.Label(pressure_input_frame, text="Wprowadzona data:")
# label_date.grid(row=0, column=3, sticky="w")
# label_date_entry = tk.Label(pressure_input_frame, textvariable=date_entry_text)
# label_date_entry.grid(row=1, column=3)




#wprowadzanie daty
cal = Calendar(pressure_input_frame, selectmode = 'day',date_pattern = 'YYYY/mm/dd')
time_input_frame = tk.LabelFrame(pressure_input_frame, text="Czas", padx=10, pady=10)
time_input_frame.columnconfigure(0,weight=1)
time_input_frame.columnconfigure(1,weight=1)
sec_input_frame = tk.Label(time_input_frame, text="sekundy")
sec_input_frame.grid(row=0, column=0,)
sec = tk.Spinbox(time_input_frame, from_=0, to=60)
sec.grid(row=0,column=1)
min_input_frame = tk.Label(time_input_frame, text="minuty")
min_input_frame.grid(row=1,column=0)
min = tk.Spinbox(time_input_frame, from_=0, to=60)
min.grid(row=1,column=1)

hour_input_frame = tk.Label(time_input_frame, text="godziny")
hour_input_frame.grid(row=2,column=0)
hour = tk.Spinbox(time_input_frame, from_=0, to=24)
hour.grid(row=2,column=1)

# button_change_date = tk.Button(main_frame, text="Wprowadz date", command=lambda: enter_date())
# button_change_date.pack()



 
# data label i entry
# label_date = tk.Label(pressure_input_frame, text="DD-MM-YYYY:")
# label_date.grid(row=2, column=0, sticky="w")
# entry_date = tk.Entry(pressure_input_frame)
# entry_date.grid(row=3, column=0)

for widget in pressure_input_frame.winfo_children():    # pętla ustawiająca padx i pady dla
    widget.grid_configure(padx=10, pady=5)              # wszystkich widgetów w pressure_input_frame

# przyciski do zapisu i usuwania
button_data_entry = tk.Button(pressure_input_frame, text="Zapisz pomiar", command=lambda: gui_add_entry(f'{cal.get_date()} {hour.get()}:{min.get()}:{sec.get()}',entry_systolic_pressure.get(),entry_diastolic_pressure.get(),entry_heart_rate.get(),show_frame_text,show_frame))
button_data_entry.grid(row=5, column=0, sticky="w"+"e", columnspan=3)

button_remove_last_data_entry = tk.Button(pressure_input_frame, text="Usuń wcześniej dodany pomiar",command= lambda: gui_delete_last_entry(show_frame_text))
button_remove_last_data_entry.grid(row=6, column=0, sticky="w"+"e", columnspan=3, pady=5)

# frame do szukania pomiarów
search_measure_frame = tk.LabelFrame(frame_left, text="Wyszukaj pomiar ciśnienia", padx=10, pady=10)
search_measure_frame.grid(row=1, column=0, sticky="w"+"e")

search_by_date_frame = tk.LabelFrame(search_measure_frame, text="Wyszukaj po dacie:")
search_by_date_frame.grid(row=0, column=0)

search_by_value_frame = tk.LabelFrame(search_measure_frame, text="Wyszukaj po wartości:")
search_by_value_frame.grid(row=0, column=1)

for widget in search_measure_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

label_date_2 = tk.Label(search_by_date_frame, text="YYYY-mm-dd HH:MM:SS :")
label_date_2.grid(row=0, column=0, sticky="w")

entry_date_2 = tk.Entry(search_by_date_frame)
entry_date_2.grid(row=1, column=0)

for widget in search_by_date_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

search_type_combobox = ttk.Combobox(search_by_value_frame, values=[" ", "Data", "Ciśnienie skurczowe", "Ciśnienie rozkurczowe", "Tętno"])
search_type_combobox.grid(row=0, column=0)

entry_type_value = tk.Entry(search_by_value_frame)
entry_type_value.grid(row=1, column=0)

for widget in search_by_value_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

def change_variable():
    if len(entry_type_value.get()) != 0 and (search_type_combobox.get() == "Ciśnienie skurczowe" or search_type_combobox.get() == "Ciśnienie rozkurczowe" or search_type_combobox.get() == "Tętno"):
        search_variable = entry_type_value.get()
        search_db(show_frame,search_type_combobox.get(), search_variable, show_frame_text)
    elif len(entry_date_2.get()) != 0 and search_type_combobox.get() == "Data":
        search_variable = entry_date_2.get()
        search_db(show_frame,search_type_combobox.get(), search_variable, show_frame_text)


button_data_entry = tk.Button(search_measure_frame, text="Szukaj",pady=20, command=lambda: change_variable())
button_data_entry.grid(row=0, column=2)

#Plot options
plot_dp = IntVar()
plot_sp = IntVar()
plot_ht = IntVar()
plot_options = tk.LabelFrame(frame_left, text="Opcje wykresu", padx=10, pady=10)
plot_options.grid(row=2, column=0, sticky="w"+"e")
checkbox_show_sp = tk.Checkbutton(plot_options, text='Pokazuj Ciś. Sk.', variable=plot_sp, onvalue=1, offvalue=0)
checkbox_show_sp.pack(anchor="w")
checkbox_show_dp = tk.Checkbutton(plot_options, text='Pokazuj Ciś. Roz.', variable=plot_dp, onvalue=1, offvalue=0)
checkbox_show_dp.pack(anchor="w")
checkbox_show_ht = tk.Checkbutton(plot_options, text='Pokazuj Tętno', variable=plot_ht, onvalue=1, offvalue=0)
checkbox_show_ht.pack(anchor="w")
button_draw_plot = tk.Button(plot_options, text="Rysuj wykres", command=lambda: draw_plot(plot_sp.get(),plot_dp.get(), plot_ht.get()))
button_draw_plot.pack(fill="x")


# pokazywanie wynikow w tym samym oknie
button_show_db = tk.Button(frame_right, text="Pokaz zawartość bazy", command=lambda: show_main_db(show_frame, show_frame_text))
button_show_db.pack()
show_frame = tk.LabelFrame(frame_right, text="Pomiary ciśnienia", padx=10, pady=10)
show_frame.pack()
show_frame_text = tk.StringVar()
show_frame_text.set(str(show_db))
# left = tk.Label(show_frame, textvariable=show_frame_text)
# left.pack()
 
root.resizable(False, False)
root.config(menu=menubar)

#start GUI refresh loop
root.mainloop()
