from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import OpeningProviderSchemas
from app import models

router = APIRouter()


@router.post("/opening_provider", status_code=status.HTTP_201_CREATED)
async def opening_provider_account(
    provider_schema: OpeningProviderSchemas, db: Session = Depends(get_db)
):
    """Opening or creating provider account"""
    new_provider = models.Provider(**provider_schema.model_dump())
    db.add(new_provider)
    db.commit()
    db.refresh(new_provider)
    return new_provider
