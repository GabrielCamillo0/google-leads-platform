# Inicialização do FastAPI 

from fastapi import FastAPI
from backend.routes import leads, users, payments

app = FastAPI()

app.include_router(leads.router)
app.include_router(users.router)
app.include_router(payments.router)

@app.get("/")
def read_root():
    return {"message": "Google Leads Platform está funcionando!"}
