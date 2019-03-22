
import pandas as pd
import numpy as np


data = pd.read_csv('~/Downloads/coursera/brasil.csv')


data_where = data.where(data['Series Code'] == 'NE.EXP.GNFS.ZS').dropna()
data_where = data.where(data['Series Code'] == 'NE.IMP.GNFS.ZS').dropna()

filter = data['Series Code']=='NE.IMP.GNFS.ZS'
filter2 = data['Series Code']=='NE.EXP.GNFS.ZS'
data_where = data.where(filter | filter2).dropna()

data_where.columns = ['Series Name', 'Series Code', 'Country Name', 'Country Code',
       '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007',
       '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015']

data_where = data_where.drop(columns=['Series Code', 'Country Name', 'Country Code'])

df = data_where.T
df = df.drop(index='Series Name')
df.columns = ['Exports', 'Imports']

import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')


df.Exports = df.Exports.astype(float)
df.Imports = df.Imports.astype(float)

df['Year'] = df.index
df.Year = df.Year.astype(int)
df['pos'] = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
df = df.set_index('pos')

ax = plt.gca()

df.plot(kind='line',x='Year',y='Imports',ax=ax, color='red')
df.plot(kind='line',x='Year',y='Exports',ax=ax, color='blue')
plt.xlabel('Year')
plt.xlim(2000, 2015)
plt.ylim(10, 18)
plt.ylabel('% of GDP')
plt.show()


