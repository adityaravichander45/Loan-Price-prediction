import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

st.title("Loan Price Prediction")

class CustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        print('\n>>>>>>>init() called.\n')
    def fit(self, X, y = None):
        print('\n>>>>>>>fit() called.\n')
        return self
    def transform(self, X, y = None):
        print('\n>>>>>>>transform() called.\n')
        print("\n>>>> Input : ",X)
        X_ = X.applymap(lambda x: x.lower())
        print("\n>>>> Output : ",X_)
        print("\n>>>>>>> Custom Transformer Called")
        return X_

model = joblib.load('model.pkl')

data = pd.read_csv('train.csv')

print(pd)

def predict_subscribe(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Loan_Status):

# get column names
    col_names = ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']

# get column values
    col_values = [ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Status,
       Loan_Amount_Term,Credit_History]

# dataframe
    test = pd.DataFrame([col_values])
    test.columns = col_names 

# calling the predict model 
    predicted = model.predict(test)
    return predicted

def main():
# creating a title
    st.title("Hackathon")

# creating a heading
    html_tmp = """
<div style='background-color:red;'>
<h2 style='color:white;text-align:center;'>Subscriber Prediction App</h2>
</div>
"""
    st.markdown(html_tmp, unsafe_allow_html=True)

Property_area = st.selectbox(
   "What is the property area for the loan?",
   ("Rural", "Urban", "Semi urban"),
   index=None,
   placeholder="Select the Property area...",
)

st.write('You selected:', Property_area)

Dependents = st.selectbox(
   "How many dependents are there for the loan?",
   ("0", "1", "2",'3+'),
   index=None,
   placeholder="Select the dependents...",
)

st.write('You selected:', Dependents)

Gender = st.selectbox(
   "What is your gender?",
   ("Male", "Female"),
   index=None,
   placeholder="Select your gender...",
)

st.write('You selected:', Gender)


Married = st.selectbox(
   "Are you married?",
   ("Yes", "No"),
   index=None,
   placeholder="Select your option...",
)

st.write('You selected:', Married)

Loan_Amount_Term = st.selectbox(
   "What is the term of the loan amount?",
   ('360','120','180','60','300','480','240','36','84'),
   index=None,
   placeholder="Select the term of the loan amount...",
)

st.write('You selected:', Loan_Amount_Term)


Education = st.selectbox(
   "Are you educated?",
   ('Graduate','Not Graduate'),
   index=None,
   placeholder="Select the qualification...",
)

st.write('You selected:', Education)


Credit_History = st.selectbox(
   "What is credit history?",
   ('0','1'),
   index=None,
   placeholder="Select the qualification...",
)

st.write('You selected:', Credit_History)


ApplicantIncome = number = st.number_input("Enter the Applicant Income", value=None, placeholder="Type the amount...")

st.write('You selected:', ApplicantIncome)


CoapplicantIncome = number = st.number_input("Enter the CoapplicantIncome", value=None, placeholder="Type the amount...")

st.write('You selected:', CoapplicantIncome)


LoanAmount = number = st.number_input("Enter the loan amount", value=None, placeholder="Type the amount...")

st.write('You selected:', LoanAmount)

# creating a button click to call the predict method
result=""
if st.button("Predict"):
    result=predict_subscribe(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,
                             CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Loan_Status)

#displaying the results
if result==1:
    st.success("A potential Customer")
elif result==0:
      st.success("Not a potential Customer")

if __name__ =='__main__':
    main()