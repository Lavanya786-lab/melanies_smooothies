# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
helpful_links = [
    "https://docs.streamlit.io",
    "https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit",
    "https://github.com/Snowflake-Labs/snowflake-demo-streamlit",
    "https://docs.snowflake.com/en/release-notes/streamlit-in-snowflake"
]

# Write directly to the app
st.title(":cup_with_straw: Customize your smoothie! :cup_with_straw:")
st.write("""Choose the fruits you want in your custom smoothie!""")


name_on_order = st.text_input("Name on Smoothie")
st.write('The name on smoothie will be', name_on_order)


cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect('Choose upto 5 ingredients:',my_dataframe,max_selections=5)
if ingredients_list:
  
    
    ingredients_string = ''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
    st.write(ingredients_string)

#name_on_order = st.text_input("ORDER_FILLED")
#st.write('The name on smoothie will be', ORDER_FILLED)
#name_on_order = st.text_input("ORDER_UID")
#st.write('The name on smoothie will be', ORDER_UID)

my_insert_stmt = """ insert into smoothies.public.orders
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""

st.write(my_insert_stmt)
st.stop()

time_to_insert = st.button('Submit Order')
if time_to_insert:
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered!' + name_on_order, icon="✅")

import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response)
    
