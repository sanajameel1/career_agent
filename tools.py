def get_career_roadmap(field):
    roadmap = {
        "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Git"],
        "Data Scientist": ["Python", "Pandas", "ML Algorithms", "Jupyter"],
        # Add more
    }
    return roadmap.get(field, ["No roadmap found. Try another field."])

def get_job_roles(field):
    jobs = {
        "Web Developer": ["Frontend Developer", "Backend Developer", "Fullstack Engineer"],
        "Data Scientist": ["ML Engineer", "AI Analyst", "Data Analyst"]
    }
    return jobs.get(field, ["No job roles found. Try another field."])