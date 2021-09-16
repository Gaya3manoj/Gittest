# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 12:08:37 2021

@author: Gayathri
"""

import pandas as pd




df = pd.read_excel('C:\Expenses\Sept\Expenses_Sheet.xlsx')
df['Total_Amt_Spent'] = df.loc[: , ['Gayathri', 'Manoj']].sum(axis=1)
print(df)
df1=df.agg({'Total_Amt_Spent': 'sum'})
print(df1)
df1.to_excel('C:\Expenses\Sept\Totalamtspent.xlsx',sheet_name='Output')





