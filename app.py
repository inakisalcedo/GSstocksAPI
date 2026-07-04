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
        stats = t.price
        return stats
    except Exception as e:
        return {"error": str(e)}
