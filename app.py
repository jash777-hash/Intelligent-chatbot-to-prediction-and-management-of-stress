import streamlit as st
from textblob import TextBlob

# 🎯 App Title
st.set_page_config(page_title="🧠 Stress Management Chatbot", page_icon="🧠")
st.title("🧠 Stress Prediction & Management Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 📝 User Input
user_input = st.text_input("Type your message here...")

# 📊 Analyze and Respond
if st.button("Send") and user_input.strip() != "":
    # Sentiment analysis
    blob = TextBlob(user_input)
    sentiment_score = blob.sentiment.polarity

    # Determine stress level and suggestions
    if sentiment_score < -0.2:
        stress_level = "😟 High Stress"
        suggestion = (
            "Take a deep breath, go for a short walk, and try to talk with someone you trust. "
            "Meditation or listening to calm music may help."
        )
    elif -0.2 <= sentiment_score <= 0.2:
        stress_level = "😐 Moderate Stress"
        suggestion = (
            "You seem okay, but it’s good to take breaks. "
            "Drink some water, stretch, or spend a few minutes doing something you enjoy."
        )
    else:
        stress_level = "😊 Low Stress"
        suggestion = (
            "You’re doing great! Keep maintaining your positive mood. "
            "Continue your daily habits that help you stay calm and focused."
        )

    # Append user and bot messages
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(
        ("Bot", f"**Stress Level:** {stress_level}\n**Suggestion:** {suggestion}")
    )

# 🗨️ Display conversation
st.subheader("Chat History:")
for sender, message in st.session_state.messages:
    st.markdown(f"**{sender}:** {message}")

# 🩵 Footer
st.markdown("---")
st.caption("Developed by [Your Name] — MCA Mini Project | Stress Prediction & Management")
