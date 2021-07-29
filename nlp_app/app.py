from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import secrets

# TO BE COMPLETED DURING THE WEBINAR


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    correct_username = secrets.compare_digest(form_data.username, 'username') # to be changed
    correct_password = secrets.compare_digest(form_data.password, 'password') # to be changed
    if not(correct_username and correct_password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password"
        )
    return {"access_token": form_data.username, "token_type": "bearer"}


# TO BE COMPLETED DURING THE WEBINAR
