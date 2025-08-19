import streamlit as st

background_image = "url(https://cdn.pixabay.com/photo/2014/11/12/19/25/diabetes-528678_640.jpg)"  # Replace with your image URL

# Add the background image and font color to the page using CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: {background_image};
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        color: black;  
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: black;   
    }}
    </style>
    """, unsafe_allow_html=True
)


st.title("Pima-indians-diabetes")

# Collecting input data
pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1, value=0)
glucose = st.number_input('Glucose Level', min_value=0, max_value=200, step=1, value=100)
blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=200, step=1, value=80)
skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, step=1, value=20)
insulin = st.number_input('Insulin Level', min_value=0.0, max_value=1000.0, step=0.1, value=50.0)
bmi = st.number_input('BMI', min_value=0.0, max_value=100.0, step=0.1, value=25.0)
diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, step=0.01, value=0.5)
age = st.number_input('Age', min_value=0, max_value=120, step=1, value=25)

if st.button('Predict'):
    # Store input data in session state
    st.session_state["input_data"] = {
        "pregnancies": pregnancies,
        "glucose": glucose,
        "blood_pressure": blood_pressure,
        "skin_thickness": skin_thickness,
        "insulin": insulin,
        "bmi": bmi,
        "diabetes_pedigree": diabetes_pedigree,
        "age": age,
    }

    # Redirect to result page
    st.page_link("pages/Result_Page.py", label="Go to Results", icon="📊")
