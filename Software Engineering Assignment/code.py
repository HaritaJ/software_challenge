import pandas as pd
import re
import sys

df = pd.read_csv('listings.csv')
df.dropna()
for apt in df['apartment_number']:
    if not isinstance(apt, str):
#         print("this is not str: ", apt)
        _ = input()
        continue
    if '-' in apt:
        apt=apt.replace('-','')
#          print(apt)
        sys.stdout.flush()


        #df['apartment_number'] = df['apartment_number'].map(lambda x: x.strip('-'))
df=df[df['apartment_number'].str.contains("/",)]
print(df[apartment_number])
