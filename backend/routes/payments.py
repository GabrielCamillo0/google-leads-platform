# Integração com Stripe 
import stripe
from fastapi import APIRouter, Request
from backend.config import STRIPE_SECRET_KEY

router = APIRouter()

stripe.api_key = STRIPE_SECRET_KEY

@router.post("/checkout")
def create_checkout_session():
    return {"message": "Sessão de pagamento criada"}

@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    return {"message": "Webhook recebido"}