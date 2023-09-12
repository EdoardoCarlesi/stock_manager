import streamlit as st
import pandas as pd
import datetime
import glob

# Function to load an initial stock template from a CSV file
def load_template(template_file):
    try:
        template_data = pd.read_csv(template_file)
        return template_data, True
    except FileNotFoundError:
        return _, False

# TODO
#def gen_template():

# Streamlit app title
st.sidebar.title("Stock Management App")

# Initialize a dictionary to store the stock items for each day
stock_data = {}

# Load an initial template if available
template_path = "./templates/"
save_path = './sales_record/'

templates = glob.glob(f'{template_path}/*.csv')
files_saved = glob.glob(f'{save_path}/*.csv')

#st.sidebar.header("Select Template")
template_file = st.sidebar.selectbox("Select Template", templates)
show_data = pd.read_csv(template_file)

if st.sidebar.button("Load Template"):
    show_data = pd.read_csv(template_file)
    #print(show_data.head())
    st.write(show_data)

print('PorcoDDio')
print(show_data.head())
now = datetime.datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

city_name = st.sidebar.text_input("City:")
value_default = f'{year}_{month}_{day}_{city_name}'
#item_name = st.sidebar.text_input("File Name Save:", value=value_default)

if st.sidebar.button("Save Stock"):
    save_file = f'{save_path}/{value_default}.csv'  
    show_data.to_csv(save_file) 
    print(f'Saving to {save_file}')

if st.sidebar.button("Refresh Files"):
    files_saved = glob.glob(f'{save_path}/*.csv')

saved_file = st.sidebar.selectbox("Load File", files_saved)

if st.sidebar.button("Load Stock"):
    show_data = pd.read_csv(saved_file)    
    st.write(show_data)
    print(f'Loading  file: {saved_file}')

"""
# Sidebar for user input

st.sidebar.header("Add New Item")
item_name = st.sidebar.text_input("ITEM:")
item_price = st.sidebar.number_input("PRICE:", step=0.01)
item_quantity = st.sidebar.number_input("SALES:", step=1)

if st.sidebar.button("Add Item"):
    if item_name:
        if item_name in stock_data.get(selected_day, {}):
            # If the item already exists, update the quantity
            stock_data[selected_day][item_name]['quantity'] += item_quantity
        else:
            # Add a new item to the stock
            if selected_day not in stock_data:
                stock_data[selected_day] = {}
            stock_data[selected_day][item_name] = {
                'ITEM': item_price,
                'SALES': item_quantity
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
    if mod_item_name in stock_data.get(selected_day, {}):
        stock_data[selected_day][mod_item_name]['quantity'] += mod_quantity

if st.sidebar.button("-"):
    if mod_item_name in stock_data.get(selected_day, {}):
        stock_data[selected_day][mod_item_name]['quantity'] -= mod_quantity

# Clear stock button
if st.sidebar.button("Clear Stock"):
    if selected_day in stock_data:
        stock_data[selected_day] = {}
        st.success("Stock for the selected day cleared.")

# Save the stock for the selected day
if st.sidebar.button("Save Stock"):
    if selected_day in stock_data:
        stock_df = pd.DataFrame(stock_data[selected_day]).transpose()
        stock_df.to_csv(f"stock_{selected_day}.csv")
        st.success(f"Stock for {selected_day} saved to 'stock_{selected_day}.csv'")
    else:
        st.warning("No items for the selected day to save.")

# Display the list of available days
st.sidebar.header("Available Days")
st.sidebar.write(list(stock_data.keys()))
"""
