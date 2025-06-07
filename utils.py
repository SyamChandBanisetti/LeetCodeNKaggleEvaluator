def get_leetcode_stats(username):
    # Replace with real scraping or API later
    return {
        "status": "success",
        "total_problems": 380,
        "easy": 150,
        "medium": 180,
        "hard": 50,
        "ranking": "Top 8%",
        "recent_submission": "2025-06-05"
    }

def get_kaggle_stats(username):
    # Replace with real scraping or Kaggle API later
    return {
        "status": "success",
        "datasets": 12,
        "rank": "Expert Tier",
        "recent_competition": "Titanic - 2025"
    }

def format_results_nicely(lc_data, kg_data):
    return f"""
### 📘 LeetCode Summary
- Total Problems Solved: **{lc_data['total_problems']}**
  - Easy: {lc_data['easy']} | Medium: {lc_data['medium']} | Hard: {lc_data['hard']}
- Global Ranking: **{lc_data['ranking']}**
- Last Submission: {lc_data['recent_submission']}

### 📙 Kaggle Summary
- Datasets Shared: **{kg_data['datasets']}**
- Rank: **{kg_data['rank']}**
- Last Competition: {kg_data['recent_competition']}
"""
