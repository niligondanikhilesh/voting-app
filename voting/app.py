from flask import Flask, request, jsonify
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379)

@app.route("/")
def index():
    votes_a = redis.get("A") or 0
    votes_b = redis.get("B") or 0
    return f"""
    <h1>🗳️ Vote for your favorite!</h1>
    <form action="/vote" method="post">
        <button name="vote" value="A" style="font-size:30px">🐱 Cats</button>
        <button name="vote" value="B" style="font-size:30px">🐶 Dogs</button>
    </form>
    <p>Current votes → Cats: {int(votes_a)} | Dogs: {int(votes_b)}</p>
    """

@app.route("/vote", methods=["POST"])
@app.route("/", methods=["POST"])
def vote():
    choice = request.form["vote"]
    redis.incr(choice)
    return f"<h2>You voted for {'🐱 Cats' if choice == 'A' else '🐶 Dogs'}!</h2><a href='/'>Vote again</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

