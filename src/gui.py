import streamlit as st
from main import Sensors

sensor = Sensors()
st.title(':evergreen_tree: is doing good!')
col1, col2, col3 = st.columns(3)
col1.metric(label="Air Temeprature", value=str(sensor.getSoilTemp()), delta="3")
col2.metric(label="Air Humidty", value=str(sensor.getSoilHumidity()), delta="3%")
col3.metric(label="Algae Temperature", value=str(sensor.getWaterTemp()), delta="3")
col4, col5, col6 = st.columns(3)
col4.metric(label="Algae Ph", value="30", delta="3")
col5.metric(label="Fan Status", value="On", delta="Off")
col6.metric(label="Heater Status", value="Off", delta="On")

if st.button('Toggle Fan'):
    sensor.toggleFan()
if st.button('Toggle Airpump'):
    sensor.toggleAir()
if st.button('Toggle Temp'):
    sensor.toggleTemp()
