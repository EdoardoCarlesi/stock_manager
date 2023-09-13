import streamlit as st
import pandas as pd

# Sample data for the table
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 22],
    'Action 1': ['-', '-', '-'],
    'Action 2': ['-', '-', '-'],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a Streamlit app
st.title('Table with Buttons')

# Function to create buttons
def create_button(action_type):
    return f'<button class="btn">{action_type}</button>'

# Display the table
st.table(df)

# Add buttons to each row inside the table
for row_idx in range(len(df)):
    row_data = df.iloc[row_idx]
    action_1_button = create_button("Action 1")
    action_2_button = create_button("Action 2")
    st.write(
        f"<tr><td>{row_data['Name']}</td><td>{row_data['Age']}</td><td>{action_1_button}</td><td>{action_2_button}</td></tr>",
        unsafe_allow_html=True
    )
