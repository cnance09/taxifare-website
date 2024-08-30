import streamlit as st
import requests
import datetime
import ast
import numpy as np
import pandas as pd

st.title('''
TaxiFareModel
''')

st.markdown('''
## 1. Tell us about your trip:
'''

'''
### Please input the parameters below
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
''')


date_pickup = st.date_input('Date of pickup: ', datetime.date.today())
time_pickup = st.time_input('Time of pickup: ', datetime.time(hour=18, minute=0))
pickup_lon = st.number_input('Pickup longitude: ', -73.950655)
pickup_lat = st.number_input('Pickup latitude: ', 40.783282)
dropoff_lon = st.number_input('Dropoff longitude: ', -73.984365)
dropoff_lat = st.number_input('Dropoff latitude: ', 40.769802)
passenger_count = st.number_input('Number of passengers: ', 1)

params = {'pickup_datetime': datetime.datetime(date_pickup.year, date_pickup.month, date_pickup.day, time_pickup.hour, time_pickup.minute),
'pickup_longitude': pickup_lon,
'pickup_latitude': pickup_lat,
'dropoff_longitude': dropoff_lon,
'dropoff_latitude': dropoff_lat,
'passenger_count': passenger_count}


st.markdown(
'''
## 2. Let's see how much this will cost! 💡
''')

url = 'https://taxifare.lewagon.ai/predict'
data = requests.get(url, params).content
data = ast.literal_eval(data.decode('utf-8'))
data = np.round(data.get('fare'),2 )
st.write('Your estimated fare is :', data)

coordinates = pd.DataFrame({'longitude': [pickup_lon, dropoff_lon], 'latitude': [pickup_lat, dropoff_lat]})
st.map(data=coordinates)
