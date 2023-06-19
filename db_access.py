import pandas as pd
import os
import numpy as np

df = pd.read_csv(os.path.join(os.getcwd(), "data/test_db.csv"))


class Database:
    """
    A class to represent the dataframe

    ...

    Attributes
    ===========
    path - path to csv file(optional) - if no path given, the class will
    create an empty dataframe with necessary columns
    
    Methods
    ===========
    get_entry(n) - returns the nth row of the dataframe
    add_entry(date,sp,dp,ht) - adds an entry with given arguments
    edit_entry(n,date,sp,dp,ht) - edits nth entry, all arguments beside n are optional 
    show() - prints out the dataframa associated with the class
    sort_by - sorts the dataframe by specific criteria, ascending - optional argument
    save(name,dir) - saves dataframe to csv file, dir - optional argument

    """
    def __init__(self, path=None):
        if path is not None:
            self.df = pd.read_csv(path)
            self.df["date"] = pd.to_datetime(df["date"], dayfirst=True,format='%d/%m/%Y %H:%M:%S')
        else:
            self.df = pd.DataFrame(columns=["date", "sp", "dp", "ht"])

    def __repr__(self) -> str:
        return self.df.to_string()

    def get_entry(self, n):
        return self.df.loc[n, :]

    def edit_entry(self, n, date: str = None, sp: int = None , dp: int = None, ht: int = None):
            if date is not None:
                self.df.at[n, "date"] = date
            if sp is not None:
                self.df.at[n, "sp"] = sp
            if dp is not None:
                self.df.at[n, "dp"] = dp
            if ht is not None:
                self.df.at[n, "ht"] = ht

    def add_entry(self, date: str, sp: int, dp: int, ht: int) -> None:
        self.df.loc[len(self.df)] = [date, sp, dp, ht]
        self.df["date"] = pd.to_datetime(self.df["date"],dayfirst=True, format='%Y/%m/%d %H:%M:%S')

    def sort_by_date(self, asc=True):
        self.df.sort_values(by="date", ascending=asc, inplace=True, ignore_index=True)

    def sort_by_sp(self, asc=True):
        self.df.sort_values(by="sp", ascending=asc, inplace=True, ignore_index=True)

    def sort_by_dp(self, asc=True):
        self.df.sort_values(by="dp", ascending=asc, inplace=True, ignore_index=True)

    def sort_by_ht(self, asc=True):
        self.df.sort_values(by="ht", ascending=asc, inplace=True, ignore_index=True)

    def save(self, path):
        self.df.to_csv(path, index=False)

    def print(self):
        print(self.df)

    def del_entry(self):
        self.df.drop(len(self.df) - 1, inplace=True)

    def get_values(self,column: str):
        return self.df[column].values.tolist()

    def filter(self, date=None, sp=None, dp=None, ht=None):
        return self.df.loc[(self.df.date == date) | (self.df.sp == sp) | (self.df.dp == dp) | (self.df.ht == ht)]

    def to_numpy(self):
        return self.df.to_numpy()

    def get_date(self):
        return self.df['date'].dt.strftime('%d.%.m%Y %H:%M:%S').values.tolist()

# main_db = Database("C:/Users/panta/OneDrive/inf/npg/dzienniczek-cisnieniowca/data/test_db.csv")
# main_db.add_entry("16.05.2023",120,80,60)
# main_db.show()
# main_db.sort_by_date()
# main_db.show()
# main_db.sort_by_dp()
# main_db.show()
# main_db.edit_entry(0,sp=10)
# print(main_db.to_numpy())


# main_db.save("test.csv")
