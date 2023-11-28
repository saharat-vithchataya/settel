from fastapi import APIRouter
from app.routers import provider, user, auth

router = APIRouter()

router.include_router(router=provider.router, prefix="/providers", tags=["Providers"])
router.include_router(router=user.router, prefix="/users", tags=["User"])
router.include_router(router=auth.router, prefix="/auth", tags=["Auth"])
