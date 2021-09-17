# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 12:08:37 2021

@author: Gayathri
"""

import pandas as pd
import numpy as np
import sys




df = pd.read_excel('C:\Expenses\Sept\Expenses_Sheet.xlsx')
df['Total_Amt_Spent'] = df.loc[: , ['Gayathri', 'Manoj', 'Appa']].sum(axis=1)
print(df)
df1=df.agg({'Total_Amt_Spent': 'sum'})
print(df1)
df1.to_excel('C:\Expenses\Sept\Expenses_Sheet.xlsx',sheet_name='Output')
sys.stdout.flush()

#grp = df.groupby('Expenses_description')
#df3=grp.aggregate(np.sum)
#for Expenses_description, group in grp:
    #print(Expenses_description)
#    print(group)
#pd.DataFrame(grp).to_excel('C:\Expenses\Sept\Totalamtspent1.xlsx',sheet_name='Output')





