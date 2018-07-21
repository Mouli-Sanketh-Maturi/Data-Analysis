import pandas as pd
import numpy as np
import os
import time
print "Reading the input file .. .. .."
df = pd.read_csv('Consumer_Complaints.csv')
os.system('cls')
print "Done .."
print "Filtering and deleting unecessary data"
del df['Consumer complaint narrative']
del df['Sub-product']
del df['Sub-issue']
del df['ZIP code']
del df['Tags']
time.sleep(5)
os.system('cls')
print "Modifying Data ..."
df['DateReceived']=pd.to_datetime(df['DateReceived'])
df['DateSent']=pd.to_datetime(df['DateSent'])
df['Time']=(df.DateSent-df.DateReceived)
print "This is taking longet than expected....please wait for some more time.."
df['Month'] = df.DateReceived.dt.month
df['Day'] = df.DateReceived.dt.weekday_name
df['Year'] = df.DateReceived.dt.year
os.system('cls')
print "Exporting File ..."
df.to_csv('modified.csv')
os.system('cls')
print "Exiting the program"
time.sleep(10)
