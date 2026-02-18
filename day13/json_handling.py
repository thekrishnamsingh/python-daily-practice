import json

# Sample data
data = {
    "name": "Krishnam Singh",
    "role": "Python Developer",
    "skills": ["Python", "Django", "FastAPI", "Flask", "Selenium",  "MongoDB", "Git","Docker", "Kubernetes", "AWS", "Azure"],
}

# Write JSON to file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data written to data.json")

# Read JSON from file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded Data:", loaded_data)