# Sistema básico de gamificação 
from fastapi import APIRouter

router = APIRouter()

@router.get("/gamification/points")
def get_user_points(username: str):
    return {"username": username, "points": 100}