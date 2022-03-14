<<<<<<< HEAD
from email.policy import default
=======
>>>>>>> a1cd72bf3d811c83b45954e343cfcfd628e3943f
import pandas as pd 
import numpy as np
from pandas.core import base 
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px 
<<<<<<< HEAD
from sklearn.preprocessing import StandardScaler

base_credit = pd.read_csv('/home/mnetto/Documents/Python/credit_data.csv') 
print(base_credit) 
#VISUALIZAR OS 10 PRIMEIROS REGISTROS
print(base_credit.head(10))  
#VIZUALIZAR OS 10 ULTIMOS REGISTROS
print(base_credit.tail(10))
#RETORNA CONTAGEM/MEDIA/MIN/MAX... 
print(base_credit.describe())  
#BUSCANDO DADOS ESPECIFICOS 
print(base_credit[base_credit['income']>=69995.685578])
print(base_credit[base_credit['loan']<=1.377630])
#CONTANDO OS VALORES UNICOS DE UMA COLUNA 
print(np.unique(base_credit['default'], return_counts=True)) 
#PLOTANDO O GRAFICO DOS VALORES DE DEFAULT 
sns.countplot(x= base_credit['default'])  
plt.show()
#FAZENDO UM HISTOGRAMA PARA IDADE 
plt.hist(x=base_credit['age']) 
plt.show() 
#HISTOGRAMA PARA RENDA 
plt.hist(x=base_credit['income'])
plt.show()
#HISTOGRAMA PARA DIVIDA 
plt.hist(x=base_credit['loan']) 
plt.show() 
#CRIANDO UM GRAFICO DINAMICO 
grafico = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color = 'default') 
grafico.show() 
#LOCALIZANDO VALORES INCONSISTENTES 
print(base_credit.loc[base_credit['age']<0]) 
#OU 
print(base_credit[base_credit['age']<0]) 
#APAGANDO TODA A COLUNA 
base_credit2 = base_credit.drop('age', axis=1) 
print(base_credit2)
#APAGANDO SOMENTE OS REGISTROS INCONSISTENTES 
base_credit3 = base_credit.drop(base_credit[base_credit['age']<0].index) 
print(base_credit3) 
#PREENCHENDO OS VALORES INCONSISTENTES COM A MEDIA  
base_credit4 = base_credit
print(base_credit.mean())#media de toda a tabela 
print(base_credit['age'].mean())#media da idade 
print(base_credit['age'][base_credit['age']<0].mean)#mediada indade sem os outlines 
base_credit4.loc[base_credit4['age']<0, 'age'] = 40.92 
#REFAZENDO OS GRAFICOS DINAMICOS 
grafico2 = px.scatter_matrix(base_credit4, dimensions=['age', 'income', 'loan'], color = 'default') 
grafico2.show() 
#TRATAMENTO DOS VALORES FALTANTES  
print(base_credit4.isnull())#printa a tabela com false e true 
print(base_credit4.isnull().sum())#Cota os valores nulos de cada coluna 
print(base_credit4.loc[pd.isnull(base_credit4['age'])])#pega as linhas que tem valor nulo na idade 
base_credit4['age'].fillna(base_credit4['age'].mean(), inplace=True)#preenche os valores nulos com a média  
print(base_credit4.loc[(base_credit4['clientid']==29)|(base_credit4['clientid']==31)|(base_credit4['clientid']==32)])#pega as linhas dos ids
#outra forma 
print(base_credit4.loc[base_credit4['clientid'].isin([29,31,32])])
#DIVISÃO ENTRE PREVISORES E CLASSE  
x_credit = base_credit4.iloc[:, 1:4].values #previsores obs.:Ele pega do 1 ao 3, o ':' pega toda a coluna, ou seja todas as linhas das culunas 1, 2 e 3   
y_credit = base_credit4.iloc[:,4]#CLASSE  
#ESCALONAMENTO DOS VALORES  
print(x_credit[:,0])#pega todos os valores da coluna 0 
print(x_credit[:,0].min())#pega o valor mínimo da coluna
print(x_credit[:,0].max())#pega o valor máximo da coluna 
print(x_credit[:,0].min(),x_credit[:,1].min(),x_credit[:,2].min())#valor minimo de todas as colunas 
print(x_credit[:,0].max(),x_credit[:,1].max(),x_credit[:,2].max())#valor maximo de todas as clunas 
scaler_credit = StandardScaler() 
x_credit = scaler_credit.fit_transform(x_credit)#colocando na mesma escala através da padronização 
print(x_credit)
print(x_credit[:,0].min(),x_credit[:,1].min(),x_credit[:,2].min())
print(x_credit[:,0].max(),x_credit[:,1].max(),x_credit[:,2].max())
=======

base_credit = pd.read_csv('credit_data.csv') 
print(base_credit)
print(base_credit.head(10))
print(base_credit.tail(10)) 
print(base_credit.describe()) 
print(base_credit[base_credit['income'] >= 69995.6855])
print(base_credit[base_credit['loan'] <= 1.377630])
>>>>>>> a1cd72bf3d811c83b45954e343cfcfd628e3943f
