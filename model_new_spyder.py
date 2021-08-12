# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:49:23 2021

@author: DELL
"""

#import pandas as pd
#import numpy as np
import pickle
import streamlit as st
#from PIL import Image
  
# loading in the model to predict on the data
 #pickle_in = open('randomforest.pkl', 'rb')
#randomforestclassifier = pickle.load(pickle_in)
model=pickle.load(open('randomforest.pkl', 'rb'))
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(number, incident_state, opened_by, opened_at, sys_updated_by,
       sys_updated_at, subcategory, resolved_by, resolved_at, closed_at):  
   
    prediction = model.predict(
        [[number, incident_state, opened_by, opened_at, sys_updated_by,
       sys_updated_at, subcategory,resolved_by, resolved_at, closed_at]])
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Incident Predictions")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:violet;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Randomforest Classifier ML App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    number = st.text_input("number", "Type Here")
    incident_state = st.text_input(" incident_state ", "Type Here")
    opened_by = st.text_input("opened_by", "Type Here")
    opened_at= st.text_input(" opened_at", "Type Here")
    sys_updated_by= st.text_input("sys_updated_by", "Type Here")
    sys_updated_at= st.text_input("sys_updated_at", "Type Here")
    subcategory= st.text_input("subcategory", "Type Here")
    resolved_at= st.text_input("resolved_at", "Type Here")
    resolved_by= st.text_input("resolved_by", "Type Here")
    closed_at= st.text_input("closed_at", "Type Here")
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(number, incident_state, opened_by, opened_at, sys_updated_by,
        sys_updated_at, subcategory, resolved_by, resolved_at, closed_at)
    st.success('The output is {}'.format(result))
               
if __name__=='__main__':
    main()
