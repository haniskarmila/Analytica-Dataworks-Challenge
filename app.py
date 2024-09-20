import streamlit as st
import pickle
import pandas as pd
import numpy as np

pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(PERMX,PERMY,PERMZ,PORO,Transmissibility):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: PERMX
        in: query
        type: number
        required: true
      - name: PERMY
        in: query
        type: number
        required: true
      - name: PERMZ
        in: query
        type: number
        required: true
      - name: PORO
        in: query
        type: number
        required: true
      - name: Transmissibility
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[PERMX,PERMY,PERMZ,PORO,Transmissibility]])
    print(prediction)
    return prediction



def main():
    st.title("OIL GAS WATER PRODUCTION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit RESERVOIR SIMULATIONS MODEL App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    PERMX = st.text_input("PERMX","Type Here")
    PERMY = st.text_input("PERMY","Type Here")
    PERMZ = st.text_input("PERMZ","Type Here")
    PORO = st.text_input("PORO","Type Here")
    Transmissibility = st.text_input("Transmissibility","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(PERMX,PERMY,PERMZ,PORO,Transmissibility)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
