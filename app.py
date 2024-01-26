import seaborn as sns
import numpy as np
import pandas as pd  
import streamlit as st  # pip install streamlit

st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")

#Load Data
df_customer = pd.read_csv('customer_interactions.csv')
df_purchase= pd.read_csv('purchase_history.csv')
df_product = pd.read_csv('product_details.csv')
df_merged = pd.read_csv('merged_data.csv')

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
customer = st.sidebar.multiselect(
    "Select the Customer ID:",
    options=df_merged["customer_id"].unique(),
    default=df_merged["customer_id"].unique()
)

# category = st.sidebar.multiselect(
#     "Select the Category:",
#     options=df_merged["category"].unique(),
#     default=df_merged["category"].unique()
# )

df_selection = df_merged.query(
    "customer_id == @customer"
)

# ---- MAINPAGE ----
st.title(":bar_chart: Dashboard")
st.markdown("##")
sum_category = df_selection["category"].value_counts()
st.table(sum_category)
st.markdown("##")
rate = df_selection.groupby(['category'])['price','ratings'].mean()
st.table(rate)


# st.markdown(hide_st_style, unsafe_allow_html=True)
