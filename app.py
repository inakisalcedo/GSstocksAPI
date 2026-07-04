from fastapi import FastAPI
from yahooquery import Ticker

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/stock/{ticker}")
def stock(ticker):
    try:
        t = Ticker(ticker)
        stats = t.key_stats
        return stats
    except Exception as e:
        return {"error": str(e)}
