import streamlit
import pandas pd

streamlit.title('Working with Fred: Breakfast in Algiers- 🐔 🐔 🐔')
streamlit.text('Milk and dates')
streamlit.text('oats and bananas')

# reading CSV files
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
