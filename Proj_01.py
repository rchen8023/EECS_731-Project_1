
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('Data/2018.csv')
data2 = pd.read_csv('Data/drinks.csv')

data1 = data1.rename(columns = {'Country or region': 'country'}, inplace = False)
data1 = data1.sort_values(by ='country' , ascending=True)

data = pd.merge(data1,data2, on='country')
data = data.dropna()

ax1 = data.plot.scatter(x='Score', y='beer_servings', color='DarkBlue', label='beer');
data.plot.scatter(x='Score', y='spirit_servings', color='DarkGreen', label='spirit', ax=ax1);
data.plot.scatter(x='Score', y='wine_servings', color='Red', label='wine', ax=ax1);

data.plot.scatter(x='GDP per capita', y='spirit_servings')
data.plot.scatter(x='GDP per capita', y='beer_servings')
data.plot.scatter(x='GDP per capita', y='wine_servings')

data.plot.scatter(x='Healthy life expectancy', y='beer_servings')
data.plot.scatter(x='Healthy life expectancy', y='spirit_servings')
data.plot.scatter(x='Healthy life expectancy', y='wine_servings')

data.plot.scatter(x='GDP per capita', y='Score')