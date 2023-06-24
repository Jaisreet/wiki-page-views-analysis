import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv('pagecounts-20190509-120000.txt', sep=' ', header=None, index_col=1,
        names=['lang', 'page', 'views', 'bytes'])

sorted_data = data1.sort_values('views', ascending=False)

data2 = pd.read_csv('pagecounts-20190509-130000.txt', sep=' ', header=None, index_col=1,
        names=['lang', 'page', 'views', 'bytes'])

combined_data = pd.DataFrame({'Data 1': data1['views'], 'Data 2': data2['views']})


plt.figure(figsize=(10, 5)) 
plt.subplot(1, 2, 1) 
plt.plot(sorted_data['views'].values) 
plt.title('Popularity Distribution')
plt.ylabel('Views')
plt.xlabel('Rank')
plt.subplot(1, 2, 2) 
# build plot 2
plt.scatter(combined_data['Data 1'], combined_data['Data 2'])
plt.title('Hourly Correlation')
plt.xlabel('Hour 2 ')
plt.ylabel('Data 2')
plt.xscale('log')
plt.yscale('log')

plt.savefig('wikipedia.png')






