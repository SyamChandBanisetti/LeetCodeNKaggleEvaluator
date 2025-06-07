import streamlit as st
from utils import get_leetcode_stats, get_kaggle_stats, format_results_nicely
import pandas as pd

st.set_page_config(page_title="🚀 ML Profile Evaluator", layout="centered")

st.title("🚀 ML Profile Dashboard")
st.markdown("Compare your journey in **LeetCode** and **Kaggle** using a clean, visual dashboard.")

# Input Fields
col1, col2 = st.columns(2)
with col1:
    leetcode_id = st.text_input("🧠 LeetCode Username", placeholder="Enter LeetCode username")
with col2:
    kaggle_id = st.text_input("📊 Kaggle Username", placeholder="Enter Kaggle username")

# Button Action
if st.button("📥 Fetch My Profile"):
    if leetcode_id and kaggle_id:
        with st.spinner("Fetching your journey..."):
            lc_data = get_leetcode_stats(leetcode_id)
            kg_data = get_kaggle_stats(kaggle_id)

            # Error Handling
            if lc_data["status"] == "error":
                st.error("⚠️ Unable to fetch LeetCode data.")
            if kg_data["status"] == "error":
                st.error("⚠️ Unable to fetch Kaggle data.")

            # Success Block
            if lc_data["status"] == "success" and kg_data["status"] == "success":
                st.success("✅ Data Retrieved Successfully!")

                # Display Text Summary
                result = format_results_nicely(lc_data, kg_data)
                st.markdown(result)

                # Comparison Table
                st.subheader("📊 Quick Comparison")
                table_data = {
                    "Platform": ["LeetCode", "Kaggle"],
                    "Total Problems / Datasets": [lc_data["total_problems"], kg_data["datasets"]],
                    "Rating / Tiers": [lc_data["ranking"], kg_data["rank"]],
                    "Recent Activity": [lc_data["recent_submission"], kg_data["recent_competition"]]
                }
                df = pd.DataFrame(table_data)
                st.table(df)

                # Chart
                st.subheader("🧠 LeetCode Problem Distribution")
                st.bar_chart({
                    "Easy": [lc_data["easy"]],
                    "Medium": [lc_data["medium"]],
                    "Hard": [lc_data["hard"]]
                })

                # Downloadable Report
                st.subheader("📄 Download My Report")
                report_content = result + "\n\n---\nComparison:\n" + df.to_string(index=False)
                st.download_button("📥 Download as TXT", report_content, file_name="ml_profile_summary.txt")
    else:
        st.warning("🚨 Please enter both usernames.")
