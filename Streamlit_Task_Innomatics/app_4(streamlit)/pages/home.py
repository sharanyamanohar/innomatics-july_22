import streamlit as st
import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\Sharanya\Downloads\pub.csv")
st.header("Lets move on to the pub!And have a fun!!")



st.text("The data describes UK pub names along with their addresses, postalcode,Latitude,longitude,easting,northing, and local authority.")
df[['latitude', 'longitude']]=df[['latitude', 'longitude']].apply(pd.to_numeric, axis = 1)
data_sel= df.local_authority.unique()
pub= "Total number of PUBS: "+str(df.shape[0])
auth="Total number of PUBS Local Authority: " +str(data_sel.shape[0])
latitude_range= "Latitude Range of Data: "+str(df['latitude'].min())+" to "+str(df['latitude'].max())
longitude_range= "Longitude Range of Data: "+str(df['longitude'].min())+" to "+str(df['longitude'].max())
st.dataframe(df.head())
st.subheader('Here are the statistics information of the pub dataset')
stat = st.button('Describe')

if stat==True:
    st.dataframe(df.describe())
else:
    st.text('')

st.subheader(pub)
st.subheader(auth)
st.subheader(latitude_range)
st.subheader(longitude_range)