# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:32:31 2019

@author: icecream boi
"""


#df = pd.read_csv(r'H:\1_Projects\biotech\DAM 1 bin\CTRL -2.txt', sep='\t', header=None, index_col=0)
"""
df['datetime'] = df.iloc[:, 0] + ' ' + df.iloc[:, 1]
df['datetime'] = pd.to_datetime(df['datetime'])
df = df.set_index(df['datetime'])
df.drop(df.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 29]], axis = 1, inplace = True) 
df = df.drop(columns=['datetime'])
df.columns = list(range(0,31))
#df1_10 = df.iloc[:, 0:10].sum(axis=1)
#df11_21 = df.iloc[:, 11:21].sum(axis=1)
#df22_31 = df.iloc[:, 21:31].sum(axis=1)
#df = pd.concat([df1_10, df11_21, df22_31], axis=1)
#df.plot(kind='line') 
#df = df.resample('H').sum()
"""
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_excel(r'H:\1_Projects\biotech\franka_new\results_2/franka_data_all.xlsx')
df.drop(df.columns[[19, 21, 22, 23, 24, 25, 26, 30, 34]], axis = 1, inplace = True) 

df = df[df.name.str.contains('^C')]
#visak columna, brisanje
df = df.drop(['Unnamed: 0', 'monitor_status'], axis=1)
df = df.groupby(['datetime']).mean()
#df = df.resample('H').mean()
#df.drop(df.columns[[15, 17, 18, 19, 20, 21, 22, 26, 30]], axis = 1, inplace = True) 
columns = list(range(1, 24))
df.columns = columns

df = df.T

from sklearn.preprocessing import StandardScaler

features = list(df.columns)
# Separating out the features
x = df.loc[:, features].values
df['target'] = df.index 
# Separating out the target
y = df.loc[:,['target']].values
# Standardizing the features
x = StandardScaler().fit_transform(x)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data = principalComponents
                           , columns = ['principal component 1',
                                        'principal component 2'])

finalDf = pd.concat([principalDf, df[['target']]], axis = 1)
Type_new = pd.Series([]) 
for i in range(len(finalDf)): 
    if finalDf["target"][i] < 11: 
        Type_new[i]="skupina 0-10"
  
    elif finalDf["target"][i] < 21: 
        Type_new[i]="skupina10-20"
  
    else: 
        Type_new[i]= 'skupina20-32'

del finalDf['target']
finalDf.insert(2, "target", Type_new) 

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['skupina 0-10', 'skupina10-20', 'skupina20-32']
colors = ['r', 'g', 'b']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()