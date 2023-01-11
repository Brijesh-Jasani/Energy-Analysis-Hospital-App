import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("AEEE-CCDC Hospital Energy Survey Data Analysis")
st.header("@Integrative Design Solutions (IDSPL)")

#sheet_id = "1WCaIIgbxEEsCmsqlokJS-Rr0EbgKXOuQ77fCpMll_bs", FILTER
#sheet_id = "1_rZKGk_IYFkEN4aCJFf7HmPAbhNIJNon" , FILTER V1
sheet_id = "1seBVfzzCDMroalZICDuYHFacq_u_caHm"  #FILTER V2
st.title("Building-level energy use")

#Excel images
image = Image.open('2.jpeg')
image1 = Image.open('1.jpeg')
st.image(image, caption='Grid Electricity consumption by hospitals')
st.image(image1, caption='Monthly variation in grid electricity consumption')


#Grid electricity monthly
sheet_name_1 = "Grid_monthly_data"
df1 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_1}")
y0 = df1.iloc[:,1:13]
y1 = df1.iloc[:,13:] 

fig1= px.box(data_frame=y0,  title='Grid Electricity Consumption by Month')
fig1.update_traces(marker_color='green')
fig1.update_xaxes(title="FY2019-20")
fig1.update_yaxes(title="Electricity (kWh)")
fig1.update_layout(yaxis_range=[0,1000000])
#st.plotly_chart(fig1, theme=None, use_container_width=True)

fig1AA= px.box(data_frame=y1,  title='Grid Electricity Consumption by Month')
fig1AA.update_traces(marker_color='green')
fig1AA.update_xaxes(title="FY 2020-21")
fig1AA.update_yaxes(title="Electricity (kWh)")
fig1AA.update_layout(yaxis_range=[0,1000000])
#st.plotly_chart(fig1AA, theme=None, use_container_width=True)

#DG set electricity monthly
sheet_name_2 = "DG_set_monthly"
df2 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_2}")
y00 = df2.iloc[:,1:13]
y11 = df2.iloc[:,13:] 
fig2 = px.box(data_frame=y00,  title='DG Set Electricity Consumption by Month')
fig2.update_xaxes(title="FY 2019-20")
fig2.update_yaxes(title="Electricity (kWh)")
fig2.update_layout(yaxis_range=[0,27000])
#st.plotly_chart(fig2, theme=None, use_container_width=True)

fig2AA = px.box(data_frame=y11,  title='DG Set Electricity Consumption by Month')
fig2AA.update_xaxes(title="FY 2020-21")
fig2AA.update_yaxes(title="Electricity (kWh)")
fig2AA.update_layout(yaxis_range=[0,27000])
#st.plotly_chart(fig2, theme=None, use_container_width=True)


col1, col2 = st.columns(2)
with col1:    
    st.plotly_chart(fig1, theme=None, use_container_width=True)
    st.plotly_chart(fig2, theme=None, use_container_width=True)
    df1A = df1.set_index("Facility name")
    varA = st.selectbox("Select hospital",df1A.index, key="chart1")
    fig1A = px.bar(data_frame=df1A.loc[varA],  title='Grid Electricity Consumption by Month for ' + str(varA))
    fig1A.update_traces(marker_color='green')
    fig1A.update_xaxes(title="Months")
    fig1A.update_yaxes(title="Electricity (kWh)")
    fig1A. update(layout_showlegend=False)
    st.plotly_chart(fig1A, theme=None, use_container_width=True)
with col2:
    st.plotly_chart(fig1AA, theme=None, use_container_width=True)
    st.plotly_chart(fig2AA, theme=None, use_container_width=True)
    #bar chart -DG SET
    df2A = df2.set_index("Facility name")
    varB = st.selectbox("Select hospital",df2A.index, key="chart2")
    fig2A = px.bar(data_frame=df2A.loc[varB],  title='DG Set Electricity Consumption by Month for ' + str(varB))
    fig2A.update_xaxes(title="Months")
    fig2A.update_yaxes(title="Electricity (kWh)")
    fig2A. update(layout_showlegend=False)
    st.plotly_chart(fig2A, theme=None, use_container_width=True)


#area vs annual(kwh)
st.title("Building area Vs other parameters")
sheet_name_3 = "HVAC"
df3 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_3}")

st.dataframe(df3)
cola, colb,colc = st.columns(3)
with cola:
    variables_x=st.selectbox("Select x axis",df3.columns[1:],key="cola",index=5)
with colb:
    variables_y=st.selectbox("Select y axis",df3.columns[1:],key="colb")
with colc:
    colour=st.selectbox("Select third varible",df3.columns,key="colc",index=3)

fig3=px.scatter(df3, y= variables_y, x=variables_x,color =colour,trendline="ols", trendline_scope="overall",title= str(variables_x) + " Vs " + str(variables_y) + " with " + str(colour) +" wise")
st.plotly_chart(fig3, theme=None, use_container_width=True)
results = px.get_trendline_results(fig3).px_fit_results.iloc[0].rsquared
st.write("R-square Value is:", round(results,2) )

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
fig4 = px.pie(df4,values=df4.loc[hospital], names=df4.columns, title='Annual end-use system electricity consumption (in kWh)')
st.plotly_chart(fig4, theme=None, use_container_width=True)

st.title("Onsite solar PV")
#Solar PV Generation
sheet_name_5 = "Solar"
df5 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_5}")
col3, col4 = st.columns(2)
with col3:
    fig5= px.box(data_frame=df5.iloc[:,5:17],  title='Solar PV Generation Monthly')
    fig5.update_traces(marker_color='orange')
    fig5.update_xaxes(title="FY 2019-20")
    fig5.update_yaxes(title="Electricity (kWh)")
    st.plotly_chart(fig5, theme=None, use_container_width=True)
with col4:
    fig5AA= px.box(data_frame=df5.iloc[:,17:],  title='Solar PV Generation Monthly')
    fig5AA.update_traces(marker_color='orange')
    fig5AA.update_xaxes(title="FY 2020-21")
    fig5AA.update_yaxes(title="Electricity (kWh)")
    st.plotly_chart(fig5AA, theme=None, use_container_width=True)
    
#bar chart
df5A = df5.set_index("Facility name")
df5A = df5A.iloc[:,4:]
varC = st.selectbox("Select hospital",df5A.index, key="chart3" )
fig5A = px.bar(data_frame=df5A.loc[varC],  title='Solar PV Generation Monthly for ' + str(varC))
fig5A.update_traces(marker_color='orange')
fig5A.update_xaxes(title="Months")
fig5A.update_yaxes(title="Electricity (kWh)")
fig5A. update(layout_showlegend=False)
st.plotly_chart(fig5A, theme=None, use_container_width=True)

#scatter plot
#x1=df5.columns[2]
variables1=st.selectbox("Select year for y axis", ["2019-20_kwh_generation","2020-21_kwh_generation"])
fig5=px.scatter(df5, y= variables1, x="Peak capacity ", title= str("Peak capacity") + " Vs Generation in " + str(variables1), trendline="ols" )
fig5.update_xaxes(title="Peak capacity (kW)")
fig5.update_yaxes(title=variables1)
st.plotly_chart(fig5, theme=None, use_container_width=True)

# #KPIs
# st.title("Important KPIs")
# sheet_name_6 = "KPI"
# df6 = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_6}")
# df6 = df6.set_index("Facility name")
# df6 = df6.iloc[:,:7]
# col=df6.columns
# variables6=st.selectbox("Select variable", df6.columns,key="chart6")
# #variables7=st.selectbox("Select variable", df6.columns,key="chart7")
# fig6=px.scatter(df6, y= variables6, x=df6.index, title= str(variables6),height=800, color="Climate Zone" )
# #fig6.update_xaxes(title=variables6)
# fig6.update_yaxes(title=variables6)
# st.plotly_chart(fig6, theme=None, use_container_width=True)