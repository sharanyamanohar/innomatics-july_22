import streamlit as st
import pandas as pd
import numpy as np

st.title("Task - Open Pub Application")

st.header("Lets create own google maps")

st.subheader("Let’s assume you are on a vacation in the United Kingdom with your friends. Just for some fun, you decided to go to the Pubs nearby for some drinks. Google Map is down because of some issues.")
st.markdown("Create a multi page application using Streamlit with the following requirements.")


st.text("Page Number 1 - (Home Page) It should be like a welcome page. Show some basic information and statistics about the dataset.")

st.text("Page Number 2 - (Pub Locations) Display a map. Based on the Postal Code or Local Authority, display all the pubs in the area chosen. ")


st.text("Page Number 3 - (Find the nearest Pub) Ask the user to enter his/her Latitude and Longitude. Display the nearest 5 Pubs on the map. Use Euclidean Distance to find the nearest pub")


