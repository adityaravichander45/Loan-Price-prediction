{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "17499ebb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.base import BaseEstimator, TransformerMixin"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f98579c2",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-10-05 21:01:05.470 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\radia\\anaconda3\\anaconda\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title(\"Loan Price Prediction\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "33cec7cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "class CustomTransformer(BaseEstimator, TransformerMixin):\n",
    "    def __init__(self):\n",
    "        print('\\n>>>>>>>init() called.\\n')\n",
    "    def fit(self, X, y = None):\n",
    "        print('\\n>>>>>>>fit() called.\\n')\n",
    "        return self\n",
    "    def transform(self, X, y = None):\n",
    "        print('\\n>>>>>>>transform() called.\\n')\n",
    "        print(\"\\n>>>> Input : \",X)\n",
    "        X_ = X.applymap(lambda x: x.lower())\n",
    "        print(\"\\n>>>> Output : \",X_)\n",
    "        print(\"\\n>>>>>>> Custom Transformer Called\")\n",
    "        return X_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9d1bb3d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = joblib.load('model.pkl')\n",
    "encod= joblib.load('encod.pkl')\n",
    "scale= joblib.load('scale.pkl')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "06adc09a",
   "metadata": {},
   "outputs": [],
   "source": [
    "Property_area = st.selectbox(\n",
    "   \"What is the property area for the loan?\",\n",
    "   (\"Rural\", \"Urban\", \"Semi urban\"),\n",
    "   index=None,\n",
    "   placeholder=\"Select the Property area...\",\n",
    ")\n",
    "\n",
    "st.write('You selected:', Property_area)\n",
    "\n",
    "Dependents = st.selectbox(\n",
    "   \"How many dependents are there for the loan?\",\n",
    "   (\"0\", \"1\", \"2\",'3+'),\n",
    "   index=None,\n",
    "   placeholder=\"Select the dependents...\",\n",
    ")\n",
    "\n",
    "st.write('You selected:', Dependents)\n",
    "\n",
    "Gender = st.selectbox(\n",
    "   \"What is your gender?\",\n",
    "   (\"Male\", \"Female\"),\n",
    "   index=None,\n",
    "   placeholder=\"Select your gender...\",\n",
    ")\n",
    "\n",
    "st.write('You selected:', Gender)\n",
    "\n",
    "Loan_Amount_Term = st.selectbox(\n",
    "   \"What is the term of the loan amount?\",\n",
    "   ('360','120','180','60','300','480','240','36','84'),\n",
    "   index=None,\n",
    "   placeholder=\"Select the term of the loan amount...\",\n",
    ")\n",
    "\n",
    "st.write('You selected:', Loan_Amount_Term)\n",
    "\n",
    "\n",
    "Education = st.selectbox(\n",
    "   \"Are you educated?\",\n",
    "   ('Graduate','Not Graduate'),\n",
    "   index=None,\n",
    "   placeholder=\"Select the qualification...\",\n",
    ")\n",
    "\n",
    "st.write('You selected:', Education)\n",
    "\n",
    "\n",
    "Credit_History = st.selectbox(\n",
    "   \"What is credit history?\",\n",
    "   ('0','1'),\n",
    "   index=None,\n",
    "   placeholder=\"Select the qualification...\",\n",
    ")\n",
    "\n",
    "st.write('You selected:', Credit_History)\n",
    "\n",
    "\n",
    "ApplicantIncome = number = st.number_input(\"Enter the Applicant Income\", value=None, placeholder=\"Type the amount...\")\n",
    "\n",
    "st.write('You selected:', ApplicantIncome)\n",
    "\n",
    "\n",
    "CoapplicantIncome = number = st.number_input(\"Enter the CoapplicantIncome\", value=None, placeholder=\"Type the amount...\")\n",
    "\n",
    "st.write('You selected:', CoapplicantIncome)\n",
    "\n",
    "\n",
    "LoanAmount = number = st.number_input(\"Enter the loan amount\", value=None, placeholder=\"Type the amount...\")\n",
    "\n",
    "st.write('You selected:', LoanAmount)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cf1ee353",
   "metadata": {},
   "outputs": [],
   "source": [
    "def predict_loan(model, Loan_Status,Credit_History):\n",
    "    new_test = [Loan_Status,Credit_History]\n",
    "    new_ = pd.DataFrame(new_test).T\n",
    "    new_.columns = ['Loan_Status','Credit_History']\n",
    "    return model.predict(new_)[0]    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "10a0faa4",
   "metadata": {},
   "outputs": [],
   "source": [
    "if st.button('Predict'):\n",
    "    result_status  = predict_loan(model, name, 'Loan_Status')\n",
    "    result_credit  = predict_loan(model, name, 'Credit_History')\n",
    "    st.write(\"Predicted  \", name ,\" Loan Status : \",result_status)\n",
    "    st.write(\"Predicted  \", name ,\" Credit History : \",result_credit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e26f82b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
