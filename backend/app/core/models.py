from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base

# Creates the base class
Base = declarative_base()

# Acitvity class
class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True, auto_increment=True)
    source = Column(String, nullable=False)
    activity_type = Column(String, nullable=False)
    duration = Column(Float, nullable=False)


# Sleep Session class
class SleepSession(Base):
    __tablename__ = 'sleep_sessions'

    id = Column(Integer, primary_key=True, auto_increment=True)
    source = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    sleep_duration = Column(DateTime, nullable=False)


# HRV Readings class
class HrvReadings(Base):
    __tablename__ = 'hrv_readings'

    id = Column(Integer, primary_key=True, auto_increment=True)
    source = Column(String, nullable=False)
    time_stamps = Column(DateTime, nullable=False)
    beat_intervals = Column(DateTime, nullable=False)


# Nutrition Log class
class NutritionLog(Base):
    __tablename__ = 'nutrition_logs'

    id = Column(Integer, primary_key=True, auto_increment=True)
    source = Column(String, nullable=False)
    food_item = Column(String, nullable=False)
    protein_in_grams = Column(Integer, nullable=False)
    carbs_in_grams = Column(Integer, nullable=False)
    fat_in_grams = Column(Integer, nullable=False)
    calories = Column(Integer, nullable=False)


# Body Composition
class BodyMetric(Base):
    __tablename__ = 'body_metrics'

    id = Column(Integer, primary_key=True, auto_increment=True)
    source = Column(String, nullable=False)
    bodyweight_in_kg = Column(Integer, nullable=False)
    height_in_cm = Column(Integer, nullable=False)
    resting_hr = Column(Integer, nullable=False)
    vo2max = Column(Integer, nullable=False)

# generate database file
if __name__ == "__main__":
    from pathlib import Path

    # create file in current directory
    BASE_DIR = Path(__file__).resolve().parent
    db_path = BASE_DIR / "parameters.db"

    engine = create_engine(f"sqlite:///{db_path}")

    Base.metadata.create_all(bind=engine)

    print(f"Schema successfully defined and {db_path} generated")