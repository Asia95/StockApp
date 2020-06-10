from flask import Flask, jsonify
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage_key import key

key = key
ts = TimeSeries(key)

app = Flask(__name__)

@app.route("/")
def home():
    aapl, meta = ts.get_daily(symbol='AAPL')
    return aapl


@app.route("/health.json")
def health():
    return jsonify({"status": "UP"}), 200


if __name__ == "__main__":
    app.run(debug=True)