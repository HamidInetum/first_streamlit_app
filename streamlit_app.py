import streamlit
import pandas

streamlit.title('Working with Fred: Breakfast in Algiers- 🐔 🐔 🐔')
streamlit.text('Milk and dates')
streamlit.text('oats and bananas')

# reading CSV files
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# adding multiselect feature
streamlit.multiselect("Pick your fruits buddy !",list(my_fruits_list.index()))

streamlit.dataframe(my_fruit_list)
