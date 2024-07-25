import pickle
import streamlit as st

# Membaca model
try:
    with open('transaction_model.sav', 'rb') as file:
       transaction_model = pickle.load(file)
except FileNotFoundError:
    st.error("File model tidak ditemukan. Pastikan file berada di jalur yang benar.")
except Exception as e:
    st.error(f"Error saat memuat model: {e}")

# Function to validate if the input is an integer
def is_valid_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Function to simulate prediction logic
def predict(sender_name, receiver_name, amount):
    # Placeholder logic for prediction
    # You can replace this with actual model prediction logic
    if int(amount) > 500:
        return 1  # success
    else:
        return 0  # failed

# Title of the application
st.title("UPI Payment Transactions Input")

# Form for user input
with st.form(key='upi_form'):
    sender_name = st.text_input("Sender Name")
    receiver_name = st.text_input("Receiver Name")
    amount = st.text_input("Amount (INR)")

    # Submit button for the form
    submit_button = st.form_submit_button(label='Prediksi')

# Validation and prediction logic after form submission
if submit_button:
    if (is_valid_integer(sender_name) and is_valid_integer(receiver_name) and is_valid_integer(amount)):
        
        st.success("All inputs are valid integers.")
        
        # Perform prediction
        prediction = predict(sender_name, receiver_name, amount)
        
        # Display prediction result
        if prediction == 1:
            st.success("Predicted Status: Success (1)")
        else:
            st.error("Predicted Status: Failed (0)")
    else:
        st.error("Please enter valid integer values.")