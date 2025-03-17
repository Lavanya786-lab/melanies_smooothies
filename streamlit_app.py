# Import python packages
 import streamlit as st
 from snowflake.snowpark.context import get_active_session
 from snowflake.snowpark.functions import col
 
 # Write directly to the app
 @@ -12,33 +11,34 @@
 name_on_order = st.text_input('Name on Smothie: ')
 st.write('The name on your Smoothie will be: ', name_on_order)
 
 session = get_active_session()
 cnx = st.connection("snowflake")
 session = cnx.session()
 
 my_dataframe = session.table(
     "smoothies.public.fruit_options").select(col('FRUIT_NAME'))
 
 ingredients_list = st.multiselect(
     "Choose up to 5 ingredients",
     my_dataframe,
     max_selections=5
 )
 
 if ingredients_list:
 
     ingredients_string = ''
 
     for fruit in ingredients_list:
         ingredients_string += fruit + ' '
 
     st.write(ingredients_string)
 
     my_insert_stmt = """ insert into smoothies.public.orders
     (ingredients, name_on_order)
     values ('""" + ingredients_string + """', '""" + name_on_order +"""')"""
 
     time_to_insert = st.button('Submit Order')
 
     if time_to_insert:
 
         session.sql(my_insert_stmt).collect()
         st.success('Your Smoothie is ordered, '+name_on_order+'!', icon="✅")
