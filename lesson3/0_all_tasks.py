import pandas as pd
from datetime import datetime
from geopy import distance

df = pd.read_csv('stops.csv',sep=';', comment='#')
print(f"number of bus stops {len(df)}")
street_stat = df.groupby('Street')['global_id'].agg('nunique')
print(f'The most popular street is {street_stat.idxmax()}')
print('top three streets are')
for index, values in street_stat.nlargest(3).items():
    print(index, values)

df = pd.read_csv('metro.csv', sep = ';')
def date_check(x, dt):
    list_of_date = x.split('-')
    if datetime.strptime(dt, '%d.%m.%Y') >= datetime.strptime(list_of_date[0], '%d.%m.%Y') and datetime.strptime(dt, '%d.%m.%Y') <= datetime.strptime(list_of_date[1], '%d.%m.%Y'):
        return 1
    else:
        return 0
df = df[~df.RepairOfEscalators.isna()][['NameOfStation','Line','RepairOfEscalators']].reset_index(drop = True)
df['is_station_repairing_now'] = df.apply(lambda x: date_check(x.RepairOfEscalators, '21.09.2019'), axis = 1)

repairing_stations = df[df.is_station_repairing_now == 1]
if len(repairing_stations) > 0:
    for station in repairing_stations:
        print(station.NameOfStation)
else:
    print('there are no stations')
    

stops = pd.read_csv('stops.csv',sep=';', comment='#')
metro = pd.read_csv('metro.csv', sep = ';')
stops_list = stops[[ 'Longitude_WGS84','Latitude_WGS84']].values

def get_stops(lon, lat, list_to_check_with):
    metro =[lon,lat]
    counter = 0
    for i in list_to_check_with:
        if distance.great_circle(metro, i).km <= 0.5:
            counter += 1
    return counter

metro['number_of_stops'] = metro.apply(lambda x: get_stops(x.Longitude_WGS84, x.Latitude_WGS84, stops_list), axis=1)
top_metro_station = metro.sort_values('number_of_stops', ascending=False).reset_index(drop = True).NameOfStation[0]
print(f"The largest number of busstops is near {top_metro_station}")