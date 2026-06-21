import pandas as pd

# Category keywords mapping - prioritized by specificity
CATEGORY_KEYWORDS = {
    "Food & Dining": [
        "doordash", "ubereats", "grubhub", "chipotle", "chick-fil-a", "starbucks",
        "mcdonald's", "burger king", "taco bell", "wendy's", "popeyes",
        "harris teeter", "whole foods", "trader joe's", "kroger", "safeway", "sprouts",
        "restaurant", "cafe", "coffee", "pizza", "burger", "sushi", "diner",
        "bistro", "grill", "bbq", "noodles", "ramen", "halal", "dessert",
        "bakery", "smoothie", "juice", "kitchen", "market", "grocery",
        "papa johns", "dominos", "sonic", "chili's", "olive garden", "crunch", "snooze",
        "salty donut", "caribou", "dunkin", "arby's", "panera", "subway",
        "auntie anne's", "cinnabon", "mano bella", "serengeti", "sweet crunch",
        "cakeable", "sabor", "two scoops", "basil thai", "frozen yogurt", "ice cream"
    ],
    "Gas & Transport": [
        "exxon", "chevron", "shell", "bp", "mobil", "texaco", "citgo", "sunoco",
        "gas", "fuel", "petro", "speedway", "circle k", "qt ", "pilot", "love's",
        "uber", "lyft", "taxi", "parking", "transit", "train", "metro",
        "amtrak", "airline", "frontier", "lime", "scooter", "bird app",
        "toll", "metro parking", "parking meter", "valet", "dmv", "carfax"
    ],
    "Phone & Subscriptions": [
        "verizon", "at&t", "t-mobile", "sprint", "metro pcs", "cricket",
        "netflix", "hulu", "disney", "spotify", "apple music", "youtube",
        "adobe", "microsoft", "slack", "zoom", "github", "aws",
        "google", "internet", "cable", "iphone", "apple.com", "playstation",
        "roblox", "xbox", "gaming", "subscription", "premium", "cleverguard",
        "booksy", "instant gaming"
    ],
    "Shopping": [
        "amazon", "ebay", "walmart", "target", "costco", "best buy",
        "home depot", "lowes", "ikea", "five below", "dollar tree", "dollar general",
        "burlington", "tj maxx", "ross", "marshalls", "wayfair", "overstock",
        "etsy", "dhgate", "ali", "wish", "shein", "h&m", "forever 21",
        "clothing", "apparel", "fashion", "shoes", "jeans", "retail",
        "barnes & noble", "cvs", "walgreens", "rite aid", "health", "pharmacy"
    ],
    "Entertainment/Social": [
        "movie", "cinema", "theater", "imax", "concert", "event", "ticket",
        "sports", "stadium", "arena", "gym", "fitness", "dyme boxing",
        "bar", "club", "lounge", "karaoke", "pool", "bowling", "skating",
        "kate's skating", "theme park", "carowinds", "museum", "zoo",
        "queen park", "room 112", "soho bistro", "social", "entertainment"
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
