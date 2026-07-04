from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/stock/{ticker}")
def stock(ticker):
    try:
        info = yf.Ticker(ticker).info
        return info
    except Exception as e:
        return {"error": str(e)}
