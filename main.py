import streamlit as st
import plotly.express as px
from main_backend import snatch_data

st.set_page_config(layout='centered')

# Adding the interactive components
st.write("<h1><center> BeamWeather® </center></h1>", unsafe_allow_html=True)
region = st.text_input("Region / Place")
no_of_days = st.slider("Select Number Of Days", min_value=1, max_value=5,
                       help='Slide and Adjust to premute the number of days.')
options = st.selectbox("View the Data in the format of", ('Temperature', 'Atmospheric'))

# Fixing the Grammer Issues
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

# 'name'
# 'country'
# 'population'
# 'id'
if region:
    filtered_data = snatch_data(region, no_of_days)

    if options == 'Temperature':
        temperature_data = [temps['main']['temp'] / 10 for temps in filtered_data]
        dates = [a_date['dt_txt'] for a_date in filtered_data]
        figure = px.line(x=dates, y=temperature_data,labels={"x":"Date", "y":"Temperature (C°)"})
        st.plotly_chart(figure)

    if options == 'Atmospheric':
        atmospheric_data = [atmos['weather'][0]['main'] for atmos in filtered_data]
        the_images = {"Clear": "images\\snowy.png", "Clouds": "images\\clouds.png", "Rain": "images\\rain.png",
                      "Snow": "images\\snowy.png"}
        image_paths = [the_images[the_atmosphere] for the_atmosphere in atmospheric_data]
        dates = [a_date['dt_txt'] for a_date in filtered_data]
        st.image(image_paths, width=80, caption=dates)


