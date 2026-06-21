from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import StringIO
from parser import parse_bofa_csv
from categorizer import categorize_transactions

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Budget categories
BUDGET_CATEGORIES = {
    "Food & Dining": 500,
    "Gas & Transport": 300,
    "Phone & Subscriptions": 150,
    "Shopping": 400,
    "Entertainment/Social": 250,
    "Savings": 0,  # No limit for savings
}


@app.get("/")
def read_root():
    return {"message": "Budget App API"}


@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    """Upload and parse BofA CSV file"""
    try:
        content = await file.read()
        df = parse_bofa_csv(content)
        transactions = categorize_transactions(df)

        return {
            "success": True,
            "transactions": transactions.to_dict(orient="records"),
            "summary": {
                "total": float(df["amount"].sum()),
                "count": len(df)
            }
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


@app.get("/categories")
def get_categories():
    """Get budget categories and limits"""
    return {"categories": BUDGET_CATEGORIES}


@app.get("/summary")
def get_summary(transactions: list = None):
    """Get spending summary by category"""
    if not transactions:
        return {"categories": {}}

    summary = {}
    for cat in BUDGET_CATEGORIES:
        summary[cat] = {"spent": 0, "budget": BUDGET_CATEGORIES[cat]}

    return {"summary": summary}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
