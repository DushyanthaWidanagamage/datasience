import pandas
import matplotlib.pyplot as pl
import pandas
from pandas.plotting import scatter_matrix

names = ['Course-Catagory','stream-catagory','result-scale','future-succes']
data = pandas.read_csv('Student.csv')

data.info()

data.shape

grouped = data.groupby(['result-scale','future-succes'])
size = grouped.size()
size.plot(kind='bar',figsize=(10,10))

grouped1 = data.groupby(['Course-Catagory','future-succes'])
size1 = grouped1.size()
size.plot(kind='bar',figsize=(10,10))

grouped2 = data.groupby(['stream-catagory','future-succes'])
size2 = grouped.size()
size2.plot(kind='bar',figsize=(10,10))
