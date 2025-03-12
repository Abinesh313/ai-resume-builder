# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import get_db
# from auth.model import Resume, User  # ✅ Import User properly
# from auth.schemas import ResumeCreate, ResumeUpdate, ResumeResponse
# from auth.auth import get_current_user

# router = APIRouter(prefix="/resume", tags=["Resumes"])

# # ✅ Create Resume
# @router.post("/", response_model=ResumeResponse)
# def create_resume(
#     resume_data: ResumeCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)
# ):
#     new_resume = Resume(
#         user_id=user.id,  # ✅ Now `user.id` works correctly
#         name=resume_data.name,
#         email=resume_data.email,
#         skills=resume_data.skills,
#         experience=resume_data.experience,
#     )
#     db.add(new_resume)
#     db.commit()
#     db.refresh(new_resume)
#     return new_resume

# # ✅ Get All Resumes
# @router.get("/", response_model=list[ResumeResponse])
# def get_resumes(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
#     return db.query(Resume).filter(Resume.user_id == user.id).all()

# # ✅ Get Resume by ID
# @router.get("/{resume_id}", response_model=ResumeResponse)
# def get_resume(resume_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
#     resume = db.query(Resume).filter(Resume.id == resume_id, Resume.user_id == user.id).first()
#     if not resume:
#         raise HTTPException(status_code=404, detail="Resume not found")
#     return resume

# # ✅ Update Resume
# @router.put("/{resume_id}", response_model=ResumeResponse)
# def update_resume(
#     resume_id: int,
#     resume_data: ResumeUpdate,
#     db: Session = Depends(get_db),
#     user: User = Depends(get_current_user)
# ):
#     resume = db.query(Resume).filter(Resume.id == resume_id, Resume.user_id == user.id).first()
#     if not resume:
#         raise HTTPException(status_code=404, detail="Resume not found")

#     for key, value in resume_data.model_dump(exclude_unset=True).items():
#         setattr(resume, key, value)

#     db.commit()
#     db.refresh(resume)
#     return resume

# # ✅ Delete Resume
# @router.delete("/{resume_id}")
# def delete_resume(resume_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
#     resume = db.query(Resume).filter(Resume.id == resume_id, Resume.user_id == user.id).first()
#     if not resume:
#         raise HTTPException(status_code=404, detail="Resume not found")

#     db.delete(resume)
#     db.commit()
#     return {"message": "Resume deleted successfully"}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from auth.model import Resume, User
from auth.schemas import ResumeCreate, ResumeUpdate, ResumeResponse
from auth.auth import get_current_user

router = APIRouter(prefix="/resume", tags=["Resumes"])

# ✅ Create Resume
@router.post("/", response_model=ResumeResponse)
def create_resume(
    resume_data: ResumeCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)
):
    new_resume = Resume(
        user_id=user.id,
        name=resume_data.name,
        email=resume_data.email,
        phone=resume_data.phone,
        summary=resume_data.summary,
        skills=resume_data.skills,
        experience=resume_data.experience,
    )
    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)
    return new_resume

# ✅ Get All Resumes (Only for logged-in user)
@router.get("/", response_model=list[ResumeResponse])
def get_resumes(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return db.query(Resume).filter(Resume.user_id == user.id).all()

# ✅ Get Resume by ID
@router.get("/{resume_id}", response_model=ResumeResponse)
def get_resume(resume_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    resume = db.query(Resume).filter(Resume.id == resume_id, Resume.user_id == user.id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return resume

# ✅ Update Resume
@router.put("/{resume_id}", response_model=ResumeResponse)
def update_resume(
    resume_id: int,
    resume_data: ResumeUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    resume = db.query(Resume).filter(Resume.id == resume_id, Resume.user_id == user.id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    for key, value in resume_data.model_dump(exclude_unset=True).items():
        setattr(resume, key, value)

    db.commit()
    db.refresh(resume)
    return resume

# ✅ Delete Resume
@router.delete("/{resume_id}")
def delete_resume(resume_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    resume = db.query(Resume).filter(Resume.id == resume_id, Resume.user_id == user.id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    db.delete(resume)
    db.commit()
    return {"message": "Resume deleted successfully"}
