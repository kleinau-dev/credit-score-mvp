from fastapi import APIRouter
from app.api.auth import router as auth_router
from app.api.financial import router as financial_router
from app.api.score import router as score_router
from app.api.user import router as user_router
from app.api.consent import router as consent_router
from app.api.admin_score_rules import router as admin_score_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(financial_router)
router.include_router(score_router)
router.include_router(user_router)
router.include_router(consent_router)
router.include_router(admin_score_router)