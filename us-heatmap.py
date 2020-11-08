# US Heatmap (Confirmed Cases)

us = latest_data.loc[latest_data['Country_Region'] == 'US']
us.drop('Admin2', axis=1, inplace=True)

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

us_min = us["Confirmed"].min()
us_mean = us["Confirmed"].mean()
us_max = us["Confirmed"].max()
us_med = us["Confirmed"].median()

fig = px.choropleth_mapbox(us, geojson=counties, locations="FIPS", color='Confirmed',
                           hover_name="Province_State",
                           color_continuous_scale="OrRd",
                           range_color=(us_med,us_mean),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.4,
                           labels={'Confirmed':'Confirmed Case Number'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
