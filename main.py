import streamlit as st
import plotly.express as px

st.set_page_config(layout='centered')

st.write("<h1><center> BeamWeather® </center></h1>", unsafe_allow_html=True)
region = st.text_input("Region")
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

def get_data(the_days):
    date = ['2022-25-10', '2022-26-10', '2022-27-10']
    temperatures = [10, 11, 15]
    dynamic_temp = [the_days * i for i in temperatures]
    return date, dynamic_temp

dates, dy_temps = get_data(no_of_days)

figure = px.line(x=dates, y=dy_temps, labels={"x":"Date", "y":"Temperature (C°)"})
st.plotly_chart(figure)