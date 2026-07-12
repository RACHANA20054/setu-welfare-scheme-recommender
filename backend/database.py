from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# This tells SQLAlchemy where our database file lives.
# "sqlite:///./setu.db" means: use SQLite, and store the file
# named setu.db in the current folder.
DATABASE_URL = "sqlite:///./setu.db"

# The "engine" is SQLAlchemy's connection manager to our database file.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# A "session" is like a temporary workspace we use to talk to the database
# (read data, add data, save changes) during a single operation.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# "Base" is a special class that all our table models will inherit from.
# It lets SQLAlchemy know which Python classes represent database tables.
Base = declarative_base()