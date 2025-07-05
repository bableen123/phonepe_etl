import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="PhonePe Insights Dashboard", layout="wide")
st.title("📊 PhonePe Data Insights Dashboard")

# Load pre-executed query results
datasets = {
    "q1": pd.read_csv("q1.csv"),
    "q2": pd.read_csv("q2.csv"),
    "q3": pd.read_csv("q3.csv"),
    "q4": pd.read_csv("q4.csv"),
    "q5": pd.read_csv("q5.csv"),
    "q6": pd.read_csv("q6.csv"),
    "q7": pd.read_csv("q7.csv"),
    "q8": pd.read_csv("q8.csv"),
    "q9": pd.read_csv("q9.csv")
}

# Helper function for section layout
def section(title, fig):
    with st.container():
        st.markdown(f"### {title}")
        st.pyplot(fig)
        st.markdown("---")

# 1. Total Transaction Amount by Year
fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.barplot(data=datasets["q1"], x='year', y='total_amount', hue='year', palette='Blues_d', ax=ax1)
ax1.set_title("Total Transaction Amount by Year")
ax1.set_ylabel("Amount (in ₹ Crores)")
ax1.set_xlabel("Year")
ax1.legend().set_visible(False)
section("1. Total Transaction Amount by Year", fig1)

# 2. App Opens by Device Brand
fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.barplot(data=datasets["q2"].head(10), x='brand', y='total_opens', hue='brand', palette='Purples', ax=ax2)
ax2.set_title("Top 10 Brands by App Opens")
ax2.set_ylabel("Total App Opens")
ax2.set_xlabel("Device Brand")
ax2.legend().set_visible(False)
ax2.tick_params(axis='x', rotation=45)
section("2. App Opens by Device Brand", fig2)

# 3. Insurance Growth by State
fig3, ax3 = plt.subplots(figsize=(10, 4))
sns.lineplot(data=datasets["q3"].head(10), x='state', y='total_value', marker='o', color='green', ax=ax3)
ax3.set_title("Top States by Insurance Value")
ax3.set_ylabel("Total Insurance Value (₹ Crores)")
ax3.set_xlabel("State")
ax3.tick_params(axis='x', rotation=45)
section("3. Insurance Value Growth by State", fig3)

# 4. Transaction Share by State (Pie Chart)
fig4, ax4 = plt.subplots(figsize=(6, 6))
ax4.pie(datasets["q4"]["total_transaction_value"].head(10),
        labels=datasets["q4"]["state"].head(10),
        autopct='%1.1f%%', startangle=140)
ax4.set_title("Top 10 States by Transaction Share")
section("4. Transaction Share by State", fig4)

# 5. Registered Users by State
fig5, ax5 = plt.subplots(figsize=(10, 4))
sns.barplot(data=datasets["q5"].head(10), x='state', y='total_users', hue='state', palette='rocket', ax=ax5)
ax5.set_title("Top States by Registered Users")
ax5.set_ylabel("Registered Users")
ax5.set_xlabel("State")
ax5.tick_params(axis='x', rotation=45)
ax5.legend().set_visible(False)
section("5. Top 10 States by Registered Users", fig5)

# 6. Insurance Transactions by State
fig6, ax6 = plt.subplots(figsize=(10, 4))
sns.barplot(data=datasets["q6"].head(10), x='state', y='insurance_transactions', hue='state', palette='crest', ax=ax6)
ax6.set_title("Top States by Insurance Count")
ax6.set_ylabel("Insurance Count")
ax6.set_xlabel("State")
ax6.tick_params(axis='x', rotation=45)
ax6.legend().set_visible(False)
section("6. Top 10 States by Insurance Transactions", fig6)

# 7. Transaction Amount by District
fig7, ax7 = plt.subplots(figsize=(10, 4))
sns.lineplot(data=datasets["q7"].head(10), x='state', y='total_transaction_amount', marker='o', color='blue', ax=ax7)
ax7.set_title("Top Districts by Transaction Amount")
ax7.set_ylabel("Transaction Amount (₹)")
ax7.set_xlabel("District")
ax7.tick_params(axis='x', rotation=45)
section("7. Top 10 Districts by Transaction Amount", fig7)

# 8. Registered Users by District
fig8, ax8 = plt.subplots(figsize=(10, 4))
sns.barplot(data=datasets["q8"].head(10), x='district', y='registered_users', hue='district', palette='mako', ax=ax8)
ax8.set_title("Top Districts by Registered Users")
ax8.set_ylabel("Registered Users")
ax8.set_xlabel("District")
ax8.tick_params(axis='x', rotation=45)
ax8.legend().set_visible(False)
section("8. Top 10 Districts by Registered Users", fig8)

# 9. Insurance Transactions by Pincode
fig9, ax9 = plt.subplots(figsize=(10, 4))
sns.barplot(data=datasets["q9"].head(10), x='pincode', y='insurance_transactions', hue='pincode', palette='flare', ax=ax9)
ax9.set_title("Top Pincodes by Insurance Transactions")
ax9.set_ylabel("Transaction Count")
ax9.set_xlabel("Pincode")
ax9.tick_params(axis='x', rotation=45)
ax9.legend().set_visible(False)
section("9. Top 10 Pincodes by Insurance Transactions", fig9)

st.success("All visualizations loaded successfully!")
