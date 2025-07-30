import streamlit as st
from ui_components import (
    setup_page, initialize_session_state, render_chat_interface,
    render_chat_input, render_bot_response, render_initial_greeting,
    render_reset_button
)
from conversation_handler import handle_user_input

def main():
    """Main application function"""
    # Set up the page
    setup_page()
    
    # Initialize session state
    initialize_session_state()
    
    # Render the main chat interface
    render_chat_interface()
    
    # Render the initial greeting
    render_initial_greeting()
    
    # Handle user input
    user_input = render_chat_input()
    
    if user_input:
        # Process the user input and get the bot's response
        bot_response = handle_user_input(user_input)
        
        # Render the bot's response
        render_bot_response(bot_response)
    
    # Render the reset button
    render_reset_button()

if __name__ == "__main__":
    main() 