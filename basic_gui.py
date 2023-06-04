#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

# okno?
root = tk.Tk()
root.title("Dziennik ciśnienia")

# głowny frame w oknie
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack()

# frame do wprowadzania pomiarów
pressure_input_frame = tk.LabelFrame(main_frame, text="Wprowadzanie nowych pomiarów ciśnienia", padx=10, pady=10)
pressure_input_frame.pack()
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

# data label i entry
label_date = tk.Label(pressure_input_frame, text="DD-MM-YYYY:")
label_date.grid(row=2, column=0, sticky="w")
entry_date = tk.Entry(pressure_input_frame)
entry_date.grid(row=3, column=0)

for widget in pressure_input_frame.winfo_children():    # pętla ustawiająca padx i pady dla
    widget.grid_configure(padx=10, pady=5)              # wszystkich widgetów w pressure_input_frame

# przyciski do zapisu i usuwania
button_data_entry = tk.Button(pressure_input_frame, text="Zapisz pomiar")
button_data_entry.grid(row=4, column=0, sticky="w"+"e", columnspan=3)

button_remove_last_data_entry = tk.Button(pressure_input_frame, text="Usuń wcześniej dodany pomiar")
button_remove_last_data_entry.grid(row=5, column=0, sticky="w"+"e", columnspan=3, pady=5)

# frame do szukania pomiarów
search_measure_frame = tk.LabelFrame(main_frame, text="Wyszukaj pomiar ciśnienia", padx=10, pady=10)
search_measure_frame.pack(fill='x')

search_by_date_frame = tk.LabelFrame(search_measure_frame, text="Wyszukaj po dacie:")
search_by_date_frame.grid(row=0, column=0)

search_by_value_frame = tk.LabelFrame(search_measure_frame, text="Wyszukaj po wartości:")
search_by_value_frame.grid(row=0, column=1)

for widget in search_measure_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

label_date_2 = tk.Label(search_by_date_frame, text="DD-MM-YYYY:")
label_date_2.grid(row=0, column=0, sticky="w")

entry_date_2 = tk.Entry(search_by_date_frame)
entry_date_2.grid(row=1, column=0)

for widget in search_by_date_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

search_type_combobox = ttk.Combobox(search_by_value_frame, values=[" ", "Ciśnienie skurczowe", "Ciśnienie rozkurczowe", "Tętno"])
search_type_combobox.grid(row=0, column=0)

entry_type_value = tk.Entry(search_by_value_frame)
entry_type_value.grid(row=1, column=0)

for widget in search_by_value_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

button_data_entry = tk.Button(search_measure_frame, text="Szukaj")
button_data_entry.grid(row=0, column=2)

root.resizable(False, False)
root.mainloop()
