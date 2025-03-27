import pandas as pd
import plotly.express as px

# Getting corruption data fomr (https://images.transparencycdn.org/images/CPI2024-Results-and-trends.xlsx)
fp = '/home/js/econ-hist/mapping/corruption.csv'
corruption = pd.read_csv(fp, index_col=0)

# Get all South American countries
countries = [
    'Argentina', 
    'Bolivia', 
    'Brazil', 
    'Chile', 
    'Colombia', 
    'Ecuador', 
    'Guyana', 
    'Paraguay', 
    'Peru', 
    'Suriname', 
    'Uruguay', 
    'Venezuela'
]
sa_corruption = corruption.loc[countries].sort_values(by='CPI_2024', ascending=False)

# Get Foreign Direct Investment (https://data.worldbank.org/indicator/BX.KLT.DINV.CD.WD)
fp = '/home/js/econ-hist/mapping/fdi.csv'
fdi = pd.read_csv(fp, index_col=0)
sa_fdi = fdi.loc[countries].sort_values(by='FDI_2023', ascending=False)

# Combine
data = sa_corruption.join(sa_fdi)
# Sort by FDI
data = data.sort_values(by="FDI_2023", ascending=False)
print(data)

# Create choropleth map
data = data.reset_index().rename(columns={"index": "country"})
fig = px.choropleth(
    data,
    locations="Country",
    locationmode="country names",  # or use "ISO-3" if you have country codes
    color="CPI_2024",
    color_continuous_scale="Viridis",  # Choose a color scale
    title="Country Perceived Corruption"
)

fig.update_geos(
    scope="south america",
    projection_type="mercator",  # Compact projection
    showframe=False,  # Hide borders around the map
    showcoastlines=False,  # Hide coastlines for a cleaner look
    showland=True  # Keep land visible
)

# Reduce layout margins to remove extra space
fig.update_layout(
    margin={"r":0, "t":30, "l":0, "b":0},  # Remove excess margins
    coloraxis_colorbar=dict(title="CPI Score")  # Adjust color legend title
)
fig.write_image("/home/js/econ-hist/mapping/corruption_map.png")

# Create the FDI map
fig_two = px.choropleth(
    data,
    locations="Country",
    locationmode="country names",  # or use "ISO-3" if you have country codes
    color="FDI_2023",
    color_continuous_scale="Viridis",  # Choose a color scale
    title="Country Net Foreign Direct Investment"
)

# Save as image
fig_two.update_geos(
    scope="south america",
    projection_type="mercator",  # Compact projection
    showframe=False,  # Hide borders around the map
    showcoastlines=False,  # Hide coastlines for a cleaner look
    showland=True  # Keep land visible
)

# Reduce layout margins to remove extra space
fig_two.update_layout(
    margin={"r":0, "t":30, "l":0, "b":0},  # Remove excess margins
    coloraxis_colorbar=dict(title="Net FDI")  # Adjust color legend title
)
fig_two.write_image("/home/js/econ-hist/mapping/fdi_map.png")