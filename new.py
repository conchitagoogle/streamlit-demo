import streamlit as st
import pandas as pd
import numpy as np
# import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

DATA_URL = (
    "IBM.csv"
)

st.title("Data Visualization: IBM HR Analytics Employee Attrition & Performance")

st.sidebar.title("IBM HR Analytics Employee Attrition & Performance")

st.markdown("This application is a Streamlit dashboard used "
            "to analyze IBM HR Analytics Employee Attrition & Performance")
st.sidebar.markdown("This application is a Streamlit dashboard used "
            "to analyze IBM HR Analytics Employee Attrition & Performance")


@st.cache_data(persist=True)
def load_data():
    df = pd.read_csv(DATA_URL)
    
    return df

df = load_data()

st.sidebar.markdown('Univariate Analysis')
a = st.sidebar.selectbox('Tasks', ['Task 1', 'Task 2'], key='20')

if not st.sidebar.checkbox("Hide", True,key='4'):
    if a == 'Task 1':
        st.write('What is the distribution of the Age & MothlyIncome columns in the data set?')
        sns.distplot(df['Age'])
        st.pyplot()
        st.header('Observation:')
        st.subheader('We have Employees mostly between the age of 30 to 45')

        sns.distplot(df['MonthlyIncome']) 
        st.pyplot()
        st.header('Observation:')
        st.subheader('Most of the Employees in the company earn between 2000 and 7000 monthly')
        st.subheader('Very few Employees command a higher salary')
        st.set_option('deprecation.showPyplotGlobalUse', False)


    if a == 'Task 2':
        st.write('Which Department of the company has the highest Attrition rate?')
        sns.countplot(data=df,x=df['Department'],hue="Attrition")
        st.pyplot()
        st.header('Observation:')
        st.subheader('Attrition raltes are high in Sales Deparment, and R&D Department as compared to HR where the attrition rate is significantly lower')


st.sidebar.markdown('Bi-variate Analysis')
a = st.sidebar.selectbox('Insights', ['Task 1', 'Task 2', 'Task 3', 'Task 4'], key='2')

if not st.sidebar.checkbox("Hide", True, key='5'):
    if a == 'Task 1':
        st.write('Which gender is more likely to leave?')
        f,ax = plt.subplots()
        new_df = df["Gender"].groupby(df["Attrition"]).value_counts(normalize = True).rename("Percentage of group").reset_index()

        sns.barplot(x = "Attrition", y = "Percentage of group", hue = "Gender", data = new_df)

        vals = ax.get_yticks()
        ax.set_yticklabels(['{:,.0%}'.format(x) for x in vals])

        ax.set(title = "Distribution of gender")
        st.pyplot()
        st.header('Observation:')
        st.subheader('The company has more men than women, and so this plot tells us that men tend to leave the company more but only because they are in a larger number. This also indicates that gender might not be a key factor for employee attrition')

    if a == 'Task 2':
        st.write('Does Job Level of employees influence Attrition rate?')
        sns.swarmplot(x="JobLevel", y="MonthlyIncome", hue="Attrition", data=df);
        st.pyplot()
        st.header('Observation:')
        st.subheader('Attrition rate is highest in employees at Job Level 1 positions')
        st.subheader('It is significant to note that as Job Level increases, monthly income also increases. With the increase in Job Level (or Monthly Income), Attrition Rate decreases')


    if a == 'Task 3':
        st.write('Which Employees are more likely to leave? Senior Employees or Recent Joinees, and does the years spent at the company affect Attrition?')
        sns.scatterplot(x=df['MonthlyIncome'],y=df['YearsAtCompany'],hue=df['Attrition'])
        st.pyplot()
        st.header('Observation:')
        st.subheader('Senior Employees with higher MonthlyIncome who have spent more number of years at company are less likely to leave as compared to recent joinees\n New Employees (less than 2 years at Company) with less MonthlyIncome are more likely to quit')

    if a == 'Task 4':
        st.write('Are Employees in a particular Job Role more likely to quit?')
        sns.swarmplot(x="JobRole", y="MonthlyIncome",hue="Attrition" ,data=df)
        plt.xticks( rotation=10 )
        st.pyplot()
        st.header('Observation:')
        st.subheader('Sales Representative employees are more likely to quit the organization whereas employees in Research Director & Manager position are less likely to leave')
        st.subheader('It is significant to note that Job Roles that command a Higher Monthly Income (Research Director & Manager) are less likely to quit as compared to those with Low Monthly Income (Sales Representative)')
        st.subheader('Attrition is high in job roles that command Low Monthly Income such as Sales Executive, Research Scientist, Laboratory Technician, Sales Representative, and Human Resources')


    if a == 'Task 5':
        st.write('Does Job Level of employees influence Attrition rate?')
        sns.swarmplot(x="JobLevel", y="MonthlyIncome", hue="Attrition", data=df);
        st.pyplot()
        st.header('Observation:')
        st.subheader('Attrition rate is highest in employees at Job Level 1 positions')
        st.subheader('It is significant to note that as Job Level increases, monthly income also increases. With the increase in Job Level (or Monthly Income), Attrition Rate decreases')

