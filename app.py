import streamlit as st
import requests
from datetime import datetime

# st.title makes a title
st.title('Taxi Fare Prediction')

# st.markdown makes a sub header
st.markdown('''
## Input ride details:
''')

# so st.something_input allows for a input with the label then the current value to display
date = st.date_input('Date', datetime.today())
time = st.time_input('Time', datetime.now().time())
pickup_longitude = st.number_input('Pickup Longitude', value=-73.985428)
pickup_latitude = st.number_input('Pickup Latitude', value=40.748817)
dropoff_longitude = st.number_input('Dropoff Longitude', value=-73.985428)
dropoff_latitude = st.number_input('Dropoff Latitude', value=40.748817)
passenger_count = st.number_input('Passenger Count', min_value=1, max_value=8, value=1)

# button with with label in the () then code to run when clickes whiches sends a reqiest to the API
if st.button('Get Fare Prediction'):
    url = 'https://taxifare.lewagon.ai/predict'
    params = {
        'pickup_datetime': f'{date} {time}',
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }
    response = requests.get(url, params=params)
    prediction = response.json()
    st.write(f'Predicted Fare: ${prediction["fare"]:.2f}')

