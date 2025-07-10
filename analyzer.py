import sys
import re
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter

# A small set of English stopwords to filter out common words
STOPWORDS = {
    "the","and","for","you","that","with","this","have","not","but",
    "are","was","just","all","from","they","your","like","out","get",
    "has","what","when","where","who","how","why","then","them","were",
    "will","can","its","our","about","them","there","would"
}

def fetch_thread(board: str, thread_id: str):
    """Fetch thread JSON and return list of raw comment texts."""
    url = f"https://a.4cdn.org/{board}/thread/{thread_id}.json"
    resp = requests.get(url)
    resp.raise_for_status()
    posts = resp.json().get("posts", [])
    texts = []
    for post in posts:
        comment = post.get("com", "")
        # Remove HTML tags
        plain = re.sub(r"<[^>]+>", "", comment)
        texts.append(plain)
    return texts

def analyze_sentiment(texts):
    """Return counts of positive, negative, and neutral posts."""
    analyzer = SentimentIntensityAnalyzer()
    counts = {"positive":0, "negative":0, "neutral":0}
    for txt in texts:
        score = analyzer.polarity_scores(txt)["compound"]
        if score >= 0.05:
            counts["positive"] += 1
        elif score <= -0.05:
            counts["negative"] += 1
        else:
            counts["neutral"]  += 1
    return counts

def extract_keywords(texts, top_n=10):
    """Return the top_n most common words (minus stopwords)."""
    words = []
    for txt in texts:
        # lowercase, split on non‑letters
        for w in re.findall(r"[a-zA-Z]{3,}", txt.lower()):
            if w not in STOPWORDS:
                words.append(w)
    return Counter(words).most_common(top_n)

def main():
    if len(sys.argv) != 3:
        print("Usage: python analyzer.py [board] [thread_id]")
        sys.exit(1)

    board, thread_id = sys.argv[1], sys.argv[2]
    print(f"Fetching /{board}/ thread {thread_id}…")
    texts = fetch_thread(board, thread_id)
    print(f"  ↳ Retrieved {len(texts)} posts")

    sent = analyze_sentiment(texts)
    print("\nSentiment counts:")
    for k,v in sent.items():
        print(f"  {k.title():>8}: {v}")

    keywords = extract_keywords(texts, top_n=10)
    print("\nTop 10 keywords:")
    for word, cnt in keywords:
        print(f"  {word:>10} — {cnt}")

if __name__ == "__main__":
    main()
