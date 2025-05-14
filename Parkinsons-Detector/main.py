"""This is the main module to run the app"""
#python -m streamlit run main.py

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Configure the app
st.set_page_config(
    page_title = 'Parkinson\'s Disease Detection',
    page_icon = 'raised_hand_with_fingers_splayed',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Import pages
from Tabs import home, data, predict, visualise



# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise
    
    
}


# Create a sidebar
# Add title to sidear
st.sidebar.title("Explore")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))


# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()

