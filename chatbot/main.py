import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data if not already present
nltk.download('punkt')

# Define the chat pairs for the chatbot
pairs = [
    ["hello|hi|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you", ["I'm doing well, thank you!", "I'm good. How about you?"]],
    ["what is your name", ["I am a chatbot.", "You can call me ChatGPT."]],
    ["quit", ["Bye!", "Goodbye!", "Nice talking to you. See you later!"]],
    # Add more chat pairs as needed
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    return chatbot.respond(user_input)

# Streamlit UI
def main():
    st.title("Text-based Chatbot")
    st.markdown("This chatbot can respond to various user inputs. Try saying hello!")

    user_input = st.text_input("You:", "")

    if st.button("Send"):
        st.text("Chatbot: " + chatbot_response(user_input))

if __name__ == "__main__":
    main()
