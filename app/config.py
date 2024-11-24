from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access the variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TESSERACT_PATH = os.getenv("TESSERACT_PATH")
