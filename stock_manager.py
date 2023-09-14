import streamlit as st
import pandas as pd
import numpy as np
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
def new_template(names, types, prices):
    pass


def gen_buttons(stock_data):

    mod_quantity = 1

    for i, row in stock_data.iterrows():

        item = row['ITEM']
        price = row['PRICE']
        sales = row['SALES']
    
        col1, col2 = st.columns([3, 1])
        container = st.container()

        row_txt = item + ' ' + str(price)
        #st.number_input(row_txt, step=1)

        with container:
            with col1:
                st.write(row_txt)
            with col2:
                quantity = st.number_input(row_txt, label_visibility="collapsed", key=item, step=1)       
        
        stock_data.at[i, 'SALES'] = quantity

    #for i, row in stock_data.iterrows():
    #    tot_sales += row['SALES'] * row['PRICE']
        #print(row['PRICE'], row['SALES'])
    tot_sales = np.sum(stock_data['SALES'].values * stock_data['PRICE'].values)
    #print(tot_sales)
    tot_txt = f'SALES TOTAL:    {tot_sales}'
    st.write(tot_txt)

# Create a dictionary to store user credentials (for demonstration purposes)
# In a real application, you should use a more secure method to store credentials.
# TODO use env vars or hidden files
user_credentials = {
    'username': 'admin',
    'password': 'password123'
}

# Streamlit app title
st.title("Login Page")

# Create input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Check if the login button is clicked
if st.button("Login"):
    # Check if the entered username and password match the stored credentials
    if username == user_credentials['username'] and password == user_credentials['password']:
        st.success("Logged in as {}".format(username))
        
        # Set a flag to indicate successful login
        st.experimental_set_query_params(logged_in=True)
    else:
        st.error("Invalid username or password. Please try again.")

# Check if the user is logged in
if st.experimental_get_query_params().get('logged_in'):

    # Streamlit app title
    st.title("Merchandise Management App")

    # Initialize a dictionary to store the stock items for each day
    stock_data = {}

    # Load an initial template if available
    template_path = "./templates/"
    save_path = './sales_record/'

    templates = glob.glob(f'{template_path}/*.csv')
    files_saved = glob.glob(f'{save_path}/*.csv')

    #st.sidebar.header("Select Template")
    template_file = st.selectbox("Select Template", templates)
    show_data = pd.read_csv(template_file)

    if st.button("Load Template"):
        show_data = pd.read_csv(template_file)
        
    gen_buttons(show_data)

    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")

    city_name = st.text_input("City:")
    value_default = f'{year}_{month}_{day}_{city_name}'
    #item_name = st.sidebar.text_input("File Name Save:", value=value_default)

    if st.button("Save Stock"):
        save_file = f'{save_path}/{value_default}.csv'  
        show_data.to_csv(save_file) 
        print(f'Saving to {save_file}')

    if st.button("Refresh Files"):
        files_saved = glob.glob(f'{save_path}/*.csv')

    saved_file = st.selectbox("Load File", files_saved)

    if st.button("Load Stock"):
        show_data = pd.read_csv(saved_file)    
        st.write(show_data)
        print(f'Loading  file: {saved_file}')





