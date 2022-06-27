import streamlit;
import pandas

streamlit.title('(: My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu');
streamlit.text('Bread, Butter');
streamlit.text('Milk, Sugar');

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

 

