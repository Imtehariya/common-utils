from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from .models import User  # Import your SQLAlchemy User model
from .config import SECRET_KEY, ALGORITHM  # Import your secret key

def create_access_token(data: dict, expires_in: int = 24):
    """
    Create a JWT token and returns its token.
    """
    expiration = datetime.now() + timedelta(hours=expires_in)
    token = jwt.encode({**data, "exp": expiration}, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_jwt(token: str) -> Optional[dict]:
    """
    Decodes a JWT token and returns its payload if valid.
    Returns None if the token is expired or invalid.
    """
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except JWTError:
        return None  # Invalid token

def verify_forgot_access_token(token: str) -> Optional[str]:
    """
    Verifies a forgot-password JWT token and returns the associated email.
    """
    payload = decode_jwt(token)
    return payload.get("sub") if payload else None

def verify_jwt(token: str) -> Optional[int]:
    """
    Verifies a standard JWT token and returns the user_id.
    """
    payload = decode_jwt(token)
    return payload.get("user_id") if payload else None

def verify_access_token(token: str, db: Session) -> Optional[User]:
    """
    Verifies an access token, fetches the user from the database, and returns the User object.
    """
    user_id = verify_jwt(token)
    return db.query(User).filter(User.id == user_id).first() if user_id else None
