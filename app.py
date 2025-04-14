import streamlit as st
from utils import get_leetcode_stats, get_kaggle_stats, evaluate_user_profile

st.title("🔍 ML Profile Evaluator: LeetCode + Kaggle")

leetcode_id = st.text_input("🧠 Enter your LeetCode ID")
kaggle_id = st.text_input("📊 Enter your Kaggle ID")

if st.button("Evaluate My Profile"):
    if leetcode_id and kaggle_id:
        with st.spinner("Fetching data..."):
            lc_data = get_leetcode_stats(leetcode_id)
            kg_data = get_kaggle_stats(kaggle_id)
            result = evaluate_user_profile(lc_data, kg_data)

        st.subheader("📈 Gemini Evaluation")
        st.markdown(result)
    else:
        st.warning("Please enter both LeetCode and Kaggle IDs.")
