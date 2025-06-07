import requests
from bs4 import BeautifulSoup

def get_leetcode_stats(username):
    try:
        url = f"https://leetcode-stats-api.herokuapp.com/{username}"
        res = requests.get(url)
        data = res.json()
        if "status" in data and data["status"] == "error":
            return {"status": "error"}

        return {
            "status": "success",
            "total_problems": data.get("totalSolved", 0),
            "easy": data.get("easySolved", 0),
            "medium": data.get("mediumSolved", 0),
            "hard": data.get("hardSolved", 0),
            "ranking": data.get("ranking", "N/A"),
            "recent_submission": "Check profile for latest"
        }
    except Exception as e:
        return {"status": "error"}

def get_kaggle_stats(username):
    try:
        url = f"https://www.kaggle.com/{username}"
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")

        rank = soup.find("span", class_="sc-dcJsrY").text.strip() if soup.find("span", class_="sc-dcJsrY") else "N/A"
        competitions = soup.find_all("div", class_="sc-iGgWBj jzIApq")  # May vary
        datasets_count = html.count("/datasets")  # Approximate

        return {
            "status": "success",
            "rank": rank,
            "datasets": datasets_count,
            "recent_competition": competitions[0].text.strip() if competitions else "N/A"
        }
    except Exception as e:
        return {"status": "error"}

def format_results_nicely(lc_data, kg_data):
    return f"""
### 👨‍💻 LeetCode Summary
- Total Problems Solved: {lc_data["total_problems"]}
- Easy: {lc_data["easy"]}, Medium: {lc_data["medium"]}, Hard: {lc_data["hard"]}
- Global Ranking: {lc_data["ranking"]}
- Recent Submission: {lc_data["recent_submission"]}

### 📊 Kaggle Summary
- Rank: {kg_data["rank"]}
- Datasets Published: {kg_data["datasets"]}
- Recent Competition: {kg_data["recent_competition"]}
"""
