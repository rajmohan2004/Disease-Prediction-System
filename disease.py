import pandas as pd
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu



#loading the models
diabetes = pickle.load(open("F:\\multiple_disease_prediction-master\\notebook_files\\diabetes_model.sav", "rb"))

heart_disease = pickle.load(open("F:\\multiple_disease_prediction-master\\notebook_files\\heart_disease_model.sav", "rb"))

lung_cancer = pickle.load(open("F:\\multiple_disease_prediction-master\\notebook_files\\lung_cancer_model.sav", "rb"))




# sidebar for navigation
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

with st.sidebar:
    selected = option_menu("Disease Prediction System using Machine Learning",
                           

                           ["Diabetes Prediction",
                            "Heart Disese Prediction",
                            "Lung Cancer Prediction"],
                           menu_icon='hospital',

                           icons=["activity", "heart-fill", "lungs-fill"],

                           default_index=0)

if (selected == "Diabetes Prediction"):

    # page title
    st.title("Diabetes Prediction ")

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Glucose Level")

    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")

    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")

    with col2:
        Insulin = st.text_input("Insulin Level")

    with col3:
        BMI = st.text_input("BMI Value")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")

    with col2:
        Age = st.text_input("Age of the Person")

    # code for Prediction
    diabetes_diagnosis = " "

    # creating a button for Prediction
    if st.button("Diabetes Test Result"):
        # Ensure inputs are converted to numeric types
        try:
            Pregnancies = float(Pregnancies)
            Glucose = float(Glucose)  # Glucose is used here instead of 'a'
            BloodPressure = float(BloodPressure)
            SkinThickness = float(SkinThickness)
            Insulin = float(Insulin)
            BMI = float(BMI)
            DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
            Age = int(Age)  # Age is directly referenced
        except ValueError:
            st.error("Please provide valid numeric inputs.")
            st.stop()
        
        recommendations = {
            'reason': '',
            'reduce': '',
            'protect': '',
            'treatment': ''
        }
        
        # Perform diabetes prediction (assuming model 'diabetes' exists)
        diabetes_prediction = diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diabetes_prediction[0] == 0):
            diabetes_diagnosis = "You have no Diabetes."
            if Glucose > 140:
                recommendations['reason'] += "High glucose levels indicate potential insulin resistance. "
                recommendations['reduce'] += "You should aim to reduce sugar and carb intake. Exercise regularly. "
                recommendations['protect'] += "Monitor blood sugar levels regularly and follow a low-glycemic diet. "
                recommendations['treatment'] += "Consult a doctor for possible insulin therapy or medications like Metformin. "
        
        # BMI-based recommendation (fix: using 'BMI' instead of 'b')
            if BMI > 30:
                recommendations['reason'] += "Your BMI suggests obesity, which is a major risk factor for diabetes. "
                recommendations['reduce'] += "Try to lose weight through diet control and physical activity. "
                recommendations['protect'] += "Aim to maintain a balanced diet rich in fiber and low in refined carbohydrates. "
                recommendations['treatment'] += "Seek advice on weight management and medication if necessary. "
        
        # Age-based recommendation (using 'Age' directly)
            if Age > 45:
                recommendations['reason'] += "Your age puts you at a higher risk of developing diabetes. "
                recommendations['reduce'] += "Stay physically active, manage your diet, and monitor glucose levels. "
                recommendations['protect'] += "Regular health check-ups can help detect early signs of complications. "
                recommendations['treatment'] += "Your doctor may recommend medications to control blood sugar if necessary. "
        
        else:
            diabetes_diagnosis = "You have Diabetes."
            if Glucose > 140:
               recommendations['reason'] += "High glucose levels indicate potential insulin resistance. "
               recommendations['reduce'] += "You should aim to reduce sugar and carb intake. Exercise regularly. "
               recommendations['protect'] += "Monitor blood sugar levels regularly and follow a low-glycemic diet. "
               recommendations['treatment'] += "Consult a doctor for possible insulin therapy or medications like Metformin. "
        
             # BMI-based recommendation (fix: using 'BMI' instead of 'b')
            if BMI > 30:
               recommendations['reason'] += "Your BMI suggests obesity, which is a major risk factor for diabetes. "
               recommendations['reduce'] += "Try to lose weight through diet control and physical activity. "
               recommendations['protect'] += "Aim to maintain a balanced diet rich in fiber and low in refined carbohydrates. "
               recommendations['treatment'] += "Seek advice on weight management and medication if necessary. "
        
        # Age-based recommendation (using 'Age' directly)
            if Age > 45:
              recommendations['reason'] += "Your age puts you at a higher risk of developing diabetes. "
              recommendations['reduce'] += "Stay physically active, manage your diet, and monitor glucose levels. "
              recommendations['protect'] += "Regular health check-ups can help detect early signs of complications. "
              recommendations['treatment'] += "Your doctor may recommend medications to control blood sugar if necessary. "
    # Display result
        st.success(diabetes_diagnosis)
        
        
        # Default recommendations
        if recommendations['reason'] == '':
            recommendations['reason'] = "Diabetes is typically caused by a combination of genetics, lifestyle, and metabolic factors."
        if recommendations['reduce'] == '':
            recommendations['reduce'] = "Manage your blood sugar by following a healthy diet and staying physically active."
        if recommendations['protect'] == '':
            recommendations['protect'] = "Maintain regular checkups, monitor your blood glucose levels, and adopt a healthy lifestyle."
        if recommendations['treatment'] == '':
            recommendations['treatment'] = "Consult with a healthcare professional for a personalized treatment plan, which may include medication or lifestyle changes."

        # Display recommendations
        st.subheader("Personalized Recommendations for Diabetes")
        st.write("**Reason for Diagnosis:** ", recommendations['reason'])
        st.write("**How to Reduce the Risk/Impact:** ", recommendations['reduce'])
        st.write("**How to Protect from the Disease:** ", recommendations['protect'])
        st.write("**Treatment Recommendations:** ", recommendations['treatment'])

# Heart Disease Prediction Page:

if (selected == "Heart Disese Prediction"):

    # page title
    st.title("Heart Disease Prediction ")

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age")

    with col2:
        sex = st.number_input("Sex")

    with col3:
        cp = st.number_input("Chest Pain Types")

    with col1:
        trestbps = st.number_input("Resting Blood Pressure")

    with col2:
        chol = st.number_input("Serum Cholestoral in mg/dl")

    with col3:
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl")

    with col1:
        restecg = st.number_input("Resting Electrocardiographic Results")

    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved")

    with col3:
        exang = st.number_input("Exercise Induced Angina")

    with col1:
        oldpeak = st.number_input("ST Depression induced by Exercise")

    with col2:
        slope = st.number_input("Slope of the peak exercise ST Segment")

    with col3:
        ca = st.number_input("Major vessels colored by Flourosopy")

    with col1:
        thal = st.number_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")

    # code for Prediction
    heart_diagnosis = " "

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            age = int(age)
            sex = int(sex)
            cp = float(cp)
            trestbps = float(trestbps)
            chol = float(chol)
            fbs = float(fbs)
            restecg = float(restecg)
            thalach = float(thalach)
            exang = float(exang)
            oldpeak = float(oldpeak)
            slope = float(slope)
            ca = float(ca)
            thal = float(thal)
        except ValueError:
            st.error("Please provide valid numeric inputs.")
            st.stop()
            
         # Recommendations based on user inputs
        recommendations = {
            'reason': '',
            'reduce': '',
            'protect': '',
            'treatment': ''
        }

        # Perform Diabetes Prediction
        heart_prediction = heart_disease.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 0:
            heart_diagnosis = "You do not have heart disease."
            if chol > 200:
               recommendations['reason'] += "Your cholesterol level is high, which is a major risk factor for heart disease. "
               recommendations['reduce'] += "You should aim to reduce cholesterol by avoiding fatty and processed foods. "
               recommendations['protect'] += "Maintain a healthy diet low in saturated fats and increase physical activity. "
               recommendations['treatment'] += "Consider cholesterol-lowering medications like statins if prescribed. "

            # Blood pressure-based recommendation
            if trestbps > 130:
               recommendations['reason'] += "Your blood pressure is elevated, increasing your risk for heart disease. "
               recommendations['reduce'] += "You should reduce salt intake, manage stress, and exercise regularly. "
               recommendations['protect'] += "Monitor blood pressure regularly and follow a heart-healthy diet. "
               recommendations['treatment'] += "Your doctor may prescribe antihypertensive medications if necessary. "

            # Age-based recommendation
            if age > 50:
               recommendations['reason'] += "Your age puts you at a higher risk for heart disease. "
               recommendations['reduce'] += "Stay physically active, eat a balanced diet, and monitor your health regularly. "
               recommendations['protect'] += "Regular checkups can help detect early signs of heart disease. "
               recommendations['treatment'] += "You may need medications or lifestyle changes to prevent heart issues. "

        else:
            heart_diagnosis = "You have heart disease."
            # Cholesterol-based recommendation
            if chol > 200:
               recommendations['reason'] += "Your cholesterol level is high, which is a major risk factor for heart disease. "
               recommendations['reduce'] += "You should aim to reduce cholesterol by avoiding fatty and processed foods. "
               recommendations['protect'] += "Maintain a healthy diet low in saturated fats and increase physical activity. "
               recommendations['treatment'] += "Consider cholesterol-lowering medications like statins if prescribed. "

            # Blood pressure-based recommendation
            if trestbps > 130:
               recommendations['reason'] += "Your blood pressure is elevated, increasing your risk for heart disease. "
               recommendations['reduce'] += "You should reduce salt intake, manage stress, and exercise regularly. "
               recommendations['protect'] += "Monitor blood pressure regularly and follow a heart-healthy diet. "
               recommendations['treatment'] += "Your doctor may prescribe antihypertensive medications if necessary. "

            # Age-based recommendation
            if age > 50:
               recommendations['reason'] += "Your age puts you at a higher risk for heart disease. "
               recommendations['reduce'] += "Stay physically active, eat a balanced diet, and monitor your health regularly. "
               recommendations['protect'] += "Regular checkups can help detect early signs of heart disease. "
               recommendations['treatment'] += "You may need medications or lifestyle changes to prevent heart issues. "

            
        # Display result
        st.success(heart_diagnosis)
        
        # Display recommendations
        st.subheader("Personalized Recommendations for Heart Disease")
        st.write("**Reason for Diagnosis:** ", recommendations['reason'])
        st.write("**How to Reduce the Risk/Impact:** ", recommendations['reduce'])
        st.write("**How to Protect from the Disease:** ", recommendations['protect'])
        st.write("**Treatment Recommendations:** ", recommendations['treatment'])



# Lung Cancer Prediction Page:

if (selected == "Lung Cancer Prediction"):

    # page title
    st.title("Lung Cancer Prediction")

    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        GENDER = st.number_input("GENDER")

    with col2:
        AGE = st.number_input("AGE")

    with col3:
        SMOKING = st.number_input("SMOKING")

    with col4:
        YELLOW_FINGERS = st.number_input("YELLOW_FINGERS")

    with col1:
        ANXIETY = st.number_input("ANXIETY")

    with col2:
        PEER_PRESSURE = st.number_input("PEER_PRESSURE")

    with col3:
        CHRONIC_DISEASE = st.number_input("CHRONIC DISEASE")

    with col4:
        FATIGUE = st.number_input("FATIGUE")

    with col1:
        ALLERGY = st.number_input("ALLERGY")

    with col2:
        WHEEZING = st.number_input("WHEEZING")

    with col3:
        ALCOHOL_CONSUMING = st.number_input("ALCOHOL CONSUMING")

    with col4:
        COUGHING = st.number_input("COUGHING")

    with col1:
        SHORTNESS_OF_BREATH = st.number_input("SHORTNESS OF BREATH")

    with col2:
        SWALLOWING_DIFFICULTY = st.number_input("SWALLOWING DIFFICULTY")
    
    with col3:
        CHEST_PAIN = st.number_input("CHEST PAIN")
    

    # code for Prediction
    lung_cancer_result = " "


    # Code for Prediction
    lung_cancer_diagnosis = " "

    # Creating a button for Prediction
    if st.button('Lung Cancer Test Result'):
        try:
           GENDER = int(GENDER)
           AGE = int(AGE)
           SMOKING = int(SMOKING)
           YELLOW_FINGERS = int(YELLOW_FINGERS)
           ANXIETY = int(ANXIETY)
           PEER_PRESSURE = int(PEER_PRESSURE)
           CHRONIC_DISEASE = int(CHRONIC_DISEASE)
           FATIGUE = int(FATIGUE)
           ALLERGY = int(ALLERGY)
           WHEEZING = int(WHEEZING)
           ALCOHOL_CONSUMING = int(ALCOHOL_CONSUMING)
           COUGHING = int(COUGHING)
           SHORTNESS_OF_BREATH = int(SHORTNESS_OF_BREATH)
           SWALLOWING_DIFFICULTY = int(SWALLOWING_DIFFICULTY)
           CHEST_PAIN=int(CHEST_PAIN)
        except ValueError:
           st.error("Please enter valid numeric values.")
           st.stop()  # Stop execution if input is invalid
        
        except Exception as e:
           st.error(f"An error occurred: {e}")
            
        # Recommendations based on user inputs
        recommendations = {
            'reason': '',
            'reduce': '',
            'protect': '',
            'treatment': ''
        }

        lung_cancer_prediction = lung_cancer.predict([[SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, 
                                                        CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, 
                                                        COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])

        if lung_cancer_prediction[0] == 0:
            lung_cancer_diagnosis = "You do not have lung cancer."
            # Smoking-based recommendation
            if SMOKING == 1:
               recommendations['reason'] += "Smoking is a major cause of lung cancer. "
               recommendations['reduce'] += "Stop smoking immediately. Seek help through cessation programs or nicotine replacement therapy. "
               recommendations['protect'] += "Avoid exposure to secondhand smoke and toxic chemicals. "
               recommendations['treatment'] += "Consider lung screening and discuss treatment options like surgery, radiation, or chemotherapy. "

            # Age-based recommendation
            if AGE > 50:
               recommendations['reason'] += "Your age increases the risk of lung cancer. "
               recommendations['reduce'] += "Get regular check-ups and screenings for early detection. "
               recommendations['protect'] += "Maintain a healthy lifestyle with a focus on lung health. "
               recommendations['treatment'] += "Consult with your doctor about early detection tests like low-dose CT scans. "

            # Coughing and Shortness of Breath recommendations
            if COUGHING == 1 or SHORTNESS_OF_BREATH == 1:
                recommendations['reason'] += "Persistent coughing and shortness of breath can indicate lung problems. "
                recommendations['reduce'] += "Monitor symptoms and seek medical advice if they "

        else:
            lung_cancer_diagnosis = "You have lung cancer."
           # Smoking-based recommendation
            if SMOKING == 1:
                recommendations['reason'] += "Smoking is a major cause of lung cancer. "
                recommendations['reduce'] += "Stop smoking immediately. Seek help through cessation programs or nicotine replacement therapy. "
                recommendations['protect'] += "Avoid exposure to secondhand smoke and toxic chemicals. "
                recommendations['treatment'] += "Consider lung screening and discuss treatment options like surgery, radiation, or chemotherapy. "

            # Age-based recommendation
            if AGE > 50:
               recommendations['reason'] += "Your age increases the risk of lung cancer. "
               recommendations['reduce'] += "Get regular check-ups and screenings for early detection. "
               recommendations['protect'] += "Maintain a healthy lifestyle with a focus on lung health. "
               recommendations['treatment'] += "Consult with your doctor about early detection tests like low-dose CT scans. "

            # Coughing and Shortness of Breath recommendations
            if COUGHING == 1 or SHORTNESS_OF_BREATH == 1:
                recommendations['reason'] += "Persistent coughing and shortness of breath can indicate lung problems. "
                recommendations['reduce'] += "Monitor symptoms and seek medical advice if they "
    
        # Display result
        st.success(lung_cancer_diagnosis)
    
    
    
    
        st.subheader("Personalized Recommendations for Lung Cancer")
        st.write("**Reason for Diagnosis:** ", recommendations['reason'])
        st.write("**How to Reduce the Risk/Impact:** ", recommendations['reduce'])
        st.write("**How to Protect from the Disease:** ", recommendations['protect'])
        st.write("**Treatment Recommendations:** ", recommendations['treatment'])
