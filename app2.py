import streamlit as st
from PIL import Image

st.title("BMI Calculator App")

w = st.number_input("What is your weight in KG")
h = st.number_input("What is your height in metres")

def bmi_calc(w,h):
    bmi = round(w/(h**2),1)
    
    if bmi > 29.9:
        rating = 'are at risk of being obese, take care'
    elif 24.9 < bmi < 30:
        rating = 'are at risk of being overweight, take care'
    elif 18.4 < bmi < 25:
        rating = 'are normal, well done'
    else:
        rating = 'are at risk of being underweight, take care'
        
    return f"Your BMI is {bmi} and you {rating}"

if st.button("Calculate BMI"):
    st.write(bmi_calc(w,h))