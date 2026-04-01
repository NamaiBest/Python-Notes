

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Streamlit Simple Pack", layout="centered")

st.title("Streamlit Simple Pack")

st.markdown("---")
st.header("1) Hello Demo")
name = st.text_input("Your name", "Ava")
if name:
    st.write(f"Hi {name}!")
st.caption("Tags used: st.title/st.header, st.text_input, st.write, st.caption")

st.markdown("---")


st.header("2) Car Filter")
df = pd.DataFrame({
    "car": ["Swift", "i20", "City", "Nexon", "Creta", "Amaze", "Baleno", "Venue"],
    "price_lakh": [6.8, 7.9, 11.5, 9.4, 14.2, 8.6, 7.1, 12.9],
    "fuel": ["Petrol", "Petrol", "Petrol", "Diesel", "Diesel", "Petrol", "CNG", "Diesel"],
    "year": [2021, 2020, 2019, 2022, 2023, 2021, 2020, 2022],
})

max_price = st.slider("Show cars priced up to (lakh)", 5.0, 16.0, 12.0, 0.1)
filtered = df[df["price_lakh"] <= max_price]
st.dataframe(filtered, use_container_width=True)
st.bar_chart(filtered.set_index("car")["price_lakh"])


st.caption("Tags used: st.slider, st.dataframe, st.bar_chart")

st.markdown("---")

st.header("3) Titanic Counts")
titanic = sns.load_dataset("titanic")
fig, ax = plt.subplots(figsize=(5, 3))
sns.countplot(data=titanic, x="class", hue="survived", ax=ax)
st.pyplot(fig)
st.caption("Tags used: st.pyplot")

st.markdown("---")
st.header("4) Quick Form")
with st.form("feedback"):
    topic = st.text_input("Topic you liked most", "Streamlit")
    rating = st.slider("Clarity rating", 1, 5, 4)
    submitted = st.form_submit_button("Submit")
if submitted:
    st.success(f"Thanks! Topic: {topic}, Rating: {rating}")
st.caption("Tags used: st.form, st.form_submit_button, st.success")
