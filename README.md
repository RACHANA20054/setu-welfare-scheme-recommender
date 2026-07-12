# SETU — AI-Driven Welfare Scheme Discovery & Eligibility Recommendation System

SETU helps citizens of Karnataka, India discover government welfare schemes they're eligible for — instantly, with clear, transparent explanations of *why* they qualify.

🔗 **Live Demo:** [setu-welfare-scheme-recommender.vercel.app](https://setu-welfare-scheme-recommender.vercel.app)
🔗 **Backend API Docs:** [setu-welfare-scheme-recommender.onrender.com/docs](https://setu-welfare-scheme-recommender.onrender.com/docs)

> **Note:** The backend is hosted on Render's free tier, which spins down after inactivity. The first request after idling may take 30–60 seconds to respond.

---

## The Problem

In India, thousands of government welfare schemes exist across central, state, and local levels — but citizens frequently miss out because:
- Information is scattered across dozens of separate portals
- Eligibility criteria are complex, inconsistent, and hard to interpret
- People simply don't know which schemes they qualify for

## The Solution

SETU stores a structured database of 28 real welfare schemes (central government + Karnataka state schemes) with their eligibility rules, takes a citizen's basic details (age, income, occupation, gender, category), and returns a personalized, explained list of every scheme they qualify for.

---

## How the "AI" Works

SETU uses a **rule-based eligibility engine**, not a machine learning model or LLM, for the core matching decision — and this was a deliberate design choice:

- **Correctness over probability:** Eligibility for a government scheme is a factual, deterministic question — not something that should be answered "probably." A rule engine gives a citizen an accurate, auditable answer every time.
- **Full explainability:** Every match includes the exact reasons a citizen qualifies (e.g., *"Age 25 meets minimum age 18"*), rather than an opaque black-box score.
- **No training data required:** Unlike an ML classifier, this approach doesn't need historical application data (which realistically isn't available for a project like this) to work correctly from day one.

This mirrors how real government and fintech eligibility systems are typically built: **deterministic rule engines for decisions, with AI/LLMs reserved for communication layers** (e.g., turning raw results into friendly natural language) — a pattern I deliberately followed here.

---

## Tech Stack

**Backend**
- Python + FastAPI — REST API framework with automatic interactive docs
- SQLAlchemy (ORM) + SQLite — structured data storage for schemes and eligibility rules
- Pydantic — request/response validation

**Frontend**
- React + Vite — component-based UI, fast dev tooling
- React Router — multi-page navigation without full reloads
- Plain CSS with a custom civic-themed design system (CSS variables)

**Deployment**
- Backend: Render (free tier)
- Frontend: Vercel (free tier)

---

## Architecture
React Frontend (Vercel)
│  HTTP POST /match (citizen details as JSON)
▼
FastAPI Backend (Render)
│
├── SQLAlchemy ORM ──► SQLite Database (28 schemes + eligibility rules)
│
└── Rule-Based Matching Engine
│  Checks age, income, occupation, gender, caste category,
│  and state applicability per scheme — only where each
│  scheme actually defines that rule (nullable fields)
▼
Returns matched schemes + human-readable reasons (JSON)
---

## Features

- 28 real, researched welfare schemes (central government + Karnataka state)
- Citizen eligibility form with validated dropdowns (occupation, gender, category)
- Instant matching with per-scheme, per-rule explanations
- Handles edge cases: zero matches, backend unavailability, direct page access without data
- Clean, civic-themed responsive UI

---

## Running Locally

### Backend
```bash
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1        # Windows
pip install -r requirements.txt
python seed.py                      # only needed once, to populate the database
uvicorn main:app --reload
```
Backend runs at `http://127.0.0.1:8000` — interactive docs at `/docs`.

### Frontend
```bash
cd frontend
npm install
npm run dev
```
Frontend runs at `http://localhost:5173`.

---

## Known Limitations (Honest Scope Notes)

- Currently supports Karnataka residents only — expanding to other states would require additional scheme data, not additional code changes.
- Disability status is not currently modeled as a citizen input, so disability-specific schemes may match on age/income alone. A production version would add this field.
- The 28-scheme dataset is a curated, realistic sample — not an exhaustive list of every scheme available in Karnataka.

---

## Future Improvements

- Add an LLM-generated natural-language summary layer on top of the rule engine's structured output
- Expand to additional Indian states
- Add user accounts to save/track scheme applications
- Add a disability-status field and related scheme rules

---

## Author

Built by Rachana as a portfolio project to demonstrate full-stack development and thoughtful AI-system design for a real-world social impact use case.