# ai_brain.py

import openai
import os

# Set the API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are RoboSage, a calm and wise AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Sorry, I had trouble thinking: {e}"
