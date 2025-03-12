import streamlit as st
st.set_page_config(page_title="Multi-Task App", layout="centered")
task = st.sidebar.radio(
    "Choose a task", ["Calculator", "User Registration"])


# 1) Task: Simple Calculator using Streamlit

# Streamlit UI
if task == "Calculator":
    st.title("Simple Calculator")

    # Input Fields
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", step=1.0)
    with col2:
        num2 = st.number_input("Enter second number", step=1.0)

    # select operation
    operation = st.radio("Choose an operation:", [
        "Addition", "Subtraction", "Multiplication", "Division"])

    # Perform calculation
    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

        st.success(f"Result: {result:.2f}")


# 2) Task: Basic Form (User Registration)
elif task == "User Registration":
    st.title("User Registration Form ")

    # Input fields
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    age = st.number_input("Enter your age", step=1, min_value=1, max_value=80)

    # Submit button
    if st.button("Submit"):
        if name and email and age:
            st.success(f"Thank you, {name}!")
            st.write(f"Email: {email}")
            st.write(f"Age: {age}")
    else:
        st.warning("Please fill in all fields before submitting!")
