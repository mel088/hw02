import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#file_name='/Users/melaniewilliamsmac/Documents/GitHub/mel088.github.io/.vscode/hw02/data.csv'

df=pd.read_csv("/Users/melaniewilliamsmac/Documents/GitHub/mel088.github.io/.vscode/hw02/data.csv")
print(df.head())
df_sorted=df.sort_values(by=['Year'])
plt.scatter('Year', 'Value', data=df_sorted, color='pink', label="scatter plot", linewidth=.5, marker=r'$\heartsuit$')
plt.xlabel('Year')
plt.yticks((0, 200, 404))
#plt.yticks([])
plt.title('Average Number of Threatened Species by Location over 15 Years')
plt.ylabel('Average Number of Threatened Species by Location')
plt.show()

#x1 = [2004, 2000, 2010, 2017]
#y1 = [0.8,1, 1, 8]
#plt.plot(x1, y1, label = "line 1", linewidth=4)
'''
plt.plot('Year', 'Value', data=df_sorted, color='#ddaf', linewidth=2)
plt.xlabel('Year')
plt.title('Average Number of Threatened Species by Location over 15 Years')
plt.ylabel('Average Number of Threatened Species by Location')
plt.yticks((0, 200, 404))
x1 = [2004, 2008, 2015, 2019]
y1 = [30,100, 300, 500]
plt.plot(x1, y1, label = "Trend", linewidth=4, color='green')
plt.legend(loc="upper left")
plt.show()
'''
