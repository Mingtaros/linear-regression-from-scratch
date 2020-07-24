import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cardata=pd.read_csv(r'car_details.csv')

print(cardata.head())
print(cardata.isnull().sum())
print(cardata.describe())

# cardata['CarName']=cardata['CarName'].apply(lambda name: name.split()[0])
# cardata.rename(index=str,columns={'CarName':'Company'},inplace=True)
# cardata['total_mpg']=(55*cardata['citympg']/100)+(45*cardata['highwaympg']/100)
# cardata.drop(['car_ID','citympg','highwaympg'],axis=1,inplace=True)
# cardata.symboling=cardata.symboling.astype(str)

cardata.head()

# cardata.Company.unique()