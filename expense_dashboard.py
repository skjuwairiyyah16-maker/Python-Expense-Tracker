import streamlit as st
# Page settings
st.set_page_config(
    page_title="Expense Tracker",
    layout="wide"
)

# Dashboard title
st.title("💜 Personal Expense Tracker")

st.write("Welcome to your Expense Tracker Dashboard!")

# Financial overview
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Income", "₹50,000")
col2.metric("Total Expenses", "₹20,000")
col3.metric("Savings", "₹30,000")
col4.metric("Savings Rate", "60%")

st.success("Your dashboard is working!")

# Monthly Expenses Chart

import pandas as pd
import plotly.express as px

st.subheader("📊 Monthly Expenses")

data = {
    "Month": [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ],
    "Expenses": [
        2000, 3500, 2500, 4000,
        3000, 4500, 2800, 3500,
        4200, 3200, 5000, 3800
    ]
}

df = pd.DataFrame(data)

fig = px.line(
    df,
    x="Month",
    y="Expenses",
    title="Expenses by Month",
    markers=True,
    color_discrete_sequence=["#8A2BE2"]
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Amount (₹)",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

# Expense Category Donut Chart

st.subheader("🍩 Expenses by Category")

category_data = {
    "Category": [
        "Food",
        "Shopping",
        "Travel",
        "Bills",
        "Entertainment"
    ],
    "Amount": [
        5000,
        4000,
        3000,
        5000,
        3000
    ]
}

category_df = pd.DataFrame(category_data)

fig2 = px.pie(
    category_df,
    names="Category",
    values="Amount",
    hole=0.5,
    title="Expense Distribution",
    color_discrete_sequence=[
        "#6A0DAD",
        "#9370DB",
        "#BA55D3",
        "#D8BFD8",
        "#E6E6FA"
    ]
)

st.plotly_chart(fig2, use_container_width=True)


# Category-wise Expense Table

st.subheader("📋 Expense Details")

expense_details = {
    "Category": [
        "Food",
        "Shopping",
        "Travel",
        "Bills",
        "Entertainment",
        "Education",
        "Healthcare"
    ],
    "Amount (₹)": [
        5000,
        4000,
        3000,
        5000,
        2000,
        2500,
        1500
    ]
}

expense_df = pd.DataFrame(expense_details)

st.dataframe(
    expense_df,
    use_container_width=True,
    hide_index=True
)

st.subheader("💰 Total Expenses by Category")

st.bar_chart(
    expense_df,
    x="Category",
    y="Amount (₹)",
    color="#9370DB"
)

st.header("➕ Add New Expense")

category = st.selectbox(
    "Select Category",
    ["Food", "Shopping", "Travel", "Bills",
     "Entertainment", "Education", "Healthcare"]
)

amount = st.number_input(
    "Enter Amount (₹)", min_value=0
)

date = st.date_input("Expense Date")

if st.button("Add Expense"):
    st.success("Expense added successfully!")