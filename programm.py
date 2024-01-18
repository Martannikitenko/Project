import pandas as pd
import numpy as nm 
import matplotlib.pyplot as plt
import tabulate

#Ielasam CSV
df = pd.read_csv("kontaparskats.csv", sep = ";", decimal = ",")
df['KATEGORIJA'] = ''
#print(df.head(5))

# Definējam kategoriju atslegvardus kategorijām
ObligaatieMaksajumi = ['SEB','TET','LATVIJAS MOBILAIS','LATVENERGO','SAIMNIEKS','TUKUMA NOVADA']
Degviela = ['CIRCLE','NESTE','KOOL']
Partika = ['RIMI','MAXIMA','ELVI','CITRO','TOP','Karotes','ORANGE','FOOD']
BrivaisLaiks = ['Karotes','ORANGE','FOOD','MCDON','CAFFE','AUZINA']

for i in range(len(df)):
    Partneris = df.iloc[i, 3].upper()
    df.iloc[i, 7] = 'Citi izdevumi'

    # Obliegātie maksājumi
    flag=0
    for key in ObligaatieMaksajumi:
        if(Partneris.find(key)!=-1):
            flag+=1
    if flag>0:
        df.iloc[i, 7] = 'Obligātie maksājumi'
    
    # Degviela
    flag=0
    for key in Degviela:
        if(Partneris.find(key)!=-1):
            flag+=1
    if flag>0:
        df.iloc[i, 7] = 'Degviela'
    
    # Pārtika
    flag=0
    for key in Partika:
        if(Partneris.find(key)!=-1):
            flag+=1
    if flag>0:
        df.iloc[i, 7] = 'Pārtika'
    
    # Brīvais laiks
    flag=0
    for key in BrivaisLaiks:
        if(Partneris.find(key)!=-1):
            flag+=1
    if flag>0:
        df.iloc[i, 7] = 'Brīvais laiks'

df_class = df[['KATEGORIJA','SUMMA']]
df2 = df_class.groupby('KATEGORIJA').sum()

#Apkopojums
print('Summārie izdevumi periodā ir : {0} EUR\n\n'.format(df2['SUMMA'].sum()))
print('Izdevumi pa kategorijām\n')
print(df2.to_markdown()+'\n')

#Kūka diagramma
y = df2['SUMMA'].to_numpy() 
labels = ['Brīvais laiks','Citi izdevumi','Degviela','Obligātie maksājumi','Pārtika']

plt.pie(y, labels = labels)
plt.legend()
plt.savefig('Pie.png')