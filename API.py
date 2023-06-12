from db_access import *
#auxiliary functions

#adding db record from GUI
def gui_add_entry (date: str, sp: int, dp: int, ht: int):
    #check data correctness
    #TODO: dodać sprawdzanie poprawności danych (czy data ma poprawny format, a pozostałe dane mieszczą się w przedziałachn np. 40-210), dodać prompta!!!

    main_db.add_entry(date, sp, dp, ht)

def gui_delete_last_entry():

    #TODO: dodać usuwanie ostatniego wpisu!!!
    pass