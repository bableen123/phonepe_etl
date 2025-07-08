# Streamlit Dashboard Layout by Query-wise Visualization
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="PhonePe Transaction Dashboard", layout="wide")
st.title("PhonePe Insights & Growth Analysis")

# Load Data
datasets = {
    "q1": pd.read_csv("q1.csv"),
    "q2": pd.read_csv("q2.csv"),
    "q3": pd.read_csv("q3.csv"),
    "q4": pd.read_csv("q4.csv"),
    "q5": pd.read_csv("q5.csv"),
    "q6": pd.read_csv("q6.csv"),
    "q7": pd.read_csv("q7.csv"),
    "q8": pd.read_csv("q8.csv")
}

def render_plot(title, fig):
    st.markdown(f"#### {title}")
    st.pyplot(fig)
    st.markdown("---")

# ==== QUERY 1 ====
col1, col2 = st.columns(2)
with col1:
    q1_grouped = datasets["q1"].groupby("year")["total_amount"].sum().reset_index()
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=q1_grouped, x='year', y='total_amount', palette='Blues_d', ax=ax1)
    ax1.set_title("1a. Total Transaction Amount by Year")
    ax1.set_ylabel("Amount (₹ Crores)")
    st.pyplot(fig1)

with col2:
    category_agg = datasets["q1"].groupby("category")["total_count"].sum().reset_index().sort_values(by='total_count', ascending=False)
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=category_agg, x='category', y='total_count', palette='coolwarm', ax=ax2)
    ax2.set_title("1b. Service Usage by Category")
    ax2.set_ylabel("Transaction Count")
    ax2.set_xlabel("Category")
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

# ==== QUERY 2 ====
col3, col4 = st.columns(2)
with col3:
    q2_sorted = datasets["q2"].sort_values(by='total_users', ascending=False)
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=q2_sorted, x='brand', y='total_users', palette='viridis', ax=ax3)
    ax3.set_title("2a. Top Device Brands by Registered Users")
    ax3.set_ylabel("Users")
    ax3.set_xlabel("Brand")
    ax3.tick_params(axis='x', rotation=45)
    st.pyplot(fig3)

with col4:
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=datasets["q2"], x='brand', y='total_opens', palette='Purples', ax=ax4)
    ax4.set_title("2b. App Opens by Device Brand")
    ax4.set_ylabel("Total App Opens")
    ax4.set_xlabel("Device Brand")
    ax4.tick_params(axis='x', rotation=45)
    st.pyplot(fig4)

# ==== QUERY 3 ====
fig5, ax5 = plt.subplots(figsize=(12, 4))
sns.barplot(data=datasets["q3"], x='state', y='total_value', hue='year', palette='Oranges', ax=ax5)
ax5.set_title("3a. Insurance Transaction Value Growth by State")
ax5.set_ylabel("Total Insurance Value")
ax5.set_xlabel("State")
ax5.tick_params(axis='x', rotation=90)
st.pyplot(fig5)

col5, col6 = st.columns(2)
with col5:
    q3_sorted = datasets["q3"].sort_values(by='total_value', ascending=False).head(10)
    fig6, ax6 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=q3_sorted, x='state', y='total_value', palette='Greens', ax=ax6)
    ax6.set_title("3b. Top States by Insurance Value")
    ax6.set_ylabel("Value (₹ Crores)")
    ax6.tick_params(axis='x', rotation=90)
    st.pyplot(fig6)

with col6:
    fig7, ax7 = plt.subplots(figsize=(6, 4))
    sns.lineplot(data=q3_sorted, x='state', y='total_value', marker='o', color='green', ax=ax7)
    ax7.set_title("3c. Insurance Value Growth by State")
    ax7.set_ylabel("Total Insurance Value")
    ax7.tick_params(axis='x', rotation=90)
    st.pyplot(fig7)

# ==== Remaining queries retained as before ====
# QUERY 4
col7, col8 = st.columns(2)
with col7:
    q4_sorted = datasets["q4"].sort_values(by='total_transaction_value', ascending=False).head(10)
    fig8, ax8 = plt.subplots(figsize=(6, 6))
    ax8.pie(q4_sorted['total_transaction_value'], labels=q4_sorted['state'], autopct='%1.1f%%', startangle=140)
    ax8.set_title("4a. Transaction Share by State")
    st.pyplot(fig8)

with col8:
    fig9, ax9 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=q4_sorted, x='state', y='total_transaction_value', palette='Oranges', ax=ax9)
    ax9.set_title("4b. Top States by Transaction Value")
    ax9.set_ylabel("Transaction Value")
    ax9.tick_params(axis='x', rotation=45)
    st.pyplot(fig9)

# QUERY 5
col9, col10 = st.columns(2)
with col9:
    fig10, ax10 = plt.subplots(figsize=(6, 4))
    q5_sorted = datasets["q5"].sort_values(by='total_users', ascending=False).head(10)
    sns.barplot(data=q5_sorted, x='state', y='total_users', palette='rocket', ax=ax10)
    ax10.set_title("5a. Top States by Registered Users")
    ax10.set_ylabel("Users")
    ax10.tick_params(axis='x', rotation=45)
    st.pyplot(fig10)

with col10:
    q5_grouped = datasets["q5"].groupby(['state', 'year'])['total_users'].sum().reset_index()
    top_states = q5_grouped.groupby('state')['total_users'].sum().nlargest(5).index
    q5_top = q5_grouped[q5_grouped['state'].isin(top_states)]
    fig11, ax11 = plt.subplots(figsize=(6, 4))
    sns.lineplot(data=q5_top, x='year', y='total_users', hue='state', marker='o', palette='tab10', ax=ax11)
    ax11.set_title("5b. Registered Users Over Time – Top States")
    ax11.set_ylabel("Users")
    st.pyplot(fig11)

# QUERY 6
q6_grouped = datasets["q6"].groupby(['state', 'year'])['total_insurance_amount'].sum().reset_index()
top_insurance_states = q6_grouped.groupby('state')['total_insurance_amount'].sum().nlargest(5).index
q6_top = q6_grouped[q6_grouped['state'].isin(top_insurance_states)]
fig12, ax12 = plt.subplots(figsize=(12, 5))
sns.lineplot(data=q6_top, x='year', y='total_insurance_amount', hue='state', marker='o', palette='Set2', ax=ax12)
ax12.set_title("6. Insurance Amount Over Years – Top States")
st.pyplot(fig12)

# QUERY 7
fig13, ax13 = plt.subplots(figsize=(12, 5))
sns.lineplot(data=datasets["q7"].head(10), x='state', y='total_transaction_amount', marker='o', color='blue', ax=ax13)
ax13.set_title("7. Top Districts by Transaction Amount")
st.pyplot(fig13)

# QUERY 8
q8_sorted = datasets["q8"].sort_values(by='registered_users', ascending=False)
fig14, ax14 = plt.subplots(figsize=(12, 5))
sns.barplot(data=q8_sorted, x='district', y='registered_users', palette='mako', ax=ax14)
ax14.set_title("8. Top Districts by Registered Users")
ax14.tick_params(axis='x', rotation=45)
st.pyplot(fig14)

