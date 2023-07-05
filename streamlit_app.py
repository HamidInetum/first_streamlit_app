import streamlit
import pandas

streamlit.title('Working with Fred: Breakfast in Algiers- 🐔 🐔 🐔')
streamlit.text('Milk and dates')
streamlit.text('oats and bananas')

# reading CSV files
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# adding multiselect feature
streamlit.multiselect("Pick your fruits buddy !",list(my_fruit_list.index),['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)
