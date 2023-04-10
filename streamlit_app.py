import streamlit

streamlit.title('My parents New healthy dinner')
streamlit.header(' Breakfast Menu')
streamlit.text('🥣  omega 3 & Blueberry Oat meal')
streamlit.text(' 🥗 kale,spinach & Rocket smoothie')
streamlit.text(' 🐔Hard-boiled free range egg')
streamlit.text('🥑🍞 Avacado toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.

