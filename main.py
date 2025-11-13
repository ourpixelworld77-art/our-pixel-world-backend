from flask import Flask, jsonify
from pytrends.request import TrendReq
import pandas as pd

app = Flask(__name__)

# Inicializa PyTrends com timeout e retries para evitar erros
pytrends = TrendReq(hl="en-US", tz=0, timeout=(10, 25), retries=3)

@app.route("/trends")
def get_trends():
    try:
        # Região válida: 'united_states' ou 'brazil' etc.
        trends = pytrends.trending_searches(pn="united_states")
        # Retorna apenas os 10 primeiros resultados
        return jsonify(trends.head(10).to_dict())
    except Exception as e:
        # Em caso de erro, retorna mensagem para debug
        return jsonify({"error": str(e)}), 500

@app.route("/custom-trends")
def custom_trends():
    try:
        kw_list = ["Python", "YouTube", "Gaming"]
        pytrends.build_payload(kw_list, timeframe='now 7-d')
        data = pytrends.interest_over_time()
        return jsonify(data.fillna(0).to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
