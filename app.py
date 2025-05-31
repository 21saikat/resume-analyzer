import streamlit as st
from analyze_resume import analyze_resume

st.title("AI Resume Analyzer ✨")
st.markdown("Paste your resume below and get expert AI feedback!")

resume_text = st.text_area("📄 Your Resume:", height=300)

if st.button("🔍 Analyze"):
    if resume_text.strip():
        feedback = analyze_resume(resume_text)
        st.success("✅ Analysis Complete!")
        st.write(feedback)
    else:
        st.warning("⚠️ Please paste your resume first.")
