import streamlit as st
from agent import career_agent, skill_agent, job_agent

st.title("💼 Career Mentor Agent")

user_input = st.text_input("What are your interests?")

if st.button("Get Career Advice") and user_input:
    with st.spinner("Thinking..."):
        field = career_agent(user_input)
        skills = skill_agent(field)
        jobs = job_agent(field)

        st.subheader("Recommended Career:")
        st.write(field)

        st.subheader("Skills You Should Learn:")
        st.write(", ".join(skills))

        st.subheader("Possible Job Roles:")
        st.write(", ".join(jobs))