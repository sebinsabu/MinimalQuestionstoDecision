# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:45:11 2018

@author: Sebin
"""

import numpy as np
import pandas as pd

#Set the file url of csv datasheet here
df1 = pd.read_csv(r"YOUR CSV File URL HERE")
#Set the column head of features in the csv sheet here
df1 = df1.set_index('DATA')


count = 0

#limiting operation to end result of 1
while (len(df1.columns) > 1):
    
    #Sorting to find the feature with most "1" or "0"
    df3 = df1.assign(f =  df1.sum(axis=1)).sort_values('f',ascending=False)
    #decision on starting with most "0" or "1"
    choice = df3['f'].idxmin()
    
    print('Do you have an issue of',choice,'?')
    #getting user input
    user_input = eval(input())
    
    if user_input==1:
       
        print('So you have an issue of',choice)
        
        #Selecting rows with choice
        df4 = df1.loc[[choice,  ]]
        df4 = df4.T
        #finding column heads wit6h feature value inmatch with user input
        drop_colmn = df4.index[df4[choice] == 0].tolist()
        #dropping columns with columns(tests) that are not in match with user input
        df1 = df1.drop(drop_colmn,axis=1)
         #calculating the number of columns
        column_numb = len(df1.columns)
        #transposing for operations on row.
        df2 = df1.T
        
        #if(df2[choice].sum() == column_numb):
        #if all values of a feature turn 0 for all column heads,it will be dropped from further iteration
        if(df2[choice].sum() == 0):

            df1 = df1.T.drop(choice,axis = 1)
            df1 = df1.T
            print(list(df1))
            # df5 = df1[df1[choice]].squeeze()

        
            # print(df5)
            #print(df4)
        else:print(list(df1))
        
    elif user_input==0:
        
        print('So you dont have an issue of',choice)
        df4 = df1.loc[[choice,  ]]
        df4 = df4.T
       # drop_value_colhead = df4['']
        drop_colmn = df4.index[df4[choice] == 1].tolist()
        
        
        df1 = df1.drop(drop_colmn,axis=1)
        print(list(df1))
        df2 = df1.T
        column_numb = len(df1.columns)
        
        #if(df2[choice].sum() == column_numb):
        #if all values of a feature turn 0 for all column heads,it will be dropped from further iteration

        if(df2[choice].sum() == 0):
            df1 = df1.T.drop(choice,axis = 1)
#            print('before transpose')
#            print(df1)
            df1 = df1.T
#            print('elif triggered')
            print(list(df1))

    
    else:
        
        print("Invalid Entry")
        
   # count = count + 1

#print(df3)
#print(df1)
   
   #Issue
   # 1. two tests with same features can create an issue
   # 2. Only single output for now. 

