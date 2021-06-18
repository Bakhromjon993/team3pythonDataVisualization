import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


data = pd.read_csv('countries.csv')
data


print('Display the GDP per Capita of Austria')



austria = data[data.country == 'Austria']


plt.plot(austria.year, austria.gdpPerCapita)
plt.title('GDP per Capita of Austria')
plt.show()


print('Find Distribution of Data using Histograms')

set(data.continent)
data2007 = data[data.year == 2007]
asia2007 = data2007[data2007.continent == 'Asia']
europe2007 = data2007[data2007.continent == 'Europe']
len(set(asia2007.country))
len(set(europe2007.country))
asia2007.gdpPerCapita.mean()
europe2007.gdpPerCapita.mean()
asia2007.gdpPerCapita.median()
europe2007.gdpPerCapita.median()

plt.subplot(211)
plt.title('Comparing GDP of EU and Asia in 2007')
plt.hist(asia2007.gdpPerCapita, 30, edgecolor='black')
plt.ylabel('Asia')
plt.subplot(212)
plt.hist(europe2007.gdpPerCapita, 30, edgecolor='black')
plt.ylabel('Europe')
plt.show()

print('Display a time series with line charts')

us = data[data.country == 'United States']
china = data[data.country == 'China']

plt.plot(us.year, us.gdpPerCapita)
plt.plot(china.year, china.gdpPerCapita)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('GDP per capita')
plt.show()

usGrowth = us.gdpPerCapita / us.gdpPerCapita.iloc[0] * 100
chinaGrowth = china.gdpPerCapita / china.gdpPerCapita.iloc[0] * 100

plt.plot(us.year, usGrowth)
plt.plot(china.year, chinaGrowth)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('GDP growth per capita')
plt.show()

print('Display relationships in data with Scatter Plots')

plt.scatter(data2007.gdpPerCapita, data2007.lifeExpectancy)
plt.title('GDP per capita and life expectancy in 2007')
plt.xlabel('GDP per capita')
plt.ylabel('Life expectancy')
plt.show()

print('Draw a scatterplot with the base log of 10')

plt.scatter(np.log10(data2007.gdpPerCapita), data2007.lifeExpectancy)
plt.title('GDP per capita and life expectancy in 2007')
plt.xlabel('GDP per capita - log10')
plt.ylabel('Life expectancy')
plt.show()

print('Increase information displaying data for each year')
yearsSorted = sorted(set(data.year))
for aYear in yearsSorted:
    dataYear = data[data.year == aYear]
    plt.scatter(dataYear.gdpPerCapita, dataYear.lifeExpectancy, 5)
    plt.title(aYear)
    plt.xlim(0,60000)
    plt.ylim(25, 85)
    plt.xlabel('GDP per capita')
    plt.ylabel('Life expectancy')
    plt.show()

for aYear in yearsSorted:
    dataYear = data[data.year == aYear]
    plt.scatter(np.log10(dataYear.gdpPerCapita), dataYear.lifeExpectancy, 5)
    plt.title(aYear)
    plt.xlim(2,5)
    plt.ylim(25, 85)
    plt.xlabel('GDP per capita - log10')
    plt.ylabel('Life expectancy')
    plt.show()

print('Comparing data with Bar Graphs')

top10 = data2007.sort_values('population', ascending=False).head(10)
top10

x = range(10)
plt.bar(x, top10.population / 10**6)
plt.xticks(x, top10.country, rotation='vertical')
plt.title('10 most populous countries')
plt.ylabel('Population in mil')
plt.show()
