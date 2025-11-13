from pytrends.request import TrendReq
from flask import Flask, jsonify
import pandas as pd
from utils import get_custom_trends  # opcional, se quiser funções extras

app = Flask(__name__)

@app.route("/trends")
def get_trends():
    try:
        pytrends = TrendReq(hl="en-US", tz=0)
        trends = pytrends.trending_searches(pn="united_states")
        return jsonify(trends.head(10).to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/custom-trends")
def custom_trends():
    data = get_custom_trends()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
