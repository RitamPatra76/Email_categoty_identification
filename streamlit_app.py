import streamlit as st
import pickle

# calling the already saved pretrained model
with open("email_classifier.pkl", "rb") as f:
    model = pickle.load(f)

# Building the UI using streamlit
st.title("Email Intent Classifier")

email_text = st.text_area("Enter email content:")

if st.button("Classify Email"):
    if email_text.strip():
        prediction = model.predict([email_text])[0]
        st.success(f"Predicted Category: **{prediction}**")
    else:
        st.warning("Please enter some email text.")
