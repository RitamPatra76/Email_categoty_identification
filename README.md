# Email Category Identification

## Overview

This project is a simple **Email category Identification** that predicts the category of an email based on its content. It is built using **Python, scikit-learn, and Streamlit**. The model is trained on a custom dataset and classifies emails into predefined categories such as **Meeting Request, Follow-up, Complaint, Job Offer, and Spam**.

## Features

- Classifies emails into predefined categories.
- Uses **TF-IDF vectorization** and a **Naïve Bayes classifier**.
- Lightweight and fast, ideal for real-world applications.
- Simple **Streamlit web interface** for user interaction.

## How I Created the Dataset

I manually created a dataset (`dataset.csv`) containing sample emails and their corresponding categories. The dataset follows a simple CSV format:

```csv
email_text,category
"Can we schedule a meeting for tomorrow?",Meeting Request
"Just following up on my last email.",Follow-up
"I have a complaint about your service.",Complaint
"We are offering you a job interview.",Job Offer
"Win a free iPhone! Click here now!",Spam
```

Since email texts might contain commas, they are enclosed in **double quotes** to ensure proper CSV parsing.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RitamPatra76/Email_categoty_identification.git
   cd Email_category_identification
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Training the Model

Run the `model_training.py` script to train the classifier:

```bash
python model_training.py
```

This will train the model and save it as `email_classifier.pkl`.

## Running the Streamlit App

Start the web app using Streamlit:

```bash
streamlit run streamlit_app.py
```

Then, enter an email text in the provided text area, and the app will classify it into one of the predefined categories.

## Project Structure

```
EMAIL_CATEGORY/
│── dataset.csv           # Custom dataset created manually
│── email_classifier.pkl  # Trained model file
│── model_training.py     # Script to train the model
│── streamlit_app.py      # Streamlit web application
│── requirements.txt      # List of dependencies
│── README.md             # Project documentation
```

## Future Improvements

- Expand the dataset with more real-world emails.
- Implement **BERT-based classification** for improved accuracy.
- Add support for **multilingual email classification**.

##
