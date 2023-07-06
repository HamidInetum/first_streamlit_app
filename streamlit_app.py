import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('Working with Fred: Breakfast in Algiers- 🐔 🐔 🐔')
streamlit.text('Milk and dates')
streamlit.text('oats, bananas and peanut butter')

# reading CSV files 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# adding multiselect feature
selected_fruits = streamlit.multiselect("Pick your fruits buddy !",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[selected_fruits]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(fruit_choice):
  fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/"+fruit_choice);
  #streamlit.write('The user entered',fruit_choice);
  fruityvice_norm = pandas.json_normalize(fruityvice_response.json());
  return fruityvice_norm


# New Section to display fruityvice API response
streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice = streamlit.text_input('What kind of fruits would you like infos about ?');
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function);
except URLError as e:
  streamlit.error()




#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)
streamlit.text("The fruit load list conains")

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall() 
if streamlit.button('Get Fruit Load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

streamlit.stop()


streamlit.dataframe(my_d)
               
# adding fruits

added_fruit=streamlit.text_input("What fruit would you like to add ?");

streamlit.write("Thanks for adding the ",added_fruit);

my_cur.execute("insert into fruit_load_list values('from streamlit')")
