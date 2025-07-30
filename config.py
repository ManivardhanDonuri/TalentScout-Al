# Configuration settings for TalentScout AI Hiring Assistant

# Page configuration
PAGE_CONFIG = {
    "page_title": "TalentScout AI Hiring Assistant",
    "page_icon": "🤖"
}

# Validation patterns
EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PHONE_PATTERN = r'^[\+]?[1-9][\d]{0,15}$'

# Experience validation
MIN_EXPERIENCE = 0
MAX_EXPERIENCE = 50

# Questions per technology
QUESTIONS_PER_TECH = 5

# Conversation stages
STAGES = {
    'greeting': 'greeting',
    'collecting_info': 'collecting_info',
    'generating_questions': 'generating_questions',
    'technical_interview': 'technical_interview',
    'completion': 'completion'
}

# Information fields to collect
INFO_FIELDS = ['email', 'phone', 'experience', 'position', 'location', 'tech_stack']

# Default messages
GREETING_MESSAGE = """Hello! I'm the TalentScout AI Hiring Assistant. I'm here to help us get to know you better and assess your technical skills.

This conversation will take about 10-15 minutes and includes:
• Basic information collection
• Technical skill assessment
• Custom interview questions based on your tech stack

Let's start by getting some basic information about you. What's your full name?"""

# Error messages
ERROR_MESSAGES = {
    'invalid_email': "Please provide a valid email address (e.g., john.doe@example.com).",
    'invalid_phone': "Please provide a valid phone number.",
    'invalid_experience': "Please provide a realistic number of years of experience (0-50).",
    'invalid_experience_format': "Please provide a number for years of experience.",
    'empty_tech_stack': "Please provide at least one technology in your tech stack.",
    'unknown_response': "I'm not sure how to respond to that. Could you please rephrase?"
}

# Success messages
SUCCESS_MESSAGES = {
    'name_collected': "Nice to meet you, {name}! Now, could you please provide your email address?",
    'email_collected': "Great! Now, what's your phone number?",
    'phone_collected': "Perfect! How many years of experience do you have in software development?",
    'experience_collected': "Excellent! What position(s) are you interested in?",
    'position_collected': "Great! What's your current location (city, country)?",
    'location_collected': "Perfect! Now, please list your tech stack (e.g., Python, Django, React, etc.). You can separate technologies with commas.",
    'tech_stack_collected': "Excellent! I'm generating custom technical questions based on your tech stack. This will take a moment...",
    'questions_generated': "Perfect! Let's start with {tech}. Here's your first question:\n\n{question}",
    'next_question': "Great answer! Here's your next question about {tech}:\n\n{question}",
    'next_tech': "Excellent! Now let's move to {tech}. Here's your first question:\n\n{question}",
    'interview_complete': "Thank you for your response! That concludes our technical interview. You've done great!\n\nSummary of your profile:\n• Name: {name}\n• Experience: {experience} years\n• Tech Stack: {tech_stack}\n• Location: {location}\n\nOur team will review your responses and get back to you within 2-3 business days. Thank you for your time and interest in joining our team!",
    'completion': "The interview is complete! Thank you for your time. Our team will review your responses and contact you soon."
} 