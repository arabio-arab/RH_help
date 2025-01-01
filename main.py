import streamlit as st
import google.generativeai as genai
from PIL import Image  # Correct import for PIL
import PyPDF2  # Import for handling PDF files

# Set your Google API key
google_api_key ="key_APi_??????????????????????????????????"
genai.configure(api_key=google_api_key)

# Title
st.title("📝 RH Helper - Enter your question about this certification:")
st.write("Examples: (full name, date, ex...)")

# Upload the file
sample_file_2 = st.file_uploader("Upload an image or PDF", type=["jpg", "png", "jpeg", "pdf"])

# Text area for user input
user_input = st.text_area("What do you need to know?")

# Check if a file has been uploaded and user input is provided
if sample_file_2 is not None and user_input: 
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
     # Use None with capital N
    if sample_file_2.type in ["image/jpeg", "image/png"]:  # Image file types
        # Open and display the uploaded image file
        uploaded_image_2 = Image.open(sample_file_2)
        st.image(uploaded_image_2, caption="Uploaded Image", use_column_width=True)

        # Example of calling a generative model for image content.
        prompt = f"Give me information in English about: {user_input}."
       
        # Generating response
        response = model.generate_content([uploaded_image_2, prompt]) # Adjusted function call

        st.write("### Answer")
        st.markdown(response.text)  # Properly display response using markdown

    elif sample_file_2.type == "application/pdf":  # PDF file type
        # Read and display the PDF content
        pdf_reader = PyPDF2.PdfReader(sample_file_2)
        pdf_text = ""
        for page in pdf_reader.pages:
            pdf_text += page.extract_text() + "\n"  # Extract text from each page

        # Display the extracted PDF text
        st.text_area("Extracted PDF Content", pdf_text, height=300)

        # Create a prompt for PDF content
        prompt = f"Give me information in English about this PDF: {user_input}."
        # response = genai.generate_text(prompt)
        # Generating response based on PDF content
        response = model.generate_content([sample_file_2, prompt])  # Adjusted function call
          # Adjusted function call

        st.write("### Answer")
        st.markdown(response.text) 
