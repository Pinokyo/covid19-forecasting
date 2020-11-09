train = pd.read_csv("/kaggle/input/covid19-global-forecasting-week-5/train.csv")
test = pd.read_csv("/kaggle/input/covid19-global-forecasting-week-5/test.csv")

train_copy = train.copy()
test_copy = test.copy()

train['day']=pd.to_datetime(train.Date,format='%Y-%m-%d').dt.day
train['month']=pd.to_datetime(train.Date,format='%Y-%m-%d').dt.month

test['day']=pd.to_datetime(test.Date,format='%Y-%m-%d').dt.day
test['month']=pd.to_datetime(test.Date,format='%Y-%m-%d').dt.month

train.columns = map(str.lower, train.columns)
train = train.rename(columns = {'county': 'country', 'province_state': 'state', 'country_region': 'region', 'target': 'case', 'targetvalue':'case_value'}, inplace = False)

tc_data = pd.read_csv("../input/number-of-cases-in-the-city-covid19-turkey/number_of_cases_in_the_city.csv")


'''Top 5 Cities with the Highest Number of Cases'''

tc_list = list(range(1, 82))
tc_data.insert(0, "id", tc_list, True) 

import plotly.express as px

more_case = tc_data.sort_values(by='Number of Case', ascending=False)

fig = px.pie(
    more_case.head(5),
    values = "Number of Case",
    names = "Province",
    color_discrete_sequence = px.colors.sequential.RdBu)

fig.update_traces(textposition="inside", textinfo="percent+label")
fig.show()

'''Turkey Heatmap (Number of Case)'''

import plotly.express as px

# loading Turkey's geoplot json file
from urllib.request import urlopen
import json
with open("../input/geoplot/tr-cities-utf8.json") as f:
    cities = json.load(f)

mini = tc_data["Number of Case"].min()
average = tc_data["Number of Case"].mean()
#tc_data.drop('id', axis=1, inplace=True)
    
fig = px.choropleth_mapbox(tc_data, geojson=cities, locations=tc_data.id, color=(tc_data["Number of Case"]),
                           hover_name="Province",
                           range_color= (mini,average),
                           color_continuous_scale='amp',
                           mapbox_style="carto-positron",
                           zoom=4, opacity=0.7,center = {"lat": 38.963745, "lon": 35.243322},
                           labels={'color':'Number of Case'})

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

'''10 Cities with the Lowest Number of Cases'''

less_case = tc_data.sort_values(by='Number of Case', ascending=True)

fig = px.bar(
    less_case.head(10),
    x = "Province",
    y = "Number of Case")
fig.update_layout(barmode="group")
fig.update_traces(marker_color='rosybrown')
fig.show()

'''Fatalities vs Confirmed Cases'''

import matplotlib as mpl

tc = train.loc[train.region == 'Turkey']

tc.drop('country', axis=1, inplace=True)
tc.drop('state', axis=1, inplace=True)
tc.drop('region', axis=1, inplace=True)
tc.drop('population', axis=1, inplace=True)

tc_1=tc['case_value'].groupby(tc['case']).sum()

fatal_tc=tc[tc['case']=='Fatalities']
conf_tc=tc[tc['case']=='ConfirmedCases']

labels =[tc_1.index[0],tc_1.index[1]]
sizes = [tc_1[0],tc_1[1]]
explode = (0, 0.08)  
plt.figure(figsize = (8,8))

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',textprops={'fontsize': 14},startangle=90)
plt.show()
