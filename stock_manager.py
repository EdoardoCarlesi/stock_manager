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
    
    tot_sales = np.sum(stock_data['SALES'].values * stock_data['PRICE'].values)
    stock_tshirt = stock_data['CLASS'] == "TSHIRT"
    stock_gadget = stock_data['CLASS'] == "GADGET"
    stock_music = stock_data['CLASS'] == "MUSIC"
    tshirt_sales = np.sum(stock_data[stock_tshirt]['SALES'].values * stock_data[stock_tshirt]['PRICE'].values)
    music_sales = np.sum(stock_data[stock_music]['SALES'].values * stock_data[stock_music]['PRICE'].values)
    gadget_sales = np.sum(stock_data[stock_gadget]['SALES'].values * stock_data[stock_gadget]['PRICE'].values)

    st.write('____________________')
    tshirt_txt = f'\n\n\t\tSALES TSHIRTS:    {tshirt_sales}'
    music_txt = f'\t\tSALES MUSIC:    {music_sales}'
    gadget_txt = f'\t\tSALES GADGET:    {gadget_sales}'
    tot_txt = f'\n\nSALES TOTAL:    {tot_sales}'

    st.write(music_txt)
    st.write(tshirt_txt)
    st.write(gadget_txt)
    st.write(tot_txt)
    st.write('____________________\n\n')


def gen_products():

    st.title("Product Input App")

    # Define a dictionary to map product types to their respective options
    product_options = {
        "T-shirt": ["XS", "S", "M", "L", "XL", "2XL", "3XL"],
        "Music": ["CD", "2CD", "LP", "2LP"],
        "Gadget": ["Standard"]
    }

    # Input selection
    product_type = st.selectbox("Select product type:", list(product_options.keys()))
    product_name = st.text_input("Enter product name:")
    price = st.number_input("Enter price:", min_value=0, step=1)
    quantity = st.number_input("Enter quantity:", min_value=0, step=1)

    # Select type based on the product type
    product_type_options = product_options.get(product_type, [])
    if product_type_options:
        product_type_selected = st.selectbox("Select product type:", product_type_options)

    # Display the input values
    st.write("Product Type:", product_type)
    st.write("Product Name:", product_name)
    st.write("Price:", price)
    st.write("Quantity:", quantity)
    st.write("Type:", product_type_selected)

# Create a dictionary to store user credentials (for demonstration purposes)
# In a real application, you should use a more secure method to store credentials.
# TODO use env vars or hidden files

def login():

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

    return st.experimental_get_query_params().get('logged_in')


# Check if the user is logged in
#logged_in = login()
logged_in = True

if logged_in: 

    templates = glob.glob('templates/*.csv')
    temp_dict = dict() 

    for temp in templates:
        temp_dict[temp.split('_')[0].split('/')[-1].upper()] = temp 

    template_name = st.selectbox("Select Template", temp_dict.keys())

    #if st.button("Load Template"):
    show_data = pd.read_csv(temp_dict[template_name])
    
    if st.button("Clear"):
        cols = ['ITEM', 'PRICE', 'SALES', 'CLASS']
        show_data = pd.DataFrame()
        for col in cols:
            show_data[col] = 0        
    

    gen_buttons(show_data)

    files_saved = []
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")

    city_name = st.text_input("City:")
    save_path = "sales_record"
    value_default = f'{year}_{month}_{day}_{city_name}'
    #item_name = st.sidebar.text_input("File Name Save:", value=value_default)

    if st.button("Save Stock"):
        save_file = f'{save_path}/{value_default}.csv'  
        show_data.to_csv(save_file) 
        print(f'Saving to {save_file}')

    #if st.button("Refresh Files"):
    files_saved = glob.glob(f'{save_path}/*.csv')
    
    if st.button("Refresh Files"):
        files_saved = glob.glob(f'{save_path}/*.csv')

    if len(files_saved) > 1:
        saved_file = st.selectbox("Load File", files_saved)
    
    if st.button("Load Stock"):
        show_data = pd.read_csv(saved_file)    
        st.write(show_data)
        print(f'Loading  file: {saved_file}')


