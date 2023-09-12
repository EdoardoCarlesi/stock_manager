import streamlit as st
import pandas as pd

# Initialize a dictionary to store the stock items for each day
stock_data = {}

# Streamlit app title
st.title("Stock Management App")

# Sidebar for user input
st.sidebar.header("Add New Item")
item_name = st.sidebar.text_input("Item Name:")
item_price = st.sidebar.number_input("Item Price:", step=0.01)
item_quantity = st.sidebar.number_input("Item Quantity:", step=1)

if st.sidebar.button("Add Item"):
    if item_name:
        if item_name in stock_data:
            # If the item already exists, update the quantity
            stock_data[item_name]['quantity'] += item_quantity
        else:
            # Add a new item to the stock
            stock_data[item_name] = {
                'price': item_price,
                'quantity': item_quantity
            }

# Show the stock table for the selected day
selected_day = st.sidebar.selectbox("Select Day:", list(stock_data.keys()))
st.header(f"Stock for {selected_day}")

if selected_day in stock_data:
    stock_df = pd.DataFrame(stock_data[selected_day]).transpose()
    stock_df.rename(columns={"quantity": "Quantity", "price": "Price"}, inplace=True)
    st.write(stock_df)
else:
    st.warning("No items for the selected day.")

# "+" and "-" buttons to increase or decrease stock
st.sidebar.header("Modify Stock Quantity")
mod_item_name = st.sidebar.selectbox("Select Item to Modify:", list(stock_data.get(selected_day, {}).keys()))
mod_quantity = st.sidebar.number_input("Quantity:", step=1)

if st.sidebar.button("+"):
    if mod_item_name in stock_data[selected_day]:
        stock_data[selected_day][mod_item_name]['quantity'] += mod_quantity

if st.sidebar.button("-"):
    if mod_item_name in stock_data[selected_day]:
        stock_data[selected_day][mod_item_name]['quantity'] -= mod_quantity

# Clear stock button
if st.sidebar.button("Clear Stock"):
    if selected_day in stock_data:
        stock_data[selected_day] = {}
        st.success("Stock for the selected day cleared.")

# Save the stock for the selected day
if st.sidebar.button("Save Stock"):
    if selected_day in stock_data:
        stock_df = pd.DataFrame(stock_data[selected_day])
        stock_df.to_csv(f"stock_{selected_day}.csv")
        st.success(f"Stock for {selected_day} saved to 'stock_{selected_day}.csv'")
    else:
        st.warning("No items for the selected day to save.")

# Load stock data for a specific day
st.sidebar.header("Load Stock Data")
load_day = st.sidebar.text_input("Enter Day to Load Data:")
if st.sidebar.button("Load Data"):
    try:
        loaded_data = pd.read_csv(f"stock_{load_day}.csv", index_col=0).to_dict()
        stock_data[load_day] = loaded_data
        st.success(f"Stock data for {load_day} loaded successfully.")
    except FileNotFoundError:
        st.error(f"Stock data file for {load_day} not found.")

# Display the list of available days
st.sidebar.header("Available Days")
st.sidebar.write(list(stock_data.keys()))

