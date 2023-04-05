import streamlit as st
import plotly.express as px
from main_backend import snatch_data

st.set_page_config(layout='centered')

st.write("<h1><center> BeamWeather® </center></h1>", unsafe_allow_html=True)
region = st.text_input("Region / Place / Country")
no_of_days = st.slider("Select Number Of Days", min_value=1, max_value=5,
                       help='Slide and Adjust to premute the number of days.')
options = st.selectbox("View the Data in the format of", ('Temperature', 'Atmospheric'))

if region and options == 'Atmospheric':
    if no_of_days == 1:
        st.subheader(f"{options} Data for the next day in {region}")
    elif no_of_days != 1:
        st.subheader(f"{options} Data for the next {no_of_days} days in {region}")
elif region and options == 'Temperature':
    if no_of_days == 1:
        st.subheader(f"{options} for the next day in {region}")
    elif no_of_days != 1:
        st.subheader(f"{options} for the next {no_of_days} days in {region}")

snatch_data(region, no_of_days, options)

# 'name'
# 'country'
# 'population'
# 'id'

figure = px.line(labels={"x":"Date", "y":"Temperature (C°)"})
st.plotly_chart(figure)
