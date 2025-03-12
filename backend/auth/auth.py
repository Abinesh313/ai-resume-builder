

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import get_db
# from auth.model import User
# from auth.schemas import UserSignup, UserLogin, TokenResponse
# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from fastapi.security import OAuth2PasswordBearer

# # Secret Key for JWT
# SECRET_KEY = "your-secret-key"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# # ✅ Define the router at the beginning
# router = APIRouter()

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# # Function to hash passwords
# def get_password_hash(password: str) -> str:
#     return pwd_context.hash(password)

# # Function to verify passwords
# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)

# # Function to create JWT token
# def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
#     to_encode = data.copy()
#     expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# # Function to extract user from token
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise HTTPException(status_code=401, detail="Invalid authentication")
#         return username
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")

# # ✅ User Signup Route
# @router.post("/signup", response_model=dict)
# def signup(user: UserSignup, db: Session = Depends(get_db)):
#     if db.query(User).filter(User.username == user.username).first():
#         raise HTTPException(status_code=400, detail="Username already exists")
    
#     hashed_password = get_password_hash(user.password)
#     new_user = User(username=user.username, email=user.email, password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     return {"message": "User created successfully"}

# # ✅ User Login Route
# @router.post("/login", response_model=TokenResponse)
# def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.username == user.username).first()
#     if not db_user or not verify_password(user.password, db_user.password):
#         raise HTTPException(status_code=400, detail="Invalid credentials")

#     access_token = create_access_token(data={"sub": user.username})
#     return {"access_token": access_token, "token_type": "bearer"}

# # ✅ Protected Route - Get User Profile
# @router.get("/profile")
# def get_profile(current_user: str = Depends(get_current_user)):
#     return {"message": f"Hello, {current_user}. Protected route accessed"}




# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from database import get_db
# from auth.model import User
# from auth.schemas import UserSignup, UserLogin, TokenResponse
# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from fastapi.security import OAuth2PasswordBearer

# # Secret Key for JWT
# SECRET_KEY = "your-secret-key"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# # ✅ Define the router at the beginning
# router = APIRouter()

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# # Function to hash passwords
# def get_password_hash(password: str) -> str:
#     return pwd_context.hash(password)

# # Function to verify passwords
# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)

# # Function to create JWT token
# def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
#     to_encode = data.copy()
#     expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# # Function to extract user from token
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise HTTPException(status_code=401, detail="Invalid authentication")
#         return username
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")

# # ✅ User Signup Route (Modified)
# @router.post("/signup", response_model=dict)
# def signup(user: UserSignup, db: Session = Depends(get_db)):
#     if db.query(User).filter(User.username == user.username).first():
#         raise HTTPException(status_code=400, detail="Username already exists")

#     hashed_password = get_password_hash(user.password)
#     new_user = User(
#         name=user.name,  # ✅ Added 'name' field
#         username=user.username,
#         email=user.email,
#         password=hashed_password
#     )
#     db.add(new_user)
#     db.commit()
#     return {"message": "User created successfully"}

# # ✅ User Login Route
# @router.post("/login", response_model=TokenResponse)
# def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.username == user.username).first()
#     if not db_user or not verify_password(user.password, db_user.password):
#         raise HTTPException(status_code=400, detail="Invalid credentials")

#     access_token = create_access_token(data={"sub": user.username})

#     return {
#         "access_token": access_token,
#         "token_type": "bearer",
#         "name": db_user.name  # ✅ Add this field to match the response model
#     }


# # ✅ Protected Route - Get User Profile
# @router.get("/profile")
# def get_profile(current_user: str = Depends(get_current_user)):
#     return {"message": f"Hello, {current_user}. Protected route accessed"}
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from database import get_db
from .model import User
from .schemas import UserSignup, UserLogin, TokenResponse

# ✅ Secret Key & Algorithm for JWT
SECRET_KEY = "your-secret-key"  # Change this in production!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ✅ Initialize router
router = APIRouter(prefix="/auth", tags=["Auth"])

# ✅ Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")  # Correct token URL

# ✅ Helper Functions
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("Decoded Token:", payload)  # Debugging

        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication")

        user = db.query(User).filter(User.id == int(user_id)).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

        return user
    except (JWTError, ValueError) as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token: {str(e)}")

# ✅ User Signup Route
@router.post("/signup", response_model=dict)
def signup(user: UserSignup, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    hashed_password = get_password_hash(user.password)
    new_user = User(
        name=user.name,
        username=user.username,
        email=user.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

# ✅ User Login Route
@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": str(db_user.id)})  # Store `user_id` as a string
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        name=db_user.name
    )

# ✅ Protected Route - Get User Profile
@router.get("/profile")
def get_profile(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}. Protected route accessed"}
