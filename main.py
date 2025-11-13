from pytrends.request import TrendReq
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/trends")
def get_trends():
    pytrends = TrendReq(hl="en-US", tz=0)
    trends = pytrends.trending_searches(pn="united_states")
    return jsonify(trends.head(10).to_dict())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
