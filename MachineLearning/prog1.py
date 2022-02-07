import pandas as pd 
import numpy as np
from pandas.core import base 
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px 

base_credit = pd.read_csv('credit_data.csv') 
print(base_credit)
print(base_credit.head(10))
print(base_credit.tail(10)) 
print(base_credit.describe()) 
print(base_credit[base_credit['income'] >= 69995.6855])
print(base_credit[base_credit['loan'] <= 1.377630])