from database import SessionLocal
from models import Scheme

db = SessionLocal()

count = db.query(Scheme).count()
print(f"Total schemes in database: {count}")

first_three = db.query(Scheme).limit(3).all()
for scheme in first_three:
    print(f"- {scheme.name} | Category: {scheme.category} | Level: {scheme.level}")

db.close()