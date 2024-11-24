from googletrans import Translator

# Initialize Google Translator
translator = Translator()

def translate_text(text, target_language):
    """Translates text into the specified language."""
    if not target_language:  # If "None" is selected
        return text
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"⚠ Translation Error: {str(e)}"
