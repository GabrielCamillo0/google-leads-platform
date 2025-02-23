# Coleta de leads no Google 
from fastapi import APIRouter

router = APIRouter()

@router.get("/leads")
def get_leads():
    return {"leads": ["Lead1", "Lead2", "Lead3"]}