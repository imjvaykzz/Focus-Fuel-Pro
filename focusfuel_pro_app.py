
# FOCUSFUEL PRO APP by jvaykzz
# Streamlit-based productivity web app with full features and advanced additions

import streamlit as st
import time
import datetime
import random
import plotly.graph_objects as go

# ------------------ CONFIGURATION ------------------
st.set_page_config(page_title="FocusFuel Pro", layout="wide")

# ------------------ SESSION SETUP ------------------
if "study_sessions" not in st.session_state:
    st.session_state.study_sessions = []
if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = []
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

# ------------------ SIDEBAR ------------------
st.sidebar.title("⚙️ Menu")
menu = st.sidebar.radio("Go to", ["🏠 Home", "📅 Study Planner", "✅ To-Do List", "🎧 Motivation", "🎵 Study Music", "📈 Progress Graphs", "ℹ️ About"])
st.sidebar.divider()
st.sidebar.write("Toggle Theme")
st.session_state.dark_mode = st.sidebar.checkbox("Dark Mode", value=True)

if st.session_state.dark_mode:
    st.markdown("""
        <style>
        body {background-color: #111; color: white;}
        </style>
    """, unsafe_allow_html=True)

# ------------------ HOME ------------------
if menu == "🏠 Home":
    st.title("🚀 FocusFuel Pro")
    st.subheader("Fuel Your Focus. Crush Your Goals.")
    st.markdown("> *\"Stay hard.\" – David Goggins*")
    st.markdown("""
        ---
        Welcome to **FocusFuel Pro**, the productivity app designed to help you grind smart, stay motivated, and reach elite focus levels.
        ---
        Made by **jvaykzz**  
        📧 Contact: [jvaykzz@gmail.com](mailto:jvaykzz@gmail.com)
    """)

# ------------------ STUDY PLANNER ------------------
elif menu == "📅 Study Planner":
    st.title("📅 Study Planner")
    subject = st.text_input("Enter Subject/Goal")
    hours = st.selectbox("Select Study Hours", list(range(0, 18)))
    minutes = st.selectbox("Select Study Minutes", [0, 15, 30, 45])
    break_min = st.selectbox("Break After (mins)", list(range(1, 16)))
    music_type = st.selectbox("Select Study Music", ["Lo-fi Chill", "Ambient Focus", "Instrumental Piano", "Anime Vibes"])

    if st.button("Start Focus Session"):
        total_minutes = hours * 60 + minutes
        st.success(f"Studying {subject} for {total_minutes} mins with {music_type} music 🎵")
        st.info(f"Break in {break_min} mins! 💡")
        st.session_state.study_sessions.append({"subject": subject, "minutes": total_minutes, "timestamp": str(datetime.date.today())})

# ------------------ TO-DO LIST ------------------
elif menu == "✅ To-Do List":
    st.title("✅ To-Do List")
    task = st.text_input("Add New Task")
    if st.button("Add Task"):
        st.session_state.completed_tasks.append({"task": task, "done": False})
    for i, t in enumerate(st.session_state.completed_tasks):
        col1, col2 = st.columns([0.9, 0.1])
        if not t["done"]:
            if col1.checkbox(t["task"], key=f"task_{i}"):
                st.session_state.completed_tasks[i]["done"] = True
                col2.success("✅")

# ------------------ MOTIVATIONAL VIDEOS ------------------
elif menu == "🎧 Motivation":
    st.title("🎧 Motivation Time")
    videos = [
        "https://www.youtube.com/embed/78I9dTB9vqM",
        "https://www.youtube.com/embed/IdTMDpizis8",
        "https://www.youtube.com/embed/Bh1yMnrbyA8"
    ]
    selected = random.choice(videos)
    st.video(selected)
    st.caption("Randomly chosen motivational video from Goggins/Eric Thomas/Jocko")

# ------------------ STUDY MUSIC ------------------
elif menu == "🎵 Study Music":
    st.title("🎵 Choose Your Focus Music")
    col1, col2 = st.columns(2)
    with col1:
        st.video("https://www.youtube.com/embed/5qap5aO4i9A")
        st.caption("Lo-fi Chill")
    with col2:
        st.video("https://www.youtube.com/embed/MYtHZgSt8Us")
        st.caption("Ambient Focus")
    col3, col4 = st.columns(2)
    with col3:
        st.video("https://www.youtube.com/embed/4D9b9K18Q6Q")
        st.caption("Instrumental Piano")
    with col4:
        st.video("https://www.youtube.com/embed/jfKfPfyJRdk")
        st.caption("Anime Vibes")

# ------------------ PROGRESS GRAPH ------------------
elif menu == "📈 Progress Graphs":
    st.title("📈 Your Productivity")
    if st.session_state.study_sessions:
        data = {}
        for session in st.session_state.study_sessions:
            date = session["timestamp"]
            mins = session["minutes"]
            data[date] = data.get(date, 0) + mins

        fig = go.Figure([go.Bar(x=list(data.keys()), y=list(data.values()), name='Study Time (min)')])
        fig.update_layout(title="📊 Study Time Per Day", xaxis_title="Date", yaxis_title="Minutes")
        st.plotly_chart(fig)
        st.markdown("---")
        st.markdown("**App built by jvaykzz**")
        st.markdown("📧 Contact: [jvaykzz@gmail.com](mailto:jvaykzz@gmail.com)")
    else:
        st.warning("No study data yet. Start a session to track progress!")

# ------------------ ABOUT PAGE ------------------
elif menu == "ℹ️ About":
    st.title("ℹ️ About This App")
    st.markdown("""
        **FocusFuel Pro** is a productivity web app built by *jvaykzz* — a student, creator, and dreamer aiming for the Ivy League.

        This app was made to help me and others like me stay laser-focused, fight distractions, and build real discipline. It includes:
        - Study planner with long sessions
        - Focus music & videos
        - Motivation breaks
        - Graphs to track your grind

        If you're an admission officer, this app is a symbol of passion, resilience, and self-made determination.

        — jvaykzz  
        📧 Contact: [jvaykzz@gmail.com](mailto:jvaykzz@gmail.com)
    """)
