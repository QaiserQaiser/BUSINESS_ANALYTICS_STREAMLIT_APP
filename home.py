import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Dashboard", page_icon="", layout="wide")

# Page header
st.header("STATISTICS FOR INFORMATION ANALYSIS")
st.subheader("PYTHON QUERY OPERATIONS")

# Load dataset from HDD
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# Side navigation
st.sidebar.image("logo1.png")

# Print dataset
with st.expander("Show Dataset"):
    st.dataframe(df, use_container_width=True)

#QUERY NO 1:
with st.expander("**QUERY 1:** Select count **States** by Frequency"):
    state_count=df["State"].value_counts().reset_index()
    state_count.columns=["State","Frequency"]
    st.write("Count of States by Frequency:")
    st.dataframe(state_count,use_container_width=True)

#QUERY NO 2:
with st.expander("**QUERY 2:** select count **States** by frequency and show a simple bar graph"):
    fig=px.bar(state_count,x="State",y="Frequency",labels={'x':'State','y':'Frequency'})
    fig.update_layout(showlegend=True)
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    st.plotly_chart(fig,use_container_width=True)


#QUERY NO 3:
with st.expander("*QUERY 3:* Select count *BusinessType* by frequency"):

    state_count2 = df["BusinessType"].value_counts().reset_index()

    state_count2.columns = ["BusinessType", "Frequency"]

    st.write("Count of BusinessType by Frequency:")

    st.dataframe(state_count2, use_container_width=True)



#QUERY NO 4:
with st.expander("QUERY 4: select count BusinessType by frequency and show simple bar graph"):

    BusinessType = df["BusinessType"].value_counts().reset_index()

    BusinessType.columns = ["BusinessType", "Frequency"]

    fig = px.bar(BusinessType, x="BusinessType", y="Frequency", labels={'x': 'BusinessType', 'y': 'Frequency'})

    fig.update_layout(showlegend=True)
    
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    st.plotly_chart(fig, use_container_width=True)

#QUERY NO 5:
# Descriptive statistics

# Max
with st.expander("QUERY 5: select Max *Investment* and Max *Rating* where *State* is Mwanza and date is range from 2021-01-02 to 2021-01-16"):

    query_5 = df[(df["State"] == "Mwanza") & 
                 (df["Expiry"] >= '2021-01-02') & 
                 (df["Expiry"] >= '2021-01-16')][['Investment', 'Rating']]
    st.dataframe(query_5)


# Query no 6

with st.expander("*QUERY 6:* Select count *State* where State is 'Dodoma'"):

    count_state = df[df["State"] == "Dodoma"]["State"].count()

    st.info(f"## {count_state}")


# Query no 7

with st.expander("*QUERY 7:* Select count *State* and *Region* where *State* is 'Dodoma' and *Region* is 'East'"):

    count_region = df[(df["State"] == "Dodoma") & (df["Region"] == "East")]['Region'].count()

    st.info(f"## {count_region}")

#8
with st.expander("QUERY 8: Select count **State** and **Region** where Location ='Dodoma' and Region='East' and **Investment** is greater than 300,000"):
    count_state = df[(df["State"] == "Dodoma") & 
                     (df["Region"] == "East") & 
                     (df["Investment"] >= 300008)]["Location"].count()

    st.info(f"## {count_state}")


# Query 9

with st.expander("*QUERY 9:* Select average mean of investment where *State* is 'Dodoma' and *Location* is not 'Urban'"):

    avg = df[(df["State"] == "Dodoma") & 
             (df["Location"] != "Urban")]["Investment"].mean()

    st.info(f"Average Investment: {avg}")


# Query 10

with st.expander("QUERY 10: Select summation of investment where Expiry is a date range from 2021-01-02 to 2021-01-16 and State is 'Dodoma'"):

    summation = df[(df["Expiry"] >= '2021-01-02') & 
                   (df["Expiry"] <= '2021-01-16') & 
                   (df["State"] == "Dodoma")]["Investment"].sum()

    st.info(f"Summation of Investment: {summation}")


# Query 11

with st.expander("QUERY 11: Select the median of Investment and Rating where State is Mwanza, Location is Urban, and Investment is greater than 400000"):

    median = df[(df["State"] == "Mwanza") & 
                (df["Location"] == "Urban") & 
                (df["Investment"] > 400000)][['Investment', 'Rating']].median()

    st.dataframe(median)


# Query 12

with st.expander("QUERY 12: Select the median of Investment and Rating where State is Mwanza, Location is Urban, Investment is greater than or equal to 400000, and Expiry is between 2021-01-02 and 2021-01-16"):

    median2 = df[(df["State"] == "Mwanza") & 
                 (df["Location"] == "Urban") & 
                 (df["Investment"] >= 400000) & 
                 (df["Expiry"] >= '2021-01-02') & 
                 (df["Expiry"] <= '2021-01-16')][['Investment', 'Rating']].median()

    st.dataframe(median2)


# Query 13

st.success("*Select by Tabular*")

with st.expander("QUERY 13: Select all from State where State = 'Dodoma'"):

    st.dataframe(df[df["State"] == "Dodoma"], use_container_width=True)


#Query 14
with st.expander("QUERY 14: Select all from State and Region where State ='Dodoma' and Region='East'"):
    result_query_14 = df[(df['State'] == 'Dodoma') & (df['Region'] == 'East')]
    st.dataframe(result_query_14)


#Query 15
with st.expander('QUERY 15: Select all from State and Region where State ="Dodoma"and Region="East" and Investment is greater than 300,000'):
    result_query_15 = df[(df['State'] == 'Dodoma') & (df['Region'] == 'East') & (df['Investment'] > 300000)]
    st.dataframe(result_query_15)


#Query 16
with st.expander('QUERY 16: Select all investment where State="Dodoma" and Location is not"Urban"'):
    result_query_16 = df[(df['State'] == 'Dodoma') & (df['Location'] != 'Urban')]['Investment']
    st.dataframe(result_query_16)

#Query 17
with st.expander('QUERY 17: select at least 5 High frequency of Investment where Expiry is a daterange from 2-jan-21 to 16-jan-21'):
    # Assuming 'Expiry' is in datetime format
    df['Expiry'] = pd.to_datetime(df['Expiry'])
    date_range = (df['Expiry'] >= '2021-01-02') & (df['Expiry'] <= '2021-01-16')

    result_query_17 = df[date_range].nlargest(5, 'Investment')

    st.dataframe(result_query_17)


#Query 18 not correct
with st.expander('QUERY 18: select all investments where Expiry is a date range from 2-jan-21 to16-jan-21 and region is Dodoma'):
    result_query_18 = df[(df['Expiry'] >= '2021-01-02') & (df['Expiry'] <= '2021-01-16') & (df['Region'] == 'Dodoma')]['Investment']
    st.dataframe(result_query_18)


#Query 19:
with st.expander("QUERY 19: select State, Region, Location and BusinessType where Region is 'East'and investment greater than 2219900 and BusinessType is not 'Other' and Construction is Frame or FireResist and State is 'Dar es Salaam' or 'Dodoma'"):
    result_query_19 = df[
    (df['Region'] == 'East') &
    (df['Investment'] > 2219900) &
    (df['BusinessType'] != 'Other') &
    (df['Construction'].isin(['Frame', 'FireResist'])) &
    (df['State'].isin(['Dar es Salaam', 'Dodoma']))
    ][['State', 'Region', 'Location', 'BusinessType']]

    st.dataframe(result_query_19)



#Query 20:
# Assuming `df` is your DataFrame containing the 'Investment' column
with st.expander("QUERY 20: Box plot to show quartiles with specified settings"):
    # Create the box plot with custom colors
    fig, ax = plt.subplots()
    
    # Customize the colors for different parts of the box plot
    boxprops = dict(color='blue', linewidth=2)   # Box color
    whiskerprops = dict(color='green', linewidth=2)  # Whisker color
    medianprops = dict(color='red', linewidth=2)  # Median line color
    capprops = dict(color='purple', linewidth=2)  # Cap color
    
    ax.boxplot(df['Investment'], 
               boxprops=boxprops, 
               whiskerprops=whiskerprops, 
               medianprops=medianprops, 
               capprops=capprops)
    
    ax.set_title('Box plot of Investment')
    ax.set_ylabel('Investment')

    # Display the plot in Streamlit
    st.pyplot(fig)



   













    
