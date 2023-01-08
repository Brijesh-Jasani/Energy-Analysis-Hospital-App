import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")
st.title("AEEE Smart Hospital Data Analysis")
st.header("@Brijesh Jasani")
#Grid electricity monthly


sheet_id = "1WCaIIgbxEEsCmsqlokJS-Rr0EbgKXOuQ77fCpMll_bs"


sheet_name_1 = "Grid_monthly_data"
df1 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_1}")
#fac_name = df1.iloc[:,0:]
#name_drop = st.selectbox("Select hospital",fac_name,)
fig1= px.box(data_frame=df1.iloc[:,1:],  title='Grid Electricity Consumption by Month')
fig1.update_traces(marker_color='green')
fig1.update_xaxes(title="Months")
fig1.update_yaxes(title="Electricity (kWh)")
st.plotly_chart(fig1, theme=None, use_container_width=True)

#bar chart
df1A = df1.set_index("Facility name")
varA = st.selectbox("Select hospital",df1A.index, key="chart1")
fig1A = px.bar(data_frame=df1A.loc[varA],  title='Grid Electricity Consumption by Month for ' + str(varA))
fig1A.update_traces(marker_color='green')
fig1A.update_xaxes(title="Months")
fig1A.update_yaxes(title="Electricity (kWh)")
st.plotly_chart(fig1A, theme=None, use_container_width=True)

#DG set electricity monthly
sheet_name_2 = "DG_set_monthly"
df2 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_2}")
fig2 = px.box(data_frame=df2.iloc[:,1:],  title='DG Set Electricity Consumption by Month')
fig2.update_xaxes(title="Months")
fig2.update_yaxes(title="Electricity (kWh)")
st.plotly_chart(fig2, theme=None, use_container_width=True)

#bar chart
df2A = df2.set_index("Facility name")
varB = st.selectbox("Select hospital",df2A.index, key="chart2" )
fig2A = px.bar(data_frame=df2A.loc[varB],  title='DG Set Electricity Consumption by Month for ' + str(varB))
fig2A.update_xaxes(title="Months")
fig2A.update_yaxes(title="Electricity (kWh)")
st.plotly_chart(fig2A, theme=None, use_container_width=True)

#area vs annual(kwh)
st.title("Building area Vs other parameters")
sheet_name_3 = "HVAC"
df3 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_3}")
x=df3.columns[1]
variables=st.selectbox("Select variable for y axis",df3.columns,)
colour=st.selectbox("Select third varible",df3.columns)
fig3=px.scatter(df3, y= variables, x=df3.columns[1],color =colour, title= str(x) + " Vs " + str(variables) )
fig3.update_xaxes(title=x)
fig3.update_yaxes(title=variables)
st.plotly_chart(fig3, theme=None, use_container_width=True)

#breakup of BMS
st.title("Annual end-use system electricity consumption (in kWh)")
sheet_name_4 = "End-breakup"
df4 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_4}")
df4=df4.set_index("Facility name")
column_names_all = df4.columns
hospital=st.selectbox("Select hospital for energy breakup",df4.index)
year=st.selectbox("Select year ", ["FY19-20","FY20-21"])

matching_columns_year = []
for column_name in column_names_all:
    if year in column_name:
        matching_columns_year.append(column_name)
        
df4 = df4[matching_columns_year]
#st.text("You have selected " + hospital)
fig4 = px.pie(df4,values=df4.loc[hospital], names=df4.columns, title='Annual end-use system electricity consumption (in kWh)')
st.plotly_chart(fig4, theme=None, use_container_width=True)

#Solar PV Generation
sheet_name_5 = "Solar"
df5 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_5}")
fig5= px.box(data_frame=df5.iloc[:,5:],  title='Solar PV Generation Monthly')
fig5.update_traces(marker_color='orange')
fig5.update_xaxes(title="Months")
fig5.update_yaxes(title="Electricity (kWh)")
st.plotly_chart(fig5, theme=None, use_container_width=True)

#bar chart
df5A = df5.set_index("Facility name")
df5A = df5A.iloc[:,4:]
varC = st.selectbox("Select hospital",df5A.index, key="chart3" )
fig5A = px.bar(data_frame=df5A.loc[varC],  title='Solar PV Generation Monthly for ' + str(varC))
fig5A.update_traces(marker_color='orange')
fig5A.update_xaxes(title="Months")
fig5A.update_yaxes(title="Electricity (kWh)")
st.plotly_chart(fig5A, theme=None, use_container_width=True)

#scatter plot
#x1=df5.columns[2]
variables1=st.selectbox("Select year for y axis", ["2019-20_kwh_generation","2020-21_kwh_generation"])
fig5=px.scatter(df5, y= variables1, x="Peak capacity ", title= str("Peak capacity") + " Vs Generation in " + str(variables1) )
fig5.update_xaxes(title="Peak capacity (kW)")
fig5.update_yaxes(title=variables1)
st.plotly_chart(fig5, theme=None, use_container_width=True)

#KPIs
st.title("Important KPIs")
sheet_name_6 = "KPI"
df6 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_6}")
df6 = df6.set_index("Facility name")
df6 = df6.iloc[:,:7]
col=df6.columns
variables6=st.selectbox("Select variable", df6.columns,key="chart6")
#variables7=st.selectbox("Select variable", df6.columns,key="chart7")
fig6=px.scatter(df6, y= variables6, x=df6.index, title= str(variables6),height=800, color="Climate Zone" )
#fig6.update_xaxes(title=variables6)
fig6.update_yaxes(title=variables6)
st.plotly_chart(fig6, theme=None, use_container_width=True)