from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class Education:
    degree: Optional[str] = None
    institution: Optional[str] = None
    start_year: Optional[str] = None
    end_year: Optional[str] = None

@dataclass
class Experience:
    title: Optional[str] = None
    company: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None

@dataclass
class ParsedResume:
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    summary: Optional[str] = None
    location: Optional[str] = None
    skills: List[str] = field(default_factory=list)
    education: List[Education] = field(default_factory=list)
    education: List[Experience] = field(default_factory=list)
    raw_text: Optional[str] = None
    extras: Dict = field(default_factory=dict)