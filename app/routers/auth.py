from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, utils, schemas, oauth2


router = APIRouter()


@router.post("/login")
async def login(
    user_crendential: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = (
        db.query(models.User)
        .filter(models.User.email == user_crendential.username)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credential"
        )

    if not utils.hash(user_crendential.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credential"
        )
    access_token = oauth2.create_access_token({"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
