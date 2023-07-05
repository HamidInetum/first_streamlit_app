import streamlit
import pandas

streamlit.title('Working with Fred: Breakfast in Algiers- 🐔 🐔 🐔')
streamlit.text('Milk and dates')
streamlit.text('oats and bananas')

# reading CSV files
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# adding multiselect feature
selected_fruits = streamlit.multiselect("Pick your fruits buddy !",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc(selected_fruits)
streamlit.dataframe(fruits_to_show)
