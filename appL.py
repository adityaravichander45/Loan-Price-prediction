{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "17499ebb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a7caddf",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = joblib.load('preprocess_model.pkl')\n",
    "\n",
    "st.title(\"Loan status Prediction\")\n",
    "name = st.selectbox(\n",
    "    'Select the Brand of the Car?',\n",
    "    ('maruti','honda','toyota'))\n",
    "fuel = st.selectbox(\n",
    "    'Select the Fuel Type of the Car?',\n",
    "    ('petrol','diesel'))\n",
    "km = st.number_input('Select the Km_Driven by the vehicle')\n",
    "\n",
    "def predict_price(model, name, fuel, km):\n",
    "    new_test = [name,fuel,km]\n",
    "    new_ = pd.DataFrame(new_test).T\n",
    "    new_.columns = ['name','fuel_type', 'km_driven']\n",
    "    return model.predict(new_)[0]    \n",
    "\n",
    "if st.button('Predict'):\n",
    "    result_petrol  = predict_price(model, name, 'petrol', km)\n",
    "    result_diesel  = predict_price(model, name, 'diesel', km)\n",
    "    st.write(\"Predicted \", name ,\" Car Price with fuel comparison: \")\n",
    "    st.write(\"Predicted  \", name ,\" Car Price with Petrol : \",result_petrol)\n",
    "    st.write(\"Predicted  \", name ,\" Car Price with Diesel : \",result_diesel)"
   ]
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
