import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title='Price Predictor', page_icon='<UNK>')
st.title('Price Predictor App for Real Estate')

with open('df.pkl', 'rb') as f:
    df=pickle.load(f)

#st.dataframe(df)

with open('pipeline.pkl', 'rb') as f:
    pipeline=pickle.load(f)


#property_type
st.header('Enter your inputs')

property_type=st.selectbox('Property Type',['flat','house'])

#sector
sector=st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

#bedroom and bathroom
bedroom=float(st.selectbox('Number of Bedroom',sorted(df['bedroom'].unique().tolist())))
bathroom=float(st.selectbox('Number of Bathroom',sorted(df['bathroom'].unique().tolist())))


#balcony
balcony=st.selectbox('Number of Balcony',sorted(df['balcony'].unique().tolist()))

#agePossession
agePossession=st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

#built_up_area
built_up_area=float(st.number_input('Built Up Area'))

#servant and store room
servant_room=float(st.selectbox('Servant Room',[0.0,1.0]))
store_room=float(st.selectbox('Store Room',[0.0,1.0]))


#furnishing_type
furnishing_type=st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))

#luxury_category and floor_category
luxury_category=st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))
floor_category=st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))


if st.button('Predict'):
    #form a dataframe
    data = [[property_type, sector, bedroom, bathroom, balcony, agePossession, built_up_area, servant_room
                , store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedroom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    #st.dataframe(one_df)

    #predict
    base_price=np.expm1(pipeline.predict(one_df))[0]
    low=base_price-0.22
    high=base_price+0.22


    #display

    st.text('The price is between  {:.2f} and {:.2} Crores INR'.format(low,high))

