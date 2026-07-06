import pandas as pd
from applications.models import Student,Drive,Application,Companies
from applications.database import db

def load_data():
    students = pd.read_sql_table("student", db.engine)
    drives = pd.read_sql_table("drive", db.engine)
    applications = pd.read_sql_table("application", db.engine)
    companies = pd.read_sql_table("companies", db.engine)
    return students,drives,applications,companies
