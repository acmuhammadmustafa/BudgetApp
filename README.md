#  Budget App

A full-stack budgeting application that parses Bank of America CSV exports, categorizes transactions, and provides real-time spending insights.

## Tech Stack

- **Backend**: Python + FastAPI
- **Frontend**: React + Vite
- **Charts**: Recharts
- **Styling**: Tailwind CSS
- **Data**: BofA CSV exports

## Project Structure

```
budget-app/
├── backend/
│   ├── main.py          # FastAPI server
│   ├── parser.py        # CSV transaction parser
│   ├── categorizer.py   # Auto-categorize transactions
│   ├── requirements.txt
│   └── venv/            # Python virtual environment
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   ├── PieChart.jsx       # Spending by category
│   │   │   ├── SpendingTracker.jsx # Summary stats
│   │   │   ├── BudgetBar.jsx      # Budget progress
│   │   │   └── Projection.jsx     # Savings forecast
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   └── node_modules/
└── README.md
```

## Setup Instructions

### Backend Setup

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Create and activate Python virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or: source venv/bin/activate  # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run FastAPI server:
   ```bash
   python main.py
   ```
   Server runs on `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start development server:
   ```bash
   npm run dev
   ```
   App runs on `http://localhost:5173`

## Budget Categories

- **Food & Dining** - $500/month
- **Gas & Transport** - $300/month
- **Phone & Subscriptions** - $150/month
- **Shopping** - $400/month
- **Entertainment/Social** - $250/month
- **Savings** - Unlimited

## How to Use

1. Get your BofA transactions:
   - Log into your Bank of America account
   - Find "Download Transactions" or "Download CSV"
   - Select last 3 months of data
   - Download as CSV

2. Upload to Budget App:
   - Start both backend and frontend servers
   - Open http://localhost:5173
   - Upload your CSV file

3. View Analytics:
   - See spending breakdown by category (pie chart)
   - Track budget progress (remaining vs. spent)
   - View daily/monthly savings projection
   - Get automatic transaction categorization

## API Endpoints

- `POST /upload` - Upload BofA CSV file
- `GET /categories` - Get budget categories
- `GET /summary` - Get spending summary
- `GET /` - Health check

## Future Enhancements

- [ ] Recurring transaction detection
- [ ] Monthly budget reset
- [ ] Customizable categories
- [ ] Email spending alerts
- [ ] Mobile-responsive improvements
- [ ] Transaction search/filter
- [ ] Export reports to PDF

## Notes

- CSV parser is flexible and handles BofA format variations
- Transactions are auto-categorized based on keywords
- Projection is based on average daily spending/income
- All data is processed locally (no external storage)
