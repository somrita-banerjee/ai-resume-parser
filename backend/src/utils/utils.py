import re
from typing import Optional

EMAIL_RE = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
PHONE_RE = re.compile(r"(\+?d[\d\-s]{7,}d)")

def extract_email(text: str) -> Optional[str]:
    m = EMAIL_RE.search(text)
    return m.group(1).strip() if m else None

def extract_phone(text: str) -> Optional[str]:
    m = PHONE_RE.search(text)
    if not m:
        return None
    phone = re.sub(r"[^\d+]","", m.group(1))
    return phone

def find_section(text: str, header_keywords:list):
    lowered = text.lower()
    for kw in header_keywords:
        idx = lowered.find(kw.lower())
        if idx != -1:
            return text[idx:]
    return None