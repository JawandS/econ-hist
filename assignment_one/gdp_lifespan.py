# Plot a cross-section of countries comparing GDP per capita and life expectancy

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd

# Document sources
# Worldbank: https://data.worldbank.org/indicator/NY.GDP.PCAP.CD
# Worldbak: https://data.worldbank.org/indicator/SP.DYN.LE00.IN

# Load the data
gdp_data = pd.read_csv('gdp_per_capita.csv', index_col='Country Name')
lifespan_data = pd.read_csv('life_expectancy.csv', index_col='Country Name')

# get data
x_axis = gdp_data['2022'] # GDP per capita for 2022
y_axis = lifespan_data['2022'] # Life expectancy for 2022
# drop if missing either data
data = pd.DataFrame({'GDP': x_axis, 'Life Expectancy': y_axis}).dropna()
# Plot the data
plt.scatter(data['GDP'], data['Life Expectancy'], color='black')
# label United States of America
plt.text(data.loc['United States']['GDP'], data.loc['United States']['Life Expectancy'], 'United States', fontsize=9, ha='right')
plt.scatter(data.loc['United States']['GDP'], data.loc['United States']['Life Expectancy'], color='red')
# Add labels
plt.title('GDP per Capita vs Life Expectancy in 2022')
plt.xlabel('GDP per Capita (USD)')
plt.ylabel('Life Expectancy at Birth (years)')

# Save the plot
plt.savefig('gdp_lifespan.png')
