"""
Using ORM framework of your choice, create models classes created in Homework 6 (Teachers, Students, Homework and others).
- Target database should be sqlite (filename main.db localted in current directory)
- ORM framework should support migrations.

Utilizing that framework capabilities, create
 - a migration file, creating all necessary database structures.
 - a migration file (separate) creating at least one record in each created database table
 - (*) optional task: write standalone script (get_report.py) that retrieves and stores the following information into CSV file report.csv
     for all done (completed) homeworks:
         Student name (who completed homework)
         Creation date
         Teacher name who created homework


Utilize ORM capabilities as much as possible, avoiding executing raw SQL queries.
"""
from pydantic import BaseModel
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from .models import Teacher

class Teacher(BaseModel):
    id: int
    name: str
    email: str

app = FastAPI()

engine = create_engine('postgresql://user:password@localhost/mydatabase')
Session = sessionmaker(bind=engine)

@app.post("/teachers")
async def create_teacher(teacher: Teacher):
    session = Session()
    new_teacher = Teacher(id=teacher.id, name=teacher.name, email=teacher.email)
    session.add(new_teacher)
    session.commit()
    return new_teacher

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.bulk_insert(
        sa.Table('teachers', sa.MetaData(),
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('email', sa.String(), nullable=False),
        ),
        [
            {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com'},
            {'id': 2, 'name': 'Jane Smith', 'email': 'jane.smith@example.com'},
        ]
    )

def downgrade():
    pass

import csv
from fastapi import FastAPI, Response
from .models import Student, Homework, Teacher

app = FastAPI()

@app.get("/report")
async def get_report(response: Response):
    session = Session()
    completed_homeworks = session.query(Homework).filter(Homework.completed == True).all()
    rows = [("Student name", "Creation date", "Teacher name")]
    for homework in completed_homeworks:
        student = session.query(Student).get(homework.student_id)
        teacher = session.query(Teacher).get(homework.teacher_id)
        rows.append((student.name, homework.created_at, teacher.name))
    writer = csv.writer(response.body)
    response.headers["Content-Disposition"] = "attachment; filename=report.csv"
    return writer.writerows(rows)
