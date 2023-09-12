import streamlit as st

# Initialize a dictionary to store the stock items
stock_items = {}

# Streamlit app title
st.title("Stock Management App")

# Sidebar for user input
st.sidebar.header("Add New Item")
item_name = st.sidebar.text_input("Item Name:")
item_price = st.sidebar.number_input("Item Price:", step=0.01)
item_quantity = st.sidebar.number_input("Item Quantity:", step=1)

if st.sidebar.button("Add Item"):
    if item_name:
        if item_name in stock_items:
            # If the item already exists, update the quantity
            stock_items[item_name]['quantity'] += item_quantity
        else:
            # Add a new item to the stock
            stock_items[item_name] = {
                'price': item_price,
                'quantity': item_quantity
            }

# Show the stock table
st.header("Current Stock")
if stock_items:
    stock_data = {'Item Name': [], 'Price': [], 'Quantity': []}
    for item_name, item_info in stock_items.items():
        stock_data['Item Name'].append(item_name)
        stock_data['Price'].append(item_info['price'])
        stock_data['Quantity'].append(item_info['quantity'])

    st.table(stock_data)
else:
    st.warning("No items in stock.")

# Clear stock button
if st.button("Clear Stock"):
    stock_items.clear()
    st.success("Stock cleared.")

# Save the stock to a file (optional)
if st.button("Save Stock"):
    with open("stock.txt", "w") as file:
        for item_name, item_info in stock_items.items():
            file.write(f"{item_name},{item_info['price']},{item_info['quantity']}\n")
    st.success("Stock saved to 'stock.txt'")

