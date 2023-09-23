import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt 

st.set_page_config(
    page_icon="🧊",
    page_title="Diwali sales analysis",
    layout="wide")
# Load your dataset
df = pd.read_csv('F:\diwali sales analysis\Python_Diwali_Sales_Analysis-main\data.csv', encoding='unicode_escape')

# Add Streamlit app title and header
st.title('Diwali Sales Analysis')

# Display data summary
st.write('## Data Summary')
st.write('Shape of the dataset:', df.shape)
st.write(df.head())

# Add interactive visualizations using Streamlit components
st.write('## Visualizations')

# Countplot for Gender
def save_plot_as_image(figure, filename):
    figure.savefig(filename, bbox_inches='tight')
    st.image(filename)

# Countplot for Gender
st.subheader('Gender Distribution')
gender_countplot = sns.countplot(x='Gender', data=df)
save_plot_as_image(gender_countplot.get_figure(), 'gender_distribution.png')

# Countplot for Age Group
st.subheader('Age Group Distribution')
age_group_countplot = sns.countplot(data=df, x='Age Group', hue='Gender')
save_plot_as_image(age_group_countplot.get_figure(), 'age_group_distribution.png')

# State-wise Orders
st.subheader('State-wise Orders')
state_orders = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False)
st.bar_chart(state_orders.set_index('State')['Orders'])

# State-wise Total Sales/Amount
st.subheader('State-wise Total Sales/Amount')
state_sales = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
st.bar_chart(state_sales.set_index('State')['Amount'])

def save_seaborn_plot_as_image(figure, filename):
    figure.savefig(filename, bbox_inches='tight')
    st.image(filename)

st.subheader('Marital Status Distribution')
marital_status_countplot = sns.countplot(data=df, x='Marital_Status')
save_seaborn_plot_as_image(marital_status_countplot.get_figure(), 'marital_status_distribution.png')

# Marital Status Distribution
st.subheader('Marital Status Distribution')
marital_status_countplot = sns.countplot(data=df, x='Marital_Status')
save_seaborn_plot_as_image(marital_status_countplot.get_figure(), 'marital_status_distribution.png')

# Marital Status vs. Amount with Gender hue
st.subheader('Marital Status vs. Amount with Gender Hue')
marital_status_vs_amount = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
st.bar_chart(marital_status_vs_amount.set_index('Marital_Status')['Amount'])

# Occupation Distribution
st.subheader('Occupation Distribution')
plt.figure(figsize=(19, 5))
occupation_countplot = sns.countplot(data=df, x='Occupation')
save_seaborn_plot_as_image(occupation_countplot.get_figure(), 'occupation_distribution.png')

# Top 10 Most Sold Products
st.subheader('Top 10 Most Sold Products')
top_10_products = df.groupby(['Product_Category'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
st.bar_chart(top_10_products.set_index('Product_Category')['Orders'])
# You can add more visualizations or interactivity as needed

