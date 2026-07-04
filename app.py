from fastapi import FastAPI
from yahooquery import Ticker

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/debug/{ticker}")
def debug(ticker):
    """Usa esto primero para ver EXACTAMENTE qué responde Yahoo desde Render."""
    try:
        t = Ticker(ticker)
        stats = t.key_stats
        raw = stats.get(ticker)
        return {
            "tipo_de_respuesta": str(type(raw)),
            "contenido_crudo": raw,
        }
    except Exception as e:
        return {"error_excepcion": str(e)}


@app.get("/stock/{ticker}")
def stock(ticker):
    try:
        t = Ticker(ticker)
        stats = t.key_stats
        data = stats.get(ticker)

        if isinstance(data, str):
            # Yahoo devolvió un mensaje de error en vez de datos
            return {"error": f"Yahoo devolvió un error para {ticker}: {data}"}

        if not isinstance(data, dict):
            return {"error": f"Respuesta inesperada para {ticker}: {data}"}

        return {
            "forwardPE": data.get("forwardPE"),
            "pegRatio": data.get("pegRatio"),
        }
    except Exception as e:
        return {"error": str(e)}
