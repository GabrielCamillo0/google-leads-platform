# Painel de administração 
from fastapi import APIRouter

router = APIRouter()

@router.get("/admin/dashboard")
def admin_dashboard():
    return {"message": "Painel administrativo acessado"}