import requests
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_leetcode_stats(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "easy": data.get("easySolved", 0),
            "medium": data.get("mediumSolved", 0),
            "hard": data.get("hardSolved", 0)
        }
    return {"easy": 0, "medium": 0, "hard": 0}

def get_kaggle_stats(username):
    url = f"https://www.kaggle.com/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        return {"competitions": 0, "predictions": 0}

    competitions = response.text.count('competition-submission')
    predictions = response.text.count('submission')

    return {"competitions": competitions, "predictions": predictions}

def evaluate_user_profile(lc_data, kg_data):
    prompt = (
        f"Evaluate this user's machine learning and data science profile:\n\n"
        f"LeetCode:\n"
        f"- Easy problems solved: {lc_data['easy']}\n"
        f"- Medium problems solved: {lc_data['medium']}\n"
        f"- Hard problems solved: {lc_data['hard']}\n\n"
        f"Kaggle:\n"
        f"- Competitions participated: {kg_data['competitions']}\n"
        f"- Predictions made: {kg_data['predictions']}\n\n"
        f"Provide a 3-4 sentence assessment and rate the user (out of 5) based on practical ML exposure."
    )

    model = genai.GenerativeModel("models/gemini-2.0-flash")  # Adjust if model name changes
    response = model.generate_content(prompt)
    return response.text
