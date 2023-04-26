import pickle
import streamlit as st

model = pickle.load(open('estimasi_gizi.sav', 'rb'))

st.title('Estimasi Jumlah Kandungan Gizi dalam Air')

Carbohydrt = st.number_input('Input Karbohidrat (g)')
Calcium  = st.number_input('Input jumlah kalsium (mg)')
Cholestrl = st.number_input('Input Total Kolesterol (mg)')
Sodium  = st.number_input('Input Jumlah Sodium (mg)')
Zinc  = st.number_input('Input Total Zinc')

predict = ''

if st.button('Estimasi'):
    predict = model.predict(
        [[Carbohydrt, Calcium, Cholestrl, Sodium, Zinc]]
    )
    st.write ('Estimasi Kandungan gizi dalam air(g): ', predict)