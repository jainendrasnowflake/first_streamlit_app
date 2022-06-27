import streamlit;
import pandas

streamlit.title('(: My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu');
streamlit.text('Bread, Butter');
streamlit.text('Milk, Sugar');


fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),[1,2,3])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

 

