from numpy import isnan
import pandas as pd
from pandas.core.dtypes.missing import isna
from pandas.tseries.offsets import DateOffset
import streamlit as st
import math
import numpy as np


df = pd.read_csv("data/AppleStore.csv")
##genre = df['prime_genre'][:200]

cats = []
values = []
genres = df['prime_genre'].unique()
i = 0
for genre in genres:
    
    for g in df['prime_genre']:
        if g == genre:
           
            if len(cats) == 0:
                
                cats = [g]
                values = [1]
            else:
                
                if cats.count(g):
                    
                    values[cats.index(g)] += 1
                else:
                    cats.append(g)
                    values.append(1)
                    

                
           
            
            i += 1

data = pd.DataFrame(values, index =cats, columns =['Categories'])
st.bar_chart(data)








