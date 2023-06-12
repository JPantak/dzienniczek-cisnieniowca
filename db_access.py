import pandas as pd
import os

df = pd.read_csv(os.path.join(os.getcwd(), "data/test_db.csv"))


class Database:
    """
    A class to represent the dataframe

    ...

    Attributes
    ===========
    path - path to csv file(optional) - if no path given, the class will create an empty dataframe with necessary columns
    
    Methods
    ===========
    get_entry(n) - returns the nth row of the dataframe
    add_entry(date,sp,dp,ht) - adds an entry with given arguments
    edit_entry(n,date,sp,dp,ht) - edits nth entry, all arguments beside n are optional 
    show() - prints out the dataframa associated with the class
    sort_by - sorts the dataframe by specific criteria, ascending - optional argument
    save(name,dir) - saves dataframe to csv file, dir - optional argument

    """
    def __init__(self,path=None):
        if(path != None):
            self.df = pd.read_csv(path)
            self.df["date"] = pd.to_datetime(df["date"], dayfirst=True)
        else:
            self.df = pd.DataFrame(columns=["date","sp","dp","ht"])
    def __repr__(self) -> str:
        return self.df.to_string()
    def get_entry(self, n):
        return self.df.loc[n,:]
    def edit_entry(self,n,date:str=None,sp:int =None ,dp:int =None,ht:int =None):
            if(date != None):
                self.df.at[n,"date"] = date
            if(sp != None):
                self.df.at[n,"sp"] = sp
            if(dp != None):
                self.df.at[n,"dp"] = dp
            if(ht != None):
                self.df.at[n,"ht"] = ht

    def add_entry(self,date: str,sp:int,dp:int,ht:int) -> None:
        self.df.loc[len(self.df)] = [date,sp,dp,ht]
        self.df["date"] = pd.to_datetime(self.df["date"],dayfirst=True)
    def sort_by_date(self,asc = True):
        self.df.sort_values(by="date", ascending=asc,inplace=True,ignore_index=True)
    def sort_by_sp(self,asc = True):
        self.df.sort_values(by="sp", ascending=asc,inplace=True,ignore_index=True)
    def sort_by_dp(self,asc = True):
        self.df.sort_values(by="dp", ascending=asc,inplace=True,ignore_index=True)
    def sort_by_ht(self,asc = True):
        self.df.sort_values(by="ht", ascending=asc,inplace=True,ignore_index=True)
    def save(self,path):
        self.df.to_csv(path,index=False)
    def print(self):
        print(self.df)


# main_db = Database("C:/Users/panta/OneDrive/inf/npg/dzienniczek-cisnieniowca/data/test_db.csv")
# main_db.add_entry("16.05.2023",120,80,60)
# main_db.show()
# main_db.sort_by_date()
# main_db.show()
# main_db.sort_by_dp()
# main_db.show()
# main_db.edit_entry(0,sp=10)
# print(main_db)


# main_db.save("test.csv")