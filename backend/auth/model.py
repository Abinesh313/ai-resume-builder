# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from database import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100), nullable=False)  
#     username = Column(String(50), unique=True, nullable=False)  
#     email = Column(String(100), unique=True, nullable=False)  
#     password = Column(String(255), nullable=False)  

#     resumes = relationship("Resume", back_populates="user")  # ✅ Relationship

# class Resume(Base):
#     __tablename__ = "resumes"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100), nullable=False)  
#     email = Column(String(100), nullable=False)  
#     phone = Column(String(20), nullable=False)  
#     summary = Column(String(500), nullable=True)  
#     skills = Column(String(500), nullable=False)  # ✅ Added field
#     experience = Column(String(1000), nullable=False)  # ✅ Added field
#     user_id = Column(Integer, ForeignKey("users.id"))

#     user = relationship("User", back_populates="resumes")
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    resumes = relationship("Resume", back_populates="user")

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    summary = Column(String(500), nullable=True)
    skills = Column(String(500), nullable=False)
    experience = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="resumes")
