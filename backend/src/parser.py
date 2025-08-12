from .schema import ParsedResume
from .utils.utils import extract_email, extract_phone
from .ner_model import extract_entities

def parse_resume_text(text: str) -> ParsedResume:
    parsed = ParsedResume(raw_text=text)
    parsed.email = extract_email(text)
    parsed.phone = extract_phone(text)

    ents = extract_entities(text)
    if "PERSON" in ents:
        parsed.name = ents["PERSON"][0]

    skills_keywords = ["python", "java", "c++", "javascript", "react", "node", "aws", "docker", "sql"]
    parsed.skills = sorted(set([kw for kw in skills_keywords if kw in text.lower()]))

    return parsed
