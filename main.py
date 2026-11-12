from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os

app = FastAPI(title="S.O.AI.Deal Mind")

class Order(BaseModel):
    prompt: str
    location: str = "Cairo"

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", encoding="utf-8") as f:
        return f.read()

@app.get("/health")
async def health():
    return {"status": "ok", "project": "S.O.AI.Deal-Mind"}

@app.post("/api/v1/orchestrate-lifestyle")
async def orchestrate(order: Order):
    return {
        "status": "ready_for_approval",
        "agent_plan": {
            "retail_items": ["Dress - Authentic - Lowest Price", "Shoes - Trusted Seller", "Bag - Authentic"],
            "service_booking": f"Top-rated open salon near {order.location} - Sunday Rescue",
            "cross_merchant_reward_applied": "40% discount unlocked",
            "total_usd": 149.99,
            "summary_message": f"Got it: {order.prompt}. Found authentic outfit + Sunday salon + 40% reward."
        },
        "paypal_checkout": "Connect your PayPal Sandbox keys to enable live checkout"
  }
