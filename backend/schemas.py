from pydantic import BaseModel
from typing import Optional, List

class SchemeOut(BaseModel):
    id: int
    name: str
    description: str
    category: str
    level: str
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    max_income: Optional[float] = None
    occupation: Optional[str] = None
    gender: Optional[str] = None
    caste_category: Optional[str] = None
    state_applicability: str
    benefits: str
    official_link: Optional[str] = None

    class Config:
        from_attributes = True
class CitizenIn(BaseModel):
    age: int
    income: float
    occupation: str
    gender: str
    caste_category: str
class MatchResult(BaseModel):
    scheme_id: int
    name: str
    category: str
    level: str
    benefits: str
    official_link: Optional[str] = None
    reasons: List[str]