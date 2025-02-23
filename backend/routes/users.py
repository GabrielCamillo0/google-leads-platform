# Gestão de usuários 
from fastapi import APIRouter, HTTPException
from backend.database import cursor, conn

router = APIRouter()

@router.get("/users/{username}")
def get_user(username: str):
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"username": user[1], "plan": user[3]}