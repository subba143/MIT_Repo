from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/report/")
def get_enrollment_report(db: Session = Depends(get_db)):
    query = text("SELECT * FROM report_student_enrollment()")
    result = db.execute(query)
    report = [
        {
            "Year": row[0],
            "Month": row[1],
            "Institute Name": row[2],
            "Course Name": row[3],
            "Student Count": row[4]
        } for row in result
    ]
    return report
