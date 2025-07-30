import streamlit as st
from config import GREETING_MESSAGE, STAGES

def setup_page():
    """Set up the page configuration"""
    from config import PAGE_CONFIG
    st.set_page_config(**PAGE_CONFIG)
    
    # Hide deploy button and other deploy-related elements
    hide_deploy_ui = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    .stApp > header {display: none;}
    .stApp > footer {display: none;}
    .stDeployButton {visibility: hidden;}
    [data-testid="stDeployButton"] {display: none;}
    </style>
    """
    st.markdown(hide_deploy_ui, unsafe_allow_html=True)

def initialize_session_state():
    """Initialize all session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'candidate_info' not in st.session_state:
        st.session_state.candidate_info = {}
    if 'conversation_stage' not in st.session_state:
        st.session_state.conversation_stage = STAGES['greeting']
    if 'current_tech_stack' not in st.session_state:
        st.session_state.current_tech_stack = []
    if 'generated_questions' not in st.session_state:
        st.session_state.generated_questions = []
    if 'current_question_index' not in st.session_state:
        st.session_state.current_question_index = 0

def render_chat_interface():
    """Render the main chat interface"""
    st.title("TalentScout AI Hiring Assistant")
    
    # Display all previous messages in the conversation
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

def render_chat_input():
    """Render the chat input and handle user input"""
    if prompt := st.chat_input("Type your message here..."):
        # Add the user's message to our conversation history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Show the user's message in the chat
        with st.chat_message("user"):
            st.write(prompt)
        
        return prompt
    return None

def render_bot_response(response):
    """Render the bot's response"""
    # Add the bot's response to conversation history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Show the bot's response in the chat
    with st.chat_message("assistant"):
        st.write(response)

def render_initial_greeting():
    """Render the initial greeting if this is the first time loading the app"""
    if not st.session_state.messages and st.session_state.conversation_stage == STAGES['greeting']:
        st.session_state.messages.append({"role": "assistant", "content": GREETING_MESSAGE})
        with st.chat_message("assistant"):
            st.write(GREETING_MESSAGE)

def render_reset_button():
    """Render the reset button at the bottom"""
    st.markdown("---")
    if st.button("🔄 Reset Conversation", type="secondary"):
        # Clear all stored information and start fresh
        st.session_state.messages = []
        st.session_state.candidate_info = {}
        st.session_state.conversation_stage = STAGES['greeting']
        st.session_state.current_tech_stack = []
        st.session_state.generated_questions = []
        st.session_state.current_question_index = 0
        st.rerun() 