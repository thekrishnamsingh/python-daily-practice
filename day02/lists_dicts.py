# lists_dicts.py
# Examples of lists and dictionaries

# List example
skills = ["Python", "Django", "FastAPI"]
skills.append("PostgreSQL")

for skill in skills:
    print("Skill:", skill)

# Dictionary example
developer = {
    "name": "Krishnam Singh",
    "role": "Python Developer",
    "experience": "Backend"
}

for key, value in developer.items():
    print(f"{key}: {value}")
