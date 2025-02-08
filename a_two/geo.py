# Looking at the relationship between the locaiton and wealth of countries

# Imports
import pandas as pd

# Get capital locs
url = 'https://gist.githubusercontent.com/ofou/df09a6834a8421b4f376c875194915c9/raw/355eb56e164ddc3cd1a9467c524422cb674e71a9/country-capital-lat-long-population.csv'
countries = pd.read_csv(url)[['Country', 'Latitude', 'Longitude']].dropna()
print(f"Total countries: {len(countries)}")

# Get market capitilizations
second_url = 'https://databank.worldbank.org/reports.aspx?country=&series=CM.MKT.LCAP.GD.ZS&source=2#'
electricity = pd.read_csv('/home/js/econ-hist/a_two/market-cap.csv')[['Country Name', '2022 [YR2022]']].dropna()
# Rename Country Name to Country
electricity = electricity.rename(columns={'Country Name': 'Country'}).rename(columns={'2022 [YR2022]': 'Electricity'})
# remove non numeric values
electricity = electricity[electricity['Electricity'] != '..']
print(f"Data points: {len(electricity)}")

# print("Missing countries:")
# for country in electricity['Country']:
#     if country not in countries['Country'].values:
#         print(country)

print("Missing data:")
for country in countries['Country']:
    if country not in electricity['Country'].values:
        print(country)

# Merge the data
# data = countries.merge(market_cap, on='Country')
# drop rows with any missing values
# data = data.dropna()
# print(len(data))
