# 🎬 FastAPI ML Recommendation System

An ML-based movie recommendation system built using FastAPI, leveraging similarity-based techniques to suggest movies for users. The project is containerized using Docker for easy deployment.

---

## 🚀 Features

- Movie recommendation based on user similarity
- FastAPI backend
- Machine Learning model
- Docker support
- Clean project structure

---

## 🧠 Tech Stack

- Python
- FastAPI
- Pandas, NumPy, Scikit-learn
- Uvicorn
- Docker

---

## 📂 Project Structure


app/
- main.py
- routes.py
- recommender.py

data/
- movies.csv
- ratings.csv
- tags.csv

ml/
- training.ipynb

models/ (ignored)

Dockerfile  
requirements.txt  
.gitignore  

---

## ⚙️ Run (Local)

pip install -r requirements.txt  
uvicorn app.main:app --reload  

Open: http://127.0.0.1:8000/docs

---

## 🐳 Run (Docker)

docker build -t fastapi-ml-app .  
docker run -p 8000:8000 fastapi-ml-app  

---

## 📡 API

GET /health  
GET /recommend?user_id=1  

---

## 📊 How it works

- User-movie interaction matrix is created
- Similarity is calculated between users
- Top similar users are selected
- Movies not watched by current user are recommended
Model (.pkl files) are not uploaded. They are created during training.

---

## 👨‍💻 Author

Mohith Ram Garaga
