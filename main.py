import streamlit as st
from app.config import GEMINI_API_KEY
from app.models import load_object_detection_model, configure_generative_ai, generate_scene_description, detect_objects, draw_boxes
from app.text_to_speech import generate_audio_file
from app.translator import translate_text
from app.utils import extract_text_from_image
from PIL import Image
from app.models import generate_task_assistance


# Configure Generative AI
configure_generative_ai(GEMINI_API_KEY)

# Load Object Detection Model
object_detection_model = load_object_detection_model()

# Streamlit App Config
st.set_page_config(page_title="AI Vision Care Assist", page_icon="👁")

# CSS for styling
st.markdown(
    """
    <style>
    .sub-title {
        font-size: 18px;
        color: #555;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Custom CSS styling for the title and sidebar
st.markdown(
    """
    <style>
    .custom-title {
        font-size: 48px;
        text-align: center;
        font-weight: bold;
        font-family: Open Sans;
        background: -webkit-linear-gradient(rgb(188, 12, 241), rgb(212, 4, 4));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-left: 95px;
    }
    .custom-icon {
        font-size: 42px; /* Adjust this size as needed */
        
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main title and subtitle
st.markdown(
    """
    <div>
        <span class="custom-title">AI Vision Care Assist</span> 
        <span class="custom-icon">👁</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="sub-title">AI for Scene Understanding, Text Extraction & Speech for the Visually Impaired 🗣</div>', unsafe_allow_html=True)

# Sidebar instructions
st.sidebar.text_area(
    "📜 Instructions", 
    """Upload an image to start. Choose a feature to interact with:
    1. Describe the Scene
    2. Extract Text from an image
    3. Detect Objects
    4. Personalized Assistance""", 
    height=155
)

# Sidebar description
st.sidebar.markdown(
    """
    💡 *How it helps*:
    Assists visually impaired users by providing scene descriptions, text extraction, object detection, and personalized assistance.

    📌 *Features*
    - 🔍 *Describe Scene*: Get AI insights about the image in text and convert the generated text into speech.
    - 📝 *Extract Text*: Extract visible text using OCR and convert the generated text into speech.
    - 🚧 *Detect Objects*: Detect objects/obstacles for safe navigation.
    - 🤖 *Personalized Assistance*: Provide guidance for specific tasks using Generative AI.
    """
)

# Language selection for translation
st.sidebar.markdown("### Select Translation Language")
language_mapping = {
    "None": None,
    "Telugu": "te",
    "Hindi": "hi",
    "Kannada": "kn",
    "Malayalam": "ml"
}
selected_language = st.sidebar.selectbox("Choose a language", list(language_mapping.keys()), index=0)

# Feature selection
st.markdown("<h3>Select a Feature</h3>", unsafe_allow_html=True)
feature_choice = st.radio(
    "Choose a feature to interact with:",
    options=["🔍 Describe Scene", "📝 Extract Text", "🚧 Object Detection", "🤖 Personalized Assistance"]
)

# Image Upload Section
st.markdown("<h3 class='feature-header'>📤 Upload an Image</h3>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Drag and drop or browse an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if feature_choice == "🔍 Describe Scene":
        if uploaded_file:
            with st.spinner("Generating scene description..."):
                image_data = [{"mime_type": uploaded_file.type, "data": uploaded_file.getvalue()}]
                scene_prompt = """
                You are an AI assistant helping visually impaired individuals by describing the scene in the image. Provide:
                1. Overall description of the image.
                """
                scene_response = generate_scene_description(scene_prompt, image_data)

                st.markdown("### Scene Description (Original):")
                st.write(scene_response)

                # Generate and play audio for the scene description
                st.markdown("### Audio Description (English):")
                scene_audio = generate_audio_file(scene_response)
                st.audio(scene_audio, format="audio/mp3")

                target_language_code = language_mapping[selected_language]
                translated_scene = translate_text(scene_response, target_language_code)

                if selected_language != "None":
                    st.markdown(f"### Translated Description ({selected_language}):")
                    st.write(translated_scene)

    elif feature_choice == "📝 Extract Text":
        if uploaded_file:
            with st.spinner("Extracting text from the image..."):
                extracted_text = extract_text_from_image(image)

                st.markdown("### Extracted Text (Original):")
                st.text_area("Extracted Text", extracted_text, height=150)

                st.markdown("### Audio Text (English):")
                text_audio = generate_audio_file(extracted_text)
                st.audio(text_audio, format="audio/mp3")

                target_language_code = language_mapping[selected_language]
                translated_text = translate_text(extracted_text, target_language_code)

                if selected_language != "None":
                    st.markdown(f"### Translated Text ({selected_language}):")
                    st.write(translated_text)

    elif feature_choice == "🚧 Object Detection":
        predictions = detect_objects(image, object_detection_model)
        image_with_boxes = draw_boxes(image.copy(), predictions)
        st.image(image_with_boxes, caption="Objects Detected", use_column_width=True)

    elif feature_choice == "🤖 Personalized Assistance":
        if uploaded_file:
            with st.spinner("Providing assistance..."):
                image_data = [{"mime_type": uploaded_file.type, "data": uploaded_file.getvalue()}]
                assistance_prompt = """
                You are a helpful AI assistant. Analyze the uploaded image and identify tasks you can assist with,
                such as recognizing objects or reading labels for a visually impaired user.
                """
                assistance_response = generate_task_assistance(assistance_prompt, image_data)

                st.markdown("### Personalized Assistance (Original):")
                st.write(assistance_response)

                st.markdown("### Audio Assistance (English):")
                english_audio = generate_audio_file(assistance_response)
                st.audio(english_audio, format="audio/mp3")

                target_language_code = language_mapping[selected_language]
                translated_response = translate_text(assistance_response, target_language_code)

                if selected_language != "None":
                    st.markdown(f"### Translated Assistance ({selected_language}):")
                    st.write(translated_response)

else:
    st.info("👆 Please select a feature and upload an image to proceed.")

# Footer
st.markdown(
    """
    <hr>
    <footer style="text-align:center;">
        <p><strong>© Pavankumar</strong> | Built with ❤ using Streamlit</p>
    </footer>
    """,
    unsafe_allow_html=True,
)
