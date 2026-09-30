# 📚 Readify Recs — Book Recommendation System

### 🔍 Overview

Readify Recs is an intelligent web-based book discovery and recommendation platform designed to help readers effortlessly discover, explore, and evaluate their next favorite books. The application features curated Amazon bestsellers with interactive previews, price details, and direct purchase links alongside an AI-driven recommendation engine powered by Scikit-Learn. By analyzing key book attributes such as genre, author, and user ratings using Nearest Neighbors cosine similarity, Readify provides highly accurate, personalized book suggestions. Developed using Python, Flask, HTML5, CSS3, and JavaScript, it offers a seamless and responsive user experience for literature enthusiasts worldwide.

---

### 🌐 Live Backend Endpoint

> **backend is running on 👉 http://127.0.0.1:5000/recommend**


---

### ✨ Key Features

- **🧠 Machine Learning Recommendations**: Utilizes a K-Nearest Neighbors (KNN) model with cosine distance metric to find books sharing similar stylistic, genre, and rating profiles.
- **🎯 Fuzzy Search Matching**: Integrated with Python's `difflib` to match partial, misspelled, or lowercase book titles with dataset entries.
- **📚 Curated Top 10 Bestsellers**: Showcase of popular titles including *Atomic Habits*, *The Alchemist*, *Norwegian Wood*, *Sapiens*, and more with interactive "Learn More" details.
- **⚡ Lightweight Flask Architecture**: Fast, modular REST routing serving dynamic Jinja2 templates and high-resolution book cover assets.
- **🎨 Responsive UI**: Warm, clean aesthetic built with custom CSS and modern typography.

---

### ⚙️ Tech Stack

- **Backend**: Python 3, Flask
- **Machine Learning & Data**: Scikit-learn (NearestNeighbors, OneHotEncoder), Pandas, NumPy, H5py
- **Frontend**: HTML5, CSS3, JavaScript, Jinja2 Templating
- **Dataset**: `books.h5` containing 1,291 curated book titles, authors, genres, and ratings

---

### 📁 Project Structure

```text
Readify/
│
├── app.py                  # Main Flask application & ML routing
├── books.h5               # Serialized book dataset (1,291 books)
├── encoder.pkl            # Trained OneHotEncoder for genre/author
├── knn_model.pkl          # Trained NearestNeighbors model
├── requirements.txt       # Python project dependencies
│
├── static image/          # High-resolution book cover assets
│   ├── atomic-habits-dots.png
│   ├── norwegian wood.jpg
│   ├── thealchemist.jpg
│   ├── sapiens.jpg
│   └── ...
│
├── templates/             # Jinja2 HTML templates
│   ├── landing1.html      # Home page (Top 10 Amazon books)
│   ├── index1.html        # About page
│   ├── recommend.html     # AI book recommendation engine
│   └── style1.css         # Custom styling
│
├── .gitignore             # Git ignore configuration
└── README.md              # Project documentation
```

---

### 🚀 How to Run Locally

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/zoyashaikh3/Readify-Recs.git
cd Readify-Recs
```

#### 2️⃣ Setup Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On macOS/Linux
```

#### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Launch the Application
```bash
python app.py
```

✅ The application will start at:
👉 **http://127.0.0.1:5000**

Visit **http://127.0.0.1:5000/recommend** to test the recommendation engine!

---

### 🧩 How the Recommendation Engine Works

1. **Title Matching**: When a user enters a book title, the system performs fuzzy text matching to locate the book within the 1,291-title dataset.
2. **Feature Extraction**: Categorical features (genre, author) are transformed using One-Hot Encoding and combined with normalized rating metrics.
3. **Nearest Neighbors Query**: The query book's vector is evaluated against the dataset using cosine distance to locate the 5 closest neighbors.
4. **Result Delivery**: Top matching titles, authors, and ratings are displayed instantly on the recommendation dashboard.

---

### 📜 License

This project is open-source and available under the [MIT License](LICENSE).
