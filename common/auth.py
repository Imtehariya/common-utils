from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db  # Import your database session dependency
from models import User  # Import your SQLAlchemy User model
from config import SECRET_KEY  # Import your secret key

def create_access_token(user_id: int, expires_in: int = 24):
    expiration = datetime.now() + timedelta(hours=expires_in)
    token = jwt.encode({"user_id": user_id, "exp": expiration}, SECRET_KEY, algorithm="HS256")
    return token

def verify_access_token(token: str, db: Session) -> Optional[User]:
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id: int = payload.get("user_id")
        
        if user_id is None:
            return None  # Invalid token

        # Fetch user from database
        user = db.query(User).filter(User.id == user_id).first()
        return user  # Return full user object
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except JWTError:
        return None  # Invalid token
