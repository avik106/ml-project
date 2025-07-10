
# 🎬 Movie Recommender System (TF-IDF Based)

A content-based movie recommendation system built using **TF-IDF Vectorization**. This system suggests similar movies based on the plot/overview of a selected movie.

---

## 🚀 Demo

Try it live (optional): [https://movie-recommender-fe2cggrsftnmmfmeifovx8.streamlit.app/](#)  

---

## 📌 Features

- Content-based filtering using **TF-IDF Vectorizer**
- Cosine similarity for comparing movie plots
- Clean and intuitive interface using **Streamlit**
- Suggests top similar movies based on selected input

---

## 🧠 How It Works

1. **Data**: Loads a movie dataset with titles and plot overviews.
2. **TF-IDF Vectorizer**: Converts text overviews into numeric vectors.
3. **Similarity Measure**: Computes **cosine similarity** between all movie vectors.
4. **Recommendation**: For a given movie, returns top N most similar ones.

---

## 🗂️ Dataset

- Source: [TMDB 5000 Movie Dataset]
- tmdb_5000_credits.csv
- tmdb_5000_movies.csv
- Fields used:
  - `title`
  - `overview`

---

## 📦 Libraries Used

- `pandas`
- `numpy`
- `scikit-learn`
- `streamlit` (for web UI)
- `pickle` (for saving model)

---

