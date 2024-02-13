
import streamlit as st

def predict(input_data):
    # Your machine learning model prediction logic here
    prediction = "Your prediction result"
    return prediction

def highlight_text(text, color='blue', font_weight='bold', font_size='16px', background_color='transparent', padding='5px'):
    return f'<span style="color:{color}; font-weight:{font_weight}; font-size:{font_size}; background-color:{background_color}; padding:{padding}">{text}</span>'

def main():
   
    st.sidebar.title("Sidebar")

    app_mode = st.sidebar.radio("Navigation",
        ["Prediction", "Settings"])

    if app_mode == "Prediction":
        prediction_page()
    elif app_mode == "Settings":
        settings_page()
page_bg_img = '''
<style>
.stApp{
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
.stTextArea {
        background-color: #f0f0f0;
        color: #333333;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #cccccc;
    }
.stButton {
 
        color: #333333;
        padding: 10px;
        text

    }
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
def prediction_page():
    st.title("Prediction Page")

    input_data = st.text_input("Input Data", "Input data here...")

    if st.button("Predict"):
        prediction = predict(input_data)
        styled_prediction = highlight_text(prediction, color='green', font_weight='bold', font_size='20px', background_color='#f0f0f0', padding='10px')
        st.markdown(f"Prediction Result: {styled_prediction}", unsafe_allow_html=True)

def settings_page():
    st.title("Settings Page")
    st.write("This is the settings page.")

if __name__ == "__main__":
    main()
