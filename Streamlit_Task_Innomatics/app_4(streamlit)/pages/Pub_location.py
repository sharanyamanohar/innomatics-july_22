import streamlit as st
import pandas as pd
import numpy as np
st.title('Pub_location')
df=pd.read_csv(r"C:\Users\Sharanya\Downloads\pub.csv")
btn_map = st.button("Display Map ")

if btn_map==True:
    st.map(df)


data_sel= df.local_authority.unique()
#choosing a local authority
optn = st.selectbox(
    'Select a Local Authority',
     data_sel)

'You selected: ', optn

#displaying the map for particular local authority
button_click= st.button('Find Now')
if button_click==True:
    res= df[df['local_authority']==optn]
    count=res.shape[0]
    st.write("Number of Pubs in this area is:",count)
    res=res[['latitude','longitude']]
    st.map(res)
    st.markdown('_Its displaying all the pubs in the area that you selected_')