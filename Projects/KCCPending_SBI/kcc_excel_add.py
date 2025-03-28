import pandas as pd


data=pd.read_excel('E:\Personal_Development\Personal_Development\Projects\KCCPending_SBI\lclat.xlsx',sheet_name='Sheet1')

data['DataAdded']='no';

data.to_excel('E:\Personal_Development\Personal_Development\Projects\KCCPending_SBI\lclat2.xlsx',sheet_name='Sheet1',index=False)