import streamlit as st
from utils import get_leetcode_stats, get_kaggle_stats, format_results_nicely

st.set_page_config(page_title="ML Profile Evaluator for LeetCode and Kaggle", layout="centered")

st.title("🚀 ML Profile Dashboard")
st.markdown("Enter your LeetCode and Kaggle usernames to view your journey!")

col1, col2 = st.columns(2)
with col1:
    leetcode_id = st.text_input("🧠 LeetCode Username")
with col2:
    kaggle_id = st.text_input("📊 Kaggle Username")

if st.button("📥 Fetch My Profile"):
    if leetcode_id and kaggle_id:
        with st.spinner("Fetching your journey..."):
            lc_data = get_leetcode_stats(leetcode_id)
            kg_data = get_kaggle_stats(kaggle_id)

            if lc_data["status"] == "error":
                st.error("⚠️ Unable to fetch LeetCode data.")
            if kg_data["status"] == "error":
                st.error("⚠️ Unable to fetch Kaggle data.")

            if lc_data["status"] == "success" and kg_data["status"] == "success":
                result = format_results_nicely(lc_data, kg_data)
                st.success("✅ Data Retrieved Successfully!")
                st.markdown(result)
    else:
        st.warning("Please fill in both usernames.")
