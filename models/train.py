import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras. layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load models

df=pd.read_csv(/workspaces/customer-churn-dl-project/data/bank_churn_data - bank_churn_data.csv)
x=df.drop(['customerId','surname','Exited'],axis=1)
y=df['Exited']