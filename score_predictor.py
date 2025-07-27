import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore')

model = joblib.load('score_predictor.pkl')

st.title('IPL Total Score Predictor')

venue = st.selectbox('Venue', ['M Chinnaswamy Stadium','Punjab Cricket Association Stadium, Mohali','Feroz Shah Kotla','Wankhede Stadium','Sawai Mansingh Stadium','MA Chidambaram Stadium, Chepauk','Eden Gardens','Himachal Pradesh Cricket Association Stadium','Rajiv Gandhi International Stadium, Uppal','Punjab Cricket Association IS Bindra Stadium, Mohali','Holkar Cricket Stadium'])
bat_team = st.selectbox('Batting Team', ['Kolkata Knight Riders','Chennai Super Kings','Rajasthan Royals','Mumbai Indians','Punjab Kings', 'Royal Challengers Bengaluru','Delhi Capitals', 'Sunrisers Hyderabad'])
bowl_team = st.selectbox('Bolwing Team', ['Kolkata Knight Riders','Chennai Super Kings','Rajasthan Royals','Mumbai Indians','Punjab Kings', 'Royal Challengers Bengaluru','Delhi Capitals', 'Sunrisers Hyderabad'])
runs = st.slider('Runs scored', 0, 400, 100)
wickets = st.slider('Wickets taken', 0, 10, 3)
overs = st.slider('Overs bowled', 5, 20, 10)
runs_last_5 = st.slider('Runs scored in last 5 overs', 0, 120, 50)
wickets_last_5 = st.slider('Wickets taken in last 5 overs', 0, 10, 2)

if bat_team == 'Kolkata Knight Riders':
       bat_encoded = 1
elif bat_team == 'Chennai Super Kings':
       bat_encoded = 2
elif bat_team == 'Rajasthan Royals':
       bat_encoded = 3
elif bat_team == 'Mumbai Indians':
       bat_encoded = 4
elif bat_team == 'Punjab Kings':
       bat_encoded = 5
elif bat_team == 'Royal Challengers Bengaluru':
       bat_encoded = 6
elif bat_team == 'Delhi Capitals':
       bat_encoded = 7
elif bat_team == 'Sunrisers Hyderabad':
       bat_encoded = 8

if bowl_team == 'Kolkata Knight Riders':
       bowl_encoded = 1
elif bowl_team == 'Chennai Super Kings':
       bowl_encoded = 2
elif bowl_team == 'Rajasthan Royals':
       bowl_encoded = 3
elif bowl_team == 'Mumbai Indians':
       bowl_encoded = 4
elif bowl_team == 'Punjab Kings':
       bowl_encoded = 5
elif bowl_team == 'Royal Challengers Bengaluru':
       bowl_encoded = 6
elif bowl_team == 'Delhi Capitals':
       bowl_encoded = 7
elif bowl_team == 'Sunrisers Hyderabad':
       bowl_encoded = 8

if venue == 'M Chinnaswamy Stadium': 
       venue_encoded = 1
elif venue == 'Punjab Cricket Association Stadium, Mohali': 
       venue_encoded = 2 
elif venue == 'Feroz Shah Kotla': 
       venue_encoded = 3
elif venue == 'Wankhede Stadium': 
       venue_encoded = 4
elif venue == 'Sawai Mansingh Stadium': 
       venue_encoded = 5
elif venue == 'MA Chidambaram Stadium, Chepauk':
       venue_encoded = 6 
elif venue == 'Eden Gardens': 
       venue_encoded = 7
elif venue == 'Himachal Pradesh Cricket Association Stadium': 
       venue_encoded = 8
elif venue == 'Rajiv Gandhi International Stadium, Uppal': 
       venue_encoded = 9
elif venue == 'Punjab Cricket Association IS Bindra Stadium, Mohali':
       venue_encoded = 10
elif venue == 'Holkar Cricket Stadium': 
       venue_encoded = 11


if st.button('Predict Total Score'):
       
        
               
       input_data = np.array([venue_encoded,
               bat_encoded,
               bowl_encoded,
               runs,
               wickets,
               overs,
               runs_last_5,
               wickets_last_5])
       prediction = model.predict(input_data.reshape(1,-1))[0]

       st.success(f'Predicted Totel Score : {prediction:.0f}') 

