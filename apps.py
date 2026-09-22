import streamlit as st
import joblib
import numpy as np
model = joblib.load('house_price_model.pkl')

st.title('House price prediction App')

st.divider()

st.write(
    'This app uses machine learning for predicting house prices '
    'with given features of the house. You can enter the inputs '
    'from this UI and then use the predict button.'
)

st.divider()

bedromm = st.number_input('Number of bedroom s',min_value= 0,value= 0)
bathroom = st.number_input('Number of bathrooms', min_value=0, value= 0)
Livingarea = st.number_input('Living area ',min_value=0, value=2000)
condtion = st.number_input('condtion', min_value=0,value=3)
numberofshcool = st.number_input('number of school nearby', min_value=0, value=0)

st.divider()

x = [[bedromm,bathroom,Livingarea,condtion,numberofshcool]]

prediction = st.button('predict!')

if prediction:
    st.balloons()
    x_array = np.array(x)
    prediction = model.predict(x_array)
    st.write(f'price prediction is {prediction[0]}')
else:
    st.write('please use predict button after entering values')