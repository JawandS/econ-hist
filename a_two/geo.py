# Looking at the relationship between the locaiton and wealth of countries

# Imports
import pandas as pd
import matplotlib.pyplot as plt

# Get capital locs
url = 'https://gist.githubusercontent.com/ofou/df09a6834a8421b4f376c875194915c9/raw/355eb56e164ddc3cd1a9467c524422cb674e71a9/country-capital-lat-long-population.csv'
countries = pd.read_csv(url)[['Country', 'Latitude', 'Longitude']].dropna()
print(f"Total countries: {len(countries)}")

# Get market capitilizations
second_url = 'https://databank.worldbank.org/reports.aspx?country=&series=CM.MKT.LCAP.GD.ZS&source=2#'
electricity = pd.read_csv('/home/js/econ-hist/a_two/electricity.csv')[['Country Name', '2022 [YR2022]']].dropna()
# Rename Country Name to Country
electricity = electricity.rename(columns={'Country Name': 'Country'}).rename(columns={'2022 [YR2022]': 'Electricity'})
# remove non numeric values
electricity = electricity[electricity['Electricity'] != '..']
# Make numeric
electricity['Electricity'] = electricity['Electricity'].astype(float)
print(f"Data points: {len(electricity)}")

# Merge the data
data = countries.merge(electricity, on='Country')
# drop rows with any missing values
data = data.dropna()
print(f"Total data: {len(data)}")

# Graph electicity vs latitude
plt.scatter(data['Latitude'], data['Electricity'])
plt.xlabel('Latitude of Country Capital')
plt.ylabel('Access to Electricty (% of population)') 
plt.title('Prevalence of Electricity vs Latitude')
plt.savefig('/home/js/econ-hist/a_two/lat_elec.png')
plt.close()

# Graph electicity vs longitude
plt.scatter(data['Longitude'], data['Electricity'])
plt.xlabel('Longitude of Country Capital')
plt.ylabel('Access to Electricity (% of population)')
plt.title('Prevalence of Electricity vs Longitude')
plt.savefig('/home/js/econ-hist/a_two/long_elec.png')
plt.close()

# Graph each point by lat/long with color intensity by electricity (red to green)
plt.scatter(data['Longitude'], data['Latitude'], c=data['Electricity'], cmap='RdYlGn')
plt.xlabel('Longitude of Country Capital')
plt.ylabel('Latitude of Country Capital')
# Set y axis to -90/90
plt.ylim(-90, 90)
# Set x axis to -180/180
plt.xlim(-180, 180)
plt.title('Location of Country Capital vs Electricity')
plt.colorbar()
plt.savefig('/home/js/econ-hist/a_two/lat_long_elec.png')
plt.close()
