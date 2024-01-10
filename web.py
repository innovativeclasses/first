


import numpy as np	# np mean, np random
import pandas as pd	 # read csv, df manipulation

import streamlit as st	# 🎈 data web app development

from streamlit_gsheets import GSheetsConnection



st.set_page_config(
	page_title="Real-Time Data Science Dashboard",
	page_icon="chart_with_upwards_trend",
	layout="wide",
)
#data source
url = "https://docs.google.com/spreadsheets/d/1QDqugik8wKtOSYFmxchjxkdW81zAMqtIOeHm49Uq7g0/edit?usp=sharing"

conn=st.connection("gsheets",type=GSheetsConnection)

st.title("Live Data MVVNL Dashboard")


st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
df=pd.read_csv('menu.csv',dtype=str)

#sidebar
st.sidebar.title('MVVNL DATA')
st.sidebar.write('Please Filter Here...')	
with st.sidebar:
	option1 = st.selectbox('Zone',df['Zone'].unique(),placeholder="choose zone",index=None)
	option2 = st.selectbox('Select Circle',df.loc[df['Zone']==option1]['Circle'].unique())
	option = st.selectbox('Select Division',df.loc[df['Circle']==option2]['Division'].unique())
	submit=st.button("Filter", use_container_width=True)
#col1,col2=st.columns((2))
#with col1:
	
st.markdown('<h3 class="bold-heading">Zone/Circle/Division Dashboard</h3>', unsafe_allow_html=True)
	
	
	

st.markdown('<h4 style="font-size: 16px; font-weight: bold;">OTS Progress</h4>', unsafe_allow_html=True)
		
	

		

df=conn.read(spreadsheet=url,usecols=[0,2,3])
	#st.dataframe(df,hide_index=True)
filtered=df[df["Zone/Circle/Division/Sub station"].isin(['MVVNL'])]
st.dataframe(filtered,hide_index=True)	
		
	
	
	
	#filter setting
	
if submit:
	print (df.head(10))
	if not option1:
		
			
	if option and option == option:
		print ('dd')
		filtered=df[df["Zone/Circle/Division/Sub station"]==option]
		print(filtered.head(10))
		#values_str = '\n'.join(filtered["col1"])
		st.dataframe(filtered,hide_index=True)
			
	elif option2 and option2 == option2:
		print ('dfdfdfd')
		filtered=df[df["Zone/Circle/Division/Sub station"]==option2]
		#values_str = '\n'.join(filtered["col1"])
		#st.write(values_str)			
		st.dataframe(filtered,hide_index=True)	
	elif option1 and option1 == option1:
		print ('dffdsdsfdfdfd')
		filtered=df[df["Zone/Circle/Division/Sub station"]==option1]
		#values_str = '\n'.join(filtered["col1"])
		#st.write(values_str)
		st.dataframe(filtered,hide_index=True)


