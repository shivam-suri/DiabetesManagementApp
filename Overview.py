import streamlit as st
import numpy as np
import datetime as dt
import functions as f

from pydexcom import Dexcom
current_time = dt.datetime.now().strftime('%I:%M:%S')

st.set_page_config(
    page_title="Diabetes"
)

if "my_username" not in st.session_state:
    st.session_state["my_username"] = ""

if "password_str" not in st.session_state:
    st.session_state["password_str"] = ""

username = "Username"
password = "Password"

st.sidebar.subheader("Please Enter Username and Password")

my_username = st.sidebar.text_input("Enter Username",
                                    st.session_state["my_username"],
                                    placeholder=username,
                                    label_visibility="collapsed")

my_password = st.sidebar.empty()
password_str = my_password.text_input("Enter Password",
                                      st.session_state["password_str"],
                                      placeholder=password,
                                      label_visibility="collapsed")

enter = st.sidebar.button("Enter")
if enter:
    st.session_state["my_username"] = my_username
    st.session_state["password_str"] = password_str
    username = my_username
    password = password_str
    my_password.text_input("",
                           placeholder=f.conv_pass(password),
                           label_visibility="collapsed")

dexcom = Dexcom(username, password, True)
bg = Dexcom.get_glucose_readings(dexcom)
bg = np.array(bg)
current_bg = Dexcom.get_current_glucose_reading(dexcom)

# Page Layout

st.title("Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg 24Hr BG:", f.avg_bg(f.prod_readings(bg)))
col2.metric("Highest 24Hr BG:", max(f.prod_readings(bg)))
col3.metric("Lowest 24Hr BG:", min(f.prod_readings(bg)))
col4.metric("Current BG:", f"{current_bg.mmol_l}{f.prod_trends(bg)[0]}")

st.subheader("BG Variation")
st.line_chart(reversed(f.prod_readings(bg)))

st.subheader("Time in Range")

range_data = [f.calc_low(f.prod_readings(bg)),
              f.calc_in_range(f.prod_readings(bg)),
              f.calc_high(f.prod_readings(bg))]

col5, col6 = st.columns(2)
col5.bar_chart(range_data)

tab1, tab2, tab3 = col6.tabs(["Low", "In range", "High"])

with tab1:
    st.write(f"Your blood sugar is **low {range_data[0]}%** of the time.")
    st.write("Target Range: 4.0 - 10.0")
with tab2:
    st.write(f"Your blood sugar is **in range {range_data[1]}%** of the time")
    st.write("Target Range: 4.0 - 10.0")
with tab3:
    st.markdown(f"Your blood sugar is **high {range_data[2]}%** of the time.")
    st.write("Target Range: 4.0 - 10.0")



