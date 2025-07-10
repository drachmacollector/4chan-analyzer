from flask import Flask, request, jsonify
from flask_cors import CORS
from analyzer import fetch_thread, analyze_sentiment, extract_keywords

app = Flask(__name__)
CORS(app)  # allow all origins; for hackathon simplicity

@app.route("/analyze", methods=["GET"])
def analyze():
    # Expect URL params: ?board=g&thread_id=12345
    board     = request.args.get("board")
    thread_id = request.args.get("thread_id")

    if not board or not thread_id:
        return jsonify({"error": "Provide both 'board' and 'thread_id' parameters"}), 400

    try:
        texts     = fetch_thread(board, thread_id)
        sentiment = analyze_sentiment(texts)
        keywords  = extract_keywords(texts, top_n=10)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Build a JSON‑friendly structure
    return jsonify({
        "board": board,
        "thread_id": thread_id,
        "post_count": len(texts),
        "sentiment": sentiment,
        "keywords": [
            {"word": w, "count": c} for w, c in keywords
        ],
    })

if __name__ == "__main__":
    # Run on port 5000 by default
    app.run(debug=True, port=5000)
