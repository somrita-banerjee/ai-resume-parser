import spacy
import re

nlp = spacy.load("en_core_web_sm")

def parse_resume(text):
    doc = nlp(text)
    name = None
    email = None
    phone = None
    skills = []

    for ent in doc.ents:
        if ent.label_ == "PERSON" and not name:
            name = ent.text

    email_match = re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",text)
    phone_match = re.search(r"\bd{10}\b", text)
    if email_match:
        email = email_match.group()
    if phone_match:
        phone = phone_match.group()

    skill_keywords = ["Python", "Java", "C++", "Machine learning", "AWS", "React", "SQL"]
    for skill in skill_keywords:
        if skill.lower() in text.lower():
            skills.append(skill)

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills
    }