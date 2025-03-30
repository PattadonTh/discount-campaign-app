from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

from core.item import Item
from core.cart import Cart
from utils.campaigns_loader import load_campaigns

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5050"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


class CampaignRequest(BaseModel):
    campaign_ids: list[str]


@app.post("/apply-discounts")
def apply_discounts(request: CampaignRequest):
    # Load items
    items_path = os.path.join(DATA_DIR, "items.json")
    with open(items_path, "r") as f:
        items_data = json.load(f)
        items = []
        for item in items_data:
            items.append(Item(item["name"], item["price"], item["category"]))


    # Load campaigns
    campaigns_path = os.path.join(DATA_DIR, "campaigns.json")
    with open(campaigns_path, "r") as f:
        campaigns_data = json.load(f)

    # Filter selected campaigns
    selected = [c for c in campaigns_data if c["id"] in request.campaign_ids]

    if not selected:
        raise HTTPException(status_code=404, detail="No valid campaigns selected.")

    # Only one campaign per category
    unique_by_category = {}
    for c in selected:
        cat = c["category"]
        if cat not in unique_by_category:
            unique_by_category[cat] = c

    if len(unique_by_category) < len(selected):
        raise HTTPException(
            status_code=400,
            detail="Only one campaign allowed per category (e.g., Coupon, On Top, Seasonal)."
        )

    # Ordering: Coupon → On Top → Seasonal
    coupon = [c for c in unique_by_category.values() if c["category"] == "Coupon"]
    on_top = [c for c in unique_by_category.values() if c["category"] == "On Top"]
    seasonal = [c for c in unique_by_category.values() if c["category"] == "Seasonal"]

    sorted_campaigns = coupon + on_top + seasonal

    # Convert to Discount objects
    discounts = load_campaigns(sorted_campaigns)

    # Apply discounts
    cart = Cart(items)
    cart.apply_discount(discounts)

    return {"final_price": round(cart.total, 2)}
