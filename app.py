import os
import difflib
import pickle
import h5py
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, send_from_directory, redirect

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_IMG_DIR = os.path.join(BASE_DIR, "static image")

app = Flask(
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=BASE_DIR,
    static_url_path=""
)

# Load book data from h5 file
h5_path = os.path.join(BASE_DIR, "books.h5")
books = None
knn = None
features = None

try:
    if os.path.exists(h5_path):
        with h5py.File(h5_path, "r") as hf:
            books = pickle.loads(hf["books_data"][()])

        books["title"] = books["title"].astype(str)
        books["title_lower"] = books["title"].str.lower()

        from sklearn.neighbors import NearestNeighbors
        from sklearn.preprocessing import OneHotEncoder

        encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
        encoded = encoder.fit_transform(books[["genre", "author"]])
        features = np.hstack((encoded, books[["ratings"]].values))

        knn = NearestNeighbors(n_neighbors=6, metric="cosine")
        knn.fit(features)
        print(f"ML Recommendation Model loaded successfully with {len(books)} books!")
except Exception as e:
    print("Warning: Could not load recommendation model:", e)


def recommend(book_title):
    if books is None or knn is None:
        return ["Recommendation model is initializing or data file is missing."]

    title = book_title.strip().lower()
    matches = difflib.get_close_matches(title, books["title_lower"], n=1, cutoff=0.6)

    if not matches:
        top_genre = books["genre"].mode()[0]
        top_books = books[books["genre"] == top_genre].nlargest(5, "ratings")
        return [
            f"{r['title'].title()} by {r['author'].title()} | Rating: {r['ratings']}"
            for _, r in top_books.iterrows()
        ]

    match_title = matches[0]
    idx = books[books["title_lower"] == match_title].index[0]
    _, indices = knn.kneighbors([features[idx]])

    recommendations = []
    for i in indices[0]:
        if i != idx:
            book_info = f"{books.iloc[i]['title'].title()} by {books.iloc[i]['author'].title()} | Rating: {books.iloc[i]['ratings']}"
            recommendations.append(book_info)

    return recommendations


# --- Routes from templates folder ---

@app.route("/")
@app.route("/landing1.html")
def home():
    return render_template("landing1.html")


@app.route("/about")
@app.route("/index1.html")
def about():
    return render_template("index1.html")


@app.route("/recommend", methods=["GET", "POST"])
def recommend_route():
    result = []
    if request.method == "POST":
        book_name = request.form.get("book_name", "")
        if book_name:
            result = recommend(book_name)
    return render_template("recommend.html", result=result)


# --- Static assets ---

@app.route("/static image/<path:filename>")
def serve_static_image(filename):
    return send_from_directory(STATIC_IMG_DIR, filename)


@app.route("/style1.css")
def serve_style():
    return send_from_directory(TEMPLATES_DIR, "style1.css")


# Fallback routes for other HTML files if needed
@app.route("/index.html")
def catalog():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/landingpage.html")
def landingpage():
    return send_from_directory(BASE_DIR, "landingpage.html")


@app.route("/signin.html", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        return redirect("/")
    return send_from_directory(BASE_DIR, "signin.html")


@app.route("/signup.html", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        return redirect("/")
    return send_from_directory(BASE_DIR, "signup.html")


@app.route("/<path:path>")
def static_proxy(path):
    target = os.path.join(BASE_DIR, path)
    if os.path.isfile(target):
        return send_from_directory(BASE_DIR, path)
    tmpl_target = os.path.join(TEMPLATES_DIR, path)
    if os.path.isfile(tmpl_target):
        return send_from_directory(TEMPLATES_DIR, path)
    return "Page not found", 404


if __name__ == "__main__":
    print("Readify running at http://127.0.0.1:5000")
    print("Home page: http://127.0.0.1:5000/")
    print("About page: http://127.0.0.1:5000/about")
    print("Recommendation page: http://127.0.0.1:5000/recommend")
    app.run(host="127.0.0.1", port=5000, debug=False)
