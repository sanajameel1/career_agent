from tools import get_career_roadmap, get_job_roles

def career_agent(user_interest):
    if "web" in user_interest.lower():
        return "Web Developer"
    elif "data" in user_interest.lower():
        return "Data Scientist"
    else:
        return "Teacher"

def skill_agent(field):
    return get_career_roadmap(field)

def job_agent(field):
    return get_job_roles(field)