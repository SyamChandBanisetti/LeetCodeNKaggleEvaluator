import requests
import os
from dotenv import load_dotenv
import google.generativeai as genai

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
            "hard": data.get("hardSolved", 0),
            "status": "success"
        }
    return {"easy": 0, "medium": 0, "hard": 0, "status": "error"}

def get_kaggle_stats(username):
    url = f"https://www.kaggle.com/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        return {"competitions": 0, "predictions": 0, "status": "error"}

    competitions = response.text.count('competition-submission')
    predictions = response.text.count('submission')

    return {"competitions": competitions, "predictions": predictions, "status": "success"}

def format_results_nicely(lc_data, kg_data):
    prompt = (
        f"Display this user's data science journey in a friendly bullet point list:\n\n"
        f"LeetCode:\n"
        f"- Easy problems solved: {lc_data['easy']}\n"
        f"- Medium problems solved: {lc_data['medium']}\n"
        f"- Hard problems solved: {lc_data['hard']}\n\n"
        f"Kaggle:\n"
        f"- Competitions participated: {kg_data['competitions']}\n"
        f"- Predictions made: {kg_data['predictions']}\n\n"
        f"Present this data as a clean summary, but do not evaluate or judge."
    )

    model = genai.GenerativeModel("models/gemini-pro")
    response = model.generate_content(prompt)
    return response.text
