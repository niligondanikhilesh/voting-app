from flask import Flask, jsonify
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379)

@app.route("/")
def results():
    votes_a = int(redis.get("A") or 0)
    votes_b = int(redis.get("B") or 0)
    total = votes_a + votes_b
    return f"""
    <h1>📊 Live Results!</h1>
    <h2>🐱 Cats: {votes_a} votes ({round(votes_a/total*100) if total > 0 else 0}%)</h2>
    <h2>🐶 Dogs: {votes_b} votes ({round(votes_b/total*100) if total > 0 else 0}%)</h2>
    <h3>Total votes: {total}</h3>
    <a href="/">Go back to voting</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

