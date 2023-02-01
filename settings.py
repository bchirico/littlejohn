AVAILABLE_TICKERS = [
    "AAPL",
    "MSFT",
    "GOOG",
    "AMZN",
    "FB",
    "TSLA",
    "NVDA",
    "JPM",
    "BABA",
    "JNJ",
    "WMT",
    "PG",
    "PYPL",
    "DIS",
    "ADBE",
    "PFE",
    "V",
    "MA",
    "CRM",
    "NFLX"
]

SEEDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

TICKER_SEEDS = dict(zip(AVAILABLE_TICKERS, SEEDS))

USERS = [
    'john',
    'mike',
    'paul'
]

USERS_PORTFOLIO = {
    'john': ['AAPL', 'GOOG'],
    'mike': ['GOOG', 'TSLA', 'BABA'],
    'paul': ['BABA']
}