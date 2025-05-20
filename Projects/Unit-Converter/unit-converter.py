import streamlit as st

# App Title and Description
st.title("🌎 Unit Converter App")
st.markdown("### Converts Length, Weight and Time Instantly")
st.write("Welcome! Select a category, enter a value and get the converted result in real-time.")

# Category Selection
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Conversion Options Based on Category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Miles to Kilometers", "Kilometers to Miles"]) 
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⌚ Select Conversion", [
        "Seconds to Minutes", "Minutes to Seconds", 
        "Minutes to Hours", "Hours to Minutes", 
        "Hours to Days", "Days to Hours"
    ])

# Value Input
value = st.number_input("Enter the value to convert", format="%.4f")

# Conversion Function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight": 
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return None

# Convert Button
if st.button("Convert"): 
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is: **{round(result, 4)}**")
    else:
        st.error("Invalid conversion.")
