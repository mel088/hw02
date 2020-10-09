import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#file_name='/Users/melaniewilliamsmac/Documents/GitHub/mel088.github.io/.vscode/hw02/data.csv'

df=pd.read_csv("/Users/melaniewilliamsmac/Documents/GitHub/mel088.github.io/hw02/data2.csv")
print(df.head(7))
dfh=df.head(7)
df_sorted=dfh.sort_values(by=['Year'])
dfa=df.iloc[81:88]
df_sorteda=dfa.sort_values(by=['Year'])
plt.plot('Year', 'Value', data=df_sorteda, color='blue', label="North America", linewidth=4)
plt.plot('Year', 'Value', data=df_sorted, color='#addd', label="Global", linewidth=7)

plt.title('Energy Production, Trade, and Suppy')
plt.xlabel('Year')
plt.ylabel('Value of Energy Production, Trade, and Suppy')
plt.legend(loc="upper left")
plt.show()

df=pd.read_csv("/Users/melaniewilliamsmac/Documents/GitHub/mel088.github.io/hw02/data3.csv")
print(df.head(8))
dfh=df.head(8)
df_sorted=dfh.sort_values(by=['Year'])
#dfa=df.iloc[81:88]
#df_sorteda=dfa.sort_values(by=['Year'])
plt.bar('Year', 'Value', data=df_sorted, color='dimgray', label="Global", linewidth=5)
#plt.plot('Year', 'Value', data=df_sorted, color='#addd', label="Global", linewidth=7)
plt.title('Worldwide Carbon Dioxide Emissions')
plt.xlabel('Year')
plt.ylabel('Emissions (thousand metric tons of carbon dioxide)')
plt.yticks(ticks=[0,3,6], labels=['16,000,000','26,000,000','36,000,000'])
#plt.legend(loc="upper left")
plt.show()
