import pandas as pd
import os

df = pd.read_csv(os.path.join(os.getcwd(), "data/test_db.csv"))


class Database:
    def __init__(self,df):
        self.df = df
        self.df["date"] = pd.to_datetime(df["date"],dayfirst=True)
    def get_entry(self, n):
        return df.loc[n,:]
    def add_entry(self,df,date: str,sp:int,dp:int,ht:int) -> None:
        df.loc[len(df)] = [date,sp,dp,ht]
        self.df["date"] = pd.to_datetime(df["date"],dayfirst=True)
    def show(self):
        print(df)
    def sort_by_date(self,asc = True):
        df.sort_values(by="date", ascending=asc,inplace=True,ignore_index=True)

main_db = Database(df)

main_db.add_entry(df,"16.05.2023",120,80,60)
main_db.show()
main_db.sort_by_date()
main_db.show()
