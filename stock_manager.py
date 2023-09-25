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

def gen_buttons(stock_data):

    mod_quantity = 1

    for i, row in stock_data.iterrows():

        item = row['ITEM']
        price = row['PRICE']
        sales = row['SALES']
    
        col1, col2 = st.columns([3, 1])
        container = st.container()

        keyplus = item 
        row_txt = item + ' ' + str(price)
        #st.number_input(row_txt, step=1)

        with container:
            with col1:
                st.write(row_txt)
            with col2:
                st.number_input(row_txt, label_visibility="collapsed", key=item, step=1)       

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

# Streamlit app title
st.title("Tour Sales Management App")

# Initialize a dictionary to store the stock items for each day
stock_data = {}

# Load an initial template if available
template_path = "./templates/"
save_path = './sales_record/'

templates = glob.glob(f'{template_path}/*.csv')
files_saved = glob.glob(f'{save_path}/*.csv')

temp_dict = dict() 

for temp in templates:
    temp_dict[temp.split('_')[0].split('/')[-1].upper()] = temp 

template_name = st.selectbox("Select Template", temp_dict.keys())

if st.button("Load Template"):
    show_data = pd.read_csv(temp_dict[template_name])
  
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

