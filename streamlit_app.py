import streamlit
import pandas
import requests
import snowflake.connector

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

# New Section to display fruityvice API response
streamlit.header('Fruityvice Fruit Advice')
fruit_choice = streamlit.text_input('What kind of fruits would you like infos about ?','Kiwi');
streamlit.write('The user entered',fruit_choice);


fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/"+fruit_choice);
# streamlit.text(fruityvice_response.json());

fruityvice_norm = pandas.json_normalize(fruityvice_response.json());
streamlit.dataframe(fruityvice_norm);


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)
my_cur.execute("select * from fruit_load_list")
my_d=my_cur.fetchall() #fetchone
streamlit.text("The fruit load list conains")
streamlit.dataframe(my_d)
               
# adding fruits
added_fruit=streamlit.text_input("What fruit would you like to add ?");
streamlit.write("Thanks for adding the ",added_fruit);

my_cur.execute("insert into fruit_load_list values('from streamlit')")
