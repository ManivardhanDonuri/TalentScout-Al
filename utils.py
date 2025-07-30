import re
from config import EMAIL_PATTERN, PHONE_PATTERN, MIN_EXPERIENCE, MAX_EXPERIENCE

def validate_email(email):
    """Check if the email follows a proper format (something@domain.com)"""
    return re.match(EMAIL_PATTERN, email) is not None

def validate_phone(phone):
    """Clean up phone number and check if it's valid (removes spaces, dashes, parentheses)"""
    cleaned_phone = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
    return re.match(PHONE_PATTERN, cleaned_phone) is not None

def validate_experience(experience_str):
    """Validate years of experience input"""
    try:
        experience = float(experience_str.strip())
        return MIN_EXPERIENCE <= experience <= MAX_EXPERIENCE
    except ValueError:
        return False

def parse_tech_stack(tech_stack_input):
    """Parse and clean tech stack input from comma-separated string"""
    if not tech_stack_input:
        return []
    
    tech_list = [tech.strip() for tech in tech_stack_input.split(',') if tech.strip()]
    return tech_list

def format_candidate_info(candidate_info):
    """Format candidate information for display"""
    formatted_info = {}
    for key, value in candidate_info.items():
        if key == 'tech_stack':
            formatted_info[key] = ', '.join(value) if isinstance(value, list) else value
        else:
            formatted_info[key] = value
    return formatted_info

def calculate_progress(current_question, total_questions):
    """Calculate interview progress percentage"""
    if total_questions == 0:
        return 0.0
    return min(current_question / total_questions, 1.0)

def get_current_tech_and_question(question_index, tech_list, questions_per_tech=5):
    """Get current technology and question based on question index"""
    tech_index = question_index // questions_per_tech
    question_in_tech = question_index % questions_per_tech
    
    if tech_index < len(tech_list):
        current_tech = tech_list[tech_index]
        return current_tech, question_in_tech
    return None, None

def is_interview_complete(question_index, tech_list, questions_per_tech=5):
    """Check if the technical interview is complete"""
    total_questions = len(tech_list) * questions_per_tech
    return question_index >= total_questions 