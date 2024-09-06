import streamlit as st
import numpy as np

def salary_model(experience):
    st.write('Model under progress , but please give a raise to your employee because he/she having ', experience,' years of experience')

def diamond_model(weight):
    st.write('Model under progress , but diamonds are really priceless')

st.title(":keycap_star: Machine Learning Models :keycap_star: ")
tab1, tab2 , tab3 = st.tabs(["Regressions","Classifications", "Clusterings"])
with tab1:
    text1 = '<p style="font-size: 20px;"> Here are all the Pretrained Regression models. </p>'
    text2 = '<p style="font-size: 20px;"> Please Choose any model and proceed.</p>'
    st.markdown(text1, unsafe_allow_html=True)
    st.markdown(text2, unsafe_allow_html=True)
    col1 , col2 = st.columns([1,2])
    with col1:
        st.markdown("<h3 style = 'text-align:center;'> Model</h3>", unsafe_allow_html=True)

    with col2:
        models = ['Salary Prediction' , 'Diamond Price Prediction']
        global selected_model
        selected_model = st.selectbox('Select a model', models)
    if selected_model == 'Salary Prediction':
        experience = st.slider('Select Experience of Employee in Years',0,40)
        if st.button('Submit'):
            salary_model(experience)
    elif selected_model == 'Diamond Price Prediction':
        weight = st.slider('Enter Weight of Diamond in gms',0,50)
        if st.button('Submit'):
            diamond_model(weight)
