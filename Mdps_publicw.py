# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:02:07 2025

@author: prate
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models correctly
with open('diabetes_model.sav', 'rb') as file:
    diabetes_model = pickle.load(file)

with open('heart_disease_model.sav', 'rb') as file:
    heart_disease_model = pickle.load(file)

with open('parkinsons_model.sav', 'rb') as file:
    parkinsons_model = pickle.load(file)

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Multiple Disease Prediction System",  # Corrected menu title
        options=['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],  # Fixed text consistency
        icons=['activity', 'heart', 'person'],  # Corrected syntax issue with the comma
        default_index=0
    )

# Diabetes prediction page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
         pregnancies =st.text_input('Number of Pregnancies')
    
    with col2:
         Glucose =st.text_input('Glucose level')
    
    with col3:
         BloodPressure =st.text_input('Blood Pressure value')
         
    with col1:
        SkinThickness =st.text_input(' Skin Thickness value')
        
    with col2:
        Insulin =st.text_input('Insulin Level') 
    
    with col3:    
        BMI =st.text_input('BMI value') 
 
    with  col1:
       DiabetespedigreeFunction =st.text_input(' Diabetes pedigree Function value')
    
    with col2:
       Age = st.text_input('Age of the person')
        
    
    #code for prediction
    diab_dignosis = ''
    
    #creating button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetespedigreeFunction, Age]])
    
        if(diab_prediction[0] == 1):
            diab_dignosis = 'The person is Diabetic'
        else:
            diab_dignosis = 'The person is not Diabetic'
            
    st.success(diab_dignosis)        
    
    

# Heart disease prediction page
if selected == 'Heart Disease Prediction':  
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
         age =st.text_input('Age')
    
    with col2:
         sex =st.text_input('Sex')
    
    with col3:
        cp =st.text_input('Chest Pain types')
         
    with col1:
        testbps =st.text_input('Resting Blood Pressure')
        
    with col2:
        chol =st.text_input('Serum cholestrol in mg/dl') 
    
    with col3:    
        fbs =st.text_input('Fasting Blood Sugar > 20 mg/dl') 
 
    with  col1:
       restecg =st.text_input('Resting Electrocardiographic results')
    
    with col2:
       thalach = st.text_input('Maximum Heart Rate Achieved')
       
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with  col1:
        oldpeak =st.text_input('ST depression induced by exercise')
      
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
         
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')   
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
    
    #code for prediction
    heart_dignosis = ''
    
    #creating button for prediction
    
    if st.button('Heart disease Test Result'):
        heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), float(testbps), float(chol), 
                                                    int(fbs), int(restecg), float(thalach), int(exang), 
                                                    float(oldpeak), int(slope), int(ca), int(thal)]])

        
    
        if(heart_prediction[0] == 1):
            heart_dignosis = 'The person is having heart disease'
        else:
            heart_dignosis = 'The person is does not have any heart disease'
            
    st.success(heart_dignosis)        
    
    


# Parkinson’s prediction page
if selected == 'Parkinsons Prediction':  
    st.title('Parkinson’s Prediction using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
    
    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
    
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter: DDP')
       
    with col4:
        Shimmer = st.text_input('MDVP: Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
    
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQS = st.text_input('Shimmer : APQS')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer: DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
    
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
         spread2 = st.text_input('spread2')
         
    with col1:
         D2 = st.text_input('D2')
         
    with col2:
         PPE = st.text_input('PPE')
         
         
    parkinson_diagnosis = ''
     
    if st.button("Parkinson's Test Result"):
      parkinsons_prediction = parkinsons_model.predict([[float(fo), float(fhi), float(flo), float(Jitter_percent), 
                                                              float(Jitter_Abs), float(RAP), float(PPQ), float(DDP), 
                                                              float(Shimmer), float(Shimmer_dB), float(APQ3), 
                                                              float(APQS), float(APQ), float(DDA), float(NHR), 
                                                              float(HNR), float(RPDE), float(DFA), float(spread1), 
                                                              float(spread2), float(D2), float(PPE)]])

      if(parkinsons_prediction[0]==1):
             parkinson_diagnosis = "The person has Parkinson's disease"
      else:
             parkinson_diagnosis = "The person does not have Parkinson's disease"
             
    st.success(parkinson_diagnosis)        
    
   
        
        
        
    
       
