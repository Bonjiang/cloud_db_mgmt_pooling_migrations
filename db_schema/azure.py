from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    contact_number = Column(String(15))

    records = relationship('MedicalRecord', back_populates='patient')

class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    diagnosis = Column(String(100), nullable=False)
    treatment = Column(String(200))
    admission_date = Column(Date, nullable=False)
    discharge_date = Column(Date)

    patient = relationship('Patient', back_populates='records')


### Part 2 - initial sqlalchemy-engine to connect to db:

engine = create_engine("mysql+pymysql://user:password@server/database",
                         connect_args={'ssl': {'ssl-mode': 'preferred'}},
                         )

## Test connection

inspector = inspect(engine)
inspector.get_table_names()


### Part 3 - create the tables using sqlalchemy models, with no raw SQL required:

Base.metadata.create_all(engine)

