import streamlit as st
from config import STAGES, ERROR_MESSAGES, SUCCESS_MESSAGES, QUESTIONS_PER_TECH
from utils import validate_email, validate_phone, validate_experience, parse_tech_stack
from utils import get_current_tech_and_question, is_interview_complete

def generate_technical_questions(tech_stack):
    """Create 5 questions for each technology the candidate mentioned"""
    questions_dict = {}
    
    for tech in tech_stack:
        questions_dict[tech] = [
            f"What are the key features of {tech}?",
            f"Describe a real-world scenario where you would use {tech}.",
            f"What are the best practices when working with {tech}?",
            f"How would you troubleshoot common issues in {tech}?",
            f"What are the latest trends and updates in {tech}?"
        ]
    
    return questions_dict

def get_question_by_index(questions_dict, tech, question_index):
    """Get a specific question for a technology by index"""
    if tech in questions_dict and 0 <= question_index < len(questions_dict[tech]):
        return questions_dict[tech][question_index]
    return None

def get_total_questions(tech_stack):
    """Calculate total number of questions based on tech stack"""
    return len(tech_stack) * QUESTIONS_PER_TECH

def get_tech_list_from_questions(questions_dict):
    """Extract list of technologies from questions dictionary"""
    return list(questions_dict.keys())

def handle_greeting_stage(user_input):
    """Handle the greeting stage - collect the candidate's name"""
    st.session_state.candidate_info['full_name'] = user_input.strip()
    st.session_state.conversation_stage = STAGES['collecting_info']
    return SUCCESS_MESSAGES['name_collected'].format(name=user_input.strip())

def handle_collecting_info_stage(user_input):
    """Handle the information collection stage"""
    current_field = None
    
    # Determine which field we're currently collecting
    if 'email' not in st.session_state.candidate_info:
        current_field = 'email'
    elif 'phone' not in st.session_state.candidate_info:
        current_field = 'phone'
    elif 'experience' not in st.session_state.candidate_info:
        current_field = 'experience'
    elif 'position' not in st.session_state.candidate_info:
        current_field = 'position'
    elif 'location' not in st.session_state.candidate_info:
        current_field = 'location'
    elif 'tech_stack' not in st.session_state.candidate_info:
        current_field = 'tech_stack'
    
    return process_field_input(current_field, user_input)

def process_field_input(field, user_input):
    """Process input for a specific field with validation"""
    user_input = user_input.strip()
    
    if field == 'email':
        if validate_email(user_input):
            st.session_state.candidate_info['email'] = user_input
            return SUCCESS_MESSAGES['email_collected']
        else:
            return ERROR_MESSAGES['invalid_email']
    
    elif field == 'phone':
        if validate_phone(user_input):
            st.session_state.candidate_info['phone'] = user_input
            return SUCCESS_MESSAGES['phone_collected']
        else:
            return ERROR_MESSAGES['invalid_phone']
    
    elif field == 'experience':
        if validate_experience(user_input):
            st.session_state.candidate_info['experience'] = float(user_input)
            return SUCCESS_MESSAGES['experience_collected']
        else:
            return ERROR_MESSAGES['invalid_experience']
    
    elif field == 'position':
        st.session_state.candidate_info['position'] = user_input
        return SUCCESS_MESSAGES['position_collected']
    
    elif field == 'location':
        st.session_state.candidate_info['location'] = user_input
        return SUCCESS_MESSAGES['location_collected']
    
    elif field == 'tech_stack':
        tech_stack = parse_tech_stack(user_input)
        if tech_stack:
            st.session_state.candidate_info['tech_stack'] = tech_stack
            st.session_state.current_tech_stack = tech_stack
            st.session_state.conversation_stage = STAGES['generating_questions']
            return SUCCESS_MESSAGES['tech_stack_collected']
        else:
            return ERROR_MESSAGES['empty_tech_stack']
    
    return ERROR_MESSAGES['unknown_response']

def handle_generating_questions_stage():
    """Handle the question generation stage"""
    if not st.session_state.generated_questions:
        questions = generate_technical_questions(st.session_state.current_tech_stack)
        st.session_state.generated_questions = questions
    
    tech_list = get_tech_list_from_questions(st.session_state.generated_questions)
    if tech_list:
        current_tech = tech_list[0]
        current_questions = st.session_state.generated_questions[current_tech]
        st.session_state.current_question_index = 0
        st.session_state.conversation_stage = STAGES['technical_interview']
        
        return SUCCESS_MESSAGES['questions_generated'].format(
            tech=current_tech, 
            question=current_questions[0]
        )
    
    return "Please wait while I generate your custom questions..."

def handle_technical_interview_stage():
    """Handle the technical interview stage"""
    tech_list = get_tech_list_from_questions(st.session_state.generated_questions)
    current_tech, question_index = get_current_tech_and_question(
        st.session_state.current_question_index, 
        tech_list
    )
    
    # Move to the next question
    st.session_state.current_question_index += 1
    
    # Check if interview is complete
    if is_interview_complete(st.session_state.current_question_index, tech_list):
        st.session_state.conversation_stage = STAGES['completion']
        return format_completion_message()
    
    # Get next question
    next_tech, next_question_index = get_current_tech_and_question(
        st.session_state.current_question_index, 
        tech_list
    )
    
    if next_tech and next_question_index is not None:
        next_questions = st.session_state.generated_questions[next_tech]
        
        if next_question_index < len(next_questions):
            return SUCCESS_MESSAGES['next_question'].format(
                tech=next_tech, 
                question=next_questions[next_question_index]
            )
        else:
            # Move to next technology
            next_tech_index = st.session_state.current_question_index // 5 + 1
            if next_tech_index < len(tech_list):
                next_tech = tech_list[next_tech_index]
                next_questions = st.session_state.generated_questions[next_tech]
                st.session_state.current_question_index = next_tech_index * 5
                return SUCCESS_MESSAGES['next_tech'].format(
                    tech=next_tech, 
                    question=next_questions[0]
                )
    
    return "Thank you for your response! Moving to the next question..."

def format_completion_message():
    """Format the completion message with candidate information"""
    candidate_info = st.session_state.candidate_info
    return SUCCESS_MESSAGES['interview_complete'].format(
        name=candidate_info.get('full_name', 'N/A'),
        experience=candidate_info.get('experience', 'N/A'),
        tech_stack=', '.join(candidate_info.get('tech_stack', [])),
        location=candidate_info.get('location', 'N/A')
    )

def handle_completion_stage():
    """Handle the completion stage"""
    return SUCCESS_MESSAGES['completion']

def handle_user_input(user_input):
    """Main function to handle user input based on conversation stage"""
    
    if st.session_state.conversation_stage == STAGES['greeting']:
        return handle_greeting_stage(user_input)
    
    elif st.session_state.conversation_stage == STAGES['collecting_info']:
        return handle_collecting_info_stage(user_input)
    
    elif st.session_state.conversation_stage == STAGES['generating_questions']:
        return handle_generating_questions_stage()
    
    elif st.session_state.conversation_stage == STAGES['technical_interview']:
        return handle_technical_interview_stage()
    
    elif st.session_state.conversation_stage == STAGES['completion']:
        return handle_completion_stage()
    
    return ERROR_MESSAGES['unknown_response'] 