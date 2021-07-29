from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    if not token == 'tonystark':
        raise HTTPException(
            status_code=401,
            detail="Token not valid",
            headers={"WWW-Authenticate": "Basic"}
        )
    return token
