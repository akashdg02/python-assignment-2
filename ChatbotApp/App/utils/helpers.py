# utils/helpers.py
from datetime import datetime

def format_timestamp():
    """Returns the current time in HH:MM AM/PM format for chat bubbles."""
    return datetime.now().strftime("%I:%M %p")

def truncate_text(text, max_length=50):
    """Truncates long strings for the chat history sidebar."""
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

def clean_input(user_text):
    """Basic sanitization of user input."""
    if not user_text:
        return ""
    return user_text.strip()