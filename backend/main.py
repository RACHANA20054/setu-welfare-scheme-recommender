from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
from models import Scheme
from schemas import SchemeOut
from schemas import SchemeOut, CitizenIn, MatchResult
from matching_engine import check_eligibility


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://setu-welfare-scheme-recommender.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This function creates a new database session for each request,
# and makes sure it's properly closed afterward - even if an error happens.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to SETU - AI-driven Welfare Scheme Recommender"}

@app.get("/schemes", response_model=List[SchemeOut])
def get_all_schemes(db: Session = Depends(get_db)):
    schemes = db.query(Scheme).all()
    return schemes

@app.get("/schemes/{scheme_id}", response_model=SchemeOut)
def get_scheme_by_id(scheme_id: int, db: Session = Depends(get_db)):
    scheme = db.query(Scheme).filter(Scheme.id == scheme_id).first()
    if scheme is None:
        raise HTTPException(status_code=404, detail="Scheme not found")
    return scheme
@app.post("/match", response_model=List[MatchResult])
def match_schemes(citizen: CitizenIn, db: Session = Depends(get_db)):
    all_schemes = db.query(Scheme).all()
    matches = []

    for scheme in all_schemes:
        eligible, reasons = check_eligibility(citizen, scheme)
        if eligible:
            matches.append(MatchResult(
                scheme_id=scheme.id,
                name=scheme.name,
                category=scheme.category,
                level=scheme.level,
                benefits=scheme.benefits,
                official_link=scheme.official_link,
                reasons=reasons
            ))

    return matches