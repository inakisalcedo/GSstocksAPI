from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/stock/{ticker}")
def stock(ticker):
    try:
        ticker = yf.Ticker(ticker)
        info = ticker.get_info()
        return info
    except Exception as e:
        return {"error": str(e)}
