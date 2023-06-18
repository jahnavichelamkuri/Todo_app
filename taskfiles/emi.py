import streamlit as st
import requests
import pandas as pd
import altair as alt
import numpy as np

np.random.seed(42)
arr_random = np.random.randint(low=0, high=100, size=(100,3)) 

emi_list =[]
customer_list =[]



if st.button('GET'):

    get_method=requests.get('http://127.0.0.1:8000/index/')
    if get_method.status_code==200:
        data=get_method.json()
        for item in data:
            emi_list.append(item['EMI_paid_on_time'])
            customer_list.append(item['total_customers'])
    else:
        st.write(get_method.status_code)

   
source = pd.DataFrame({
    'EMI Paid On Time': emi_list,
    'Number of customers': customer_list
 })

user_colour = st.color_picker(label='Choose a colour for your plot')

bar_chart = alt.Chart(source).mark_bar().encode(
    x='EMI Paid On Time:O',
    y='Number of customers:Q',
    c=user_colour,
)

st.altair_chart(bar_chart, use_container_width=True)
