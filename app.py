from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/stock/{ticker}")
def stock(ticker):
    try:
        t = yf.Ticker(ticker)
        info = t.info
        fast = t.fast_info
        return {
            "currentPrice": fast.get("lastPrice"),
            "forwardPE": info.get("forwardPE"),
            "pegRatio": info.get("pegRatio")
        }
    except Exception as e:
        return {"error": str(e)}
