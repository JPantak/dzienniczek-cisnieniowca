#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import ttk, Menu, IntVar
from tkcalendar import Calendar
from API import *
import matplotlib.pyplot as plt

def donothing():
   pass

# okno?
root = tk.Tk()
root.title("Dziennik ciśnieniowca")
main_db = Database()
#menu głowne
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
new_file()
filemenu.add_command(label="New", command=lambda: new_file(show_frame_text))
filemenu.add_command(label="Open", command=lambda : select_file(show_frame_text))
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

cal = Calendar(pressure_input_frame, selectmode = 'day',date_pattern = 'dd/mm/YYYY')
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



 
# data label i entry
# label_date = tk.Label(pressure_input_frame, text="DD-MM-YYYY:")
# label_date.grid(row=2, column=0, sticky="w")
# entry_date = tk.Entry(pressure_input_frame)
# entry_date.grid(row=3, column=0)

for widget in pressure_input_frame.winfo_children():    # pętla ustawiająca padx i pady dla
    widget.grid_configure(padx=10, pady=5)              # wszystkich widgetów w pressure_input_frame

# przyciski do zapisu i usuwania
button_data_entry = tk.Button(pressure_input_frame, text="Zapisz pomiar", command=lambda: gui_add_entry(f'{cal.get_date()} {hour.get()}:{min.get()}:{sec.get()}',entry_systolic_pressure.get(),entry_diastolic_pressure.get(),entry_heart_rate.get(),show_frame_text))
button_data_entry.grid(row=4, column=0, sticky="w"+"e", columnspan=3)

button_remove_last_data_entry = tk.Button(pressure_input_frame, text="Usuń wcześniej dodany pomiar",command= lambda: gui_delete_last_entry(show_frame_text))
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

#Plot options
plot_dp = IntVar()
plot_sp = IntVar()
plot_ht = IntVar()
plot_options = tk.LabelFrame(main_frame, text="Opcje wykresu", padx=10, pady=10)
plot_options.pack(fill='both')
checkbox_show_sp = tk.Checkbutton(plot_options, text='Show SP',variable=plot_sp, onvalue=1, offvalue=0)
checkbox_show_sp.pack()
checkbox_show_dp = tk.Checkbutton(plot_options, text='Show DP',variable=plot_dp, onvalue=1, offvalue=0)
checkbox_show_dp.pack()
checkbox_show_ht = tk.Checkbutton(plot_options, text='Show HT',variable=plot_ht, onvalue=1, offvalue=0)
checkbox_show_ht.pack()

button_draw_plot = tk.Button(plot_options, text="Rysuj wykres", command=lambda: draw_plot(df,1,1,1))
button_draw_plot.pack()


# pokazywanie wynikow w tym samym oknie
show_frame = tk.LabelFrame(main_frame, text="Pomiary ciśnienia", padx=10, pady=10)
show_frame.pack(fill='both',expand="yes")
show_frame_text = tk.StringVar()
show_frame_text.set(str(main_db))
left = tk.Label(show_frame, textvariable=show_frame_text)
left.pack()
 
root.resizable(False, False)
root.config(menu=menubar)

#start GUI refresh loop
root.mainloop()
