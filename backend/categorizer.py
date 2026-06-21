import pandas as pd

# Category keywords mapping
CATEGORY_KEYWORDS = {
    "Food & Dining": [
        "restaurant", "cafe", "coffee", "pizza", "burger", "sushi", "food", "doordash",
        "ubereats", "grubhub", "chipotle", "mcdonalds", "starbucks", "grocery", "whole foods",
        "trader joe's", "target", "walmart", "safeway", "kroger", "sprouts", "safeway"
    ],
    "Gas & Transport": [
        "gas", "shell", "chevron", "bp", "exxon", "mobil", "parking", "uber", "lyft",
        "transit", "parking", "toll", "metro", "train", "amtrak", "airline", "airline",
        "costco gas", "fred meyer", "chevron", "texaco"
    ],
    "Phone & Subscriptions": [
        "verizon", "at&t", "t-mobile", "sprint", "phone", "subscription", "netflix",
        "hulu", "disney", "spotify", "apple music", "adobe", "microsoft", "slack", "zoom",
        "github", "aws", "google", "internet", "cable", "iphone"
    ],
    "Shopping": [
        "amazon", "ebay", "store", "shop", "retail", "target", "costco", "walmart",
        "best buy", "home depot", "lowes", "ikea", "mall", "mall", "clothing", "apparel"
    ],
    "Entertainment/Social": [
        "movie", "cinema", "theater", "concert", "event", "ticket", "sports", "gym",
        "fitness", "bar", "club", "karaoke", "entertainment", "theme park", "museum"
    ],
}


def categorize_transactions(df):
    """
    Automatically categorize transactions based on description keywords
    """
    df = df.copy()
    df['category'] = 'Savings'  # Default category

    # Match keywords (case-insensitive)
    description_lower = df['description'].str.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            mask = description_lower.str.contains(
                keyword, case=False, na=False)
            df.loc[mask, 'category'] = category

    return df[['date', 'description', 'amount', 'category']]
