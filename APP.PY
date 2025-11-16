from flask import Flask, request, jsonify
from db import query_db
from clip_model import get_text_embedding, get_image_embedding

app = Flask(__name__)

@app.get("/")
def home():
    return {"status": "API RUNNING ✔"}

@app.post("/search/text")
def search_text():
    text = request.json.get("query")
    embedding = get_text_embedding(text)

    rows = query_db("""
        SELECT filename,
               embedding <=> %s AS distance
        FROM images
        ORDER BY embedding <=> %s
        LIMIT 10
    """, (embedding, embedding))

    return jsonify(rows)

@app.post("/search/image")
def search_image():
    file = request.files["image"]
    embedding = get_image_embedding(file)

    rows = query_db("""
        SELECT filename,
               embedding <=> %s AS distance
        FROM images
        ORDER BY embedding <=> %s
        LIMIT 10
    """, (embedding, embedding))

    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
