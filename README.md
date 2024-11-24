
```markdown
# AI Vision Care Assist

AI Vision Care Assist is an AI-powered solution designed to assist visually impaired individuals by providing scene descriptions, text extraction from images, object detection for navigation, and personalized task assistance.

The application leverages several AI models and libraries to enable the following functionalities:

- Scene understanding and description generation
- Text extraction (OCR) from images
- Object detection and obstacle recognition for safe navigation
- Personalized assistance for task-specific guidance using Generative AI

## Features

- **🔍 Describe Scene**: Generates a textual description of the scene in the uploaded image and provides an audio output.
- **📝 Extract Text**: Extracts visible text from an image using OCR (Tesseract) and converts it into audio.
- **🚧 Detect Objects**: Detects objects and obstacles in the image for navigation and safety.
- **🤖 Personalized Assistance**: Provides task-specific guidance using Generative AI, such as identifying objects or reading labels.

## Installation

### 1. Clone the repository
Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/AI-Vision-Care-Assist.git
```

### 2. Install dependencies
Navigate to the project folder and install the required dependencies using **pip**:

```bash
cd AI-Vision-Care-Assist
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can create it by running the following command after installing the necessary libraries:

```bash
pip freeze > requirements.txt
```

### 3. Set up Environment Variables
1. Create a **`.env`** file in the root of your project directory.
2. Add your **Google Generative AI API key** and the **Tesseract path** (for OCR) in the `.env` file.

Example of `.env`:

```ini
GEMINI_API_KEY=your_generative_ai_api_key_here
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe  # Update this path to where Tesseract is installed
```

### 4. Run the App
Run the Streamlit app with the following command:

```bash
streamlit run main.py
```

This will launch the app in your default web browser.

## Usage

1. **Upload an image**: Once the app is running, you can upload an image to be processed.
2. **Select a feature**: Choose between **Describe Scene**, **Extract Text**, **Detect Objects**, or **Personalized Assistance**.
3. **Interact with the output**:
    - The app will display the generated text or extracted text.
    - The text can be translated into **Telugu, Hindi, Kannada, or Malayalam** based on your selection.
    - The text is also read aloud using **text-to-speech** in English.

## Technologies Used

- **Streamlit**: For building the web app.
- **Google Generative AI (Gemini API)**: For scene understanding and generating personalized assistance.
- **Tesseract OCR**: For optical character recognition to extract text from images.
- **PyTorch & Faster R-CNN**: For object detection and recognizing obstacles in images.
- **Google Translate API**: For translating text into multiple languages (Telugu, Hindi, Kannada, Malayalam).
- **pyttsx3**: For text-to-speech conversion to read text aloud.

## File Structure

```
/project_root
    ├── main.py                # Main file to run the Streamlit app
    ├── .env                   # Environment variables (e.g., API keys, paths)
    ├── app/                   # Package folder containing logic
    │   ├── __init__.py        # This makes 'app' a package
    │   ├── config.py          # Configuration and API keys
    │   ├── models.py          # Object detection and AI models
    │   ├── text_to_speech.py  # Text-to-speech logic
    │   ├── translator.py      # Google Translate logic
    │   ├── utils.py           # Helper functions (e.g., OCR, scene description)
    ├── requirements.txt       # List of dependencies
    ├── .gitignore             # Files to exclude from version control
    └── README.md              # Project documentation
```
