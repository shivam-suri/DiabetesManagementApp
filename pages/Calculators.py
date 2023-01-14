import streamlit as st
import functions as f
from pydexcom import Dexcom

dexcom = Dexcom(st.session_state["my_username"], st.session_state["password_str"], True)
current_bg = Dexcom.get_current_glucose_reading(dexcom).mmol_l

st.title("Calculators")

st.subheader("Correction Bolus Calculator")

factor = st.text_input("Enter Correction Factor:", placeholder="e.g 2.5")
enter2 = st.button("Enter", key="enter2")
if enter2:
    bolus = f.calc_correction(factor, current_bg)
    st.write(f"Administer a bolus of {bolus}")

st.subheader("Food Bolus Calculator")

ic = st.text_input("Enter Insulin to Carb Ratio:", placeholder="e.g 13")
carbs = st.text_input("Enter Number of Carbs:", placeholder="e.g 100")
factor2 = st.text_input("Enter Correction Factor:", placeholder="e.g 2.5", key="factor2")
enter3 = st.button("Enter", key="enter3")
if enter3:
    bolus = f.calc_food_bolus(ic, carbs, factor2, current_bg)
    st.write(f"Administer a bolus of {bolus}")
