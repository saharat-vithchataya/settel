from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, models, utils, oauth2

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user_account(
    user_schema: schemas.UserRegistrationSchemas, db: Session = Depends(get_db)
):
    user_schema.password = utils.hash(user_schema.password)
    new_user = models.User(**user_schema.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserResponse,
)
async def get_user_infomation(
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):
    user = db.query(models.User).filter(models.User.id == current_user.id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return user
