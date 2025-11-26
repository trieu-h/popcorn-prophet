from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pycaret.regression import load_model, predict_model
import sqlite3
import pandas as pd
from pydantic import BaseModel

conn = sqlite3.connect('movies.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
model = load_model('../data-analysis/et_movie_revenue')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/movies")
async def get_movies(title:str = "", last_id = None):
    title = title.strip()
    if title == "":
        return []

    if last_id:
        res = cursor.execute("SELECT * FROM movies WHERE id > ? AND title LIKE ? LIMIT 12", (last_id, '%'+title+'%'));
    else:
        res = cursor.execute("SELECT * FROM movies WHERE title LIKE ? LIMIT 12", ('%'+title+'%', ));

    rows = res.fetchall()

    movies = [dict(row) for row in rows]
    for movie in movies:
        res = dict(movie);
        input_df = pd.DataFrame([res])
        predictions_df = predict_model(estimator=model, data=input_df)
        print(predictions_df.iloc[0]['prediction_label'])
        movie['predicted_revenue'] = predictions_df.iloc[0]['prediction_label']

    return movies

@app.get("/analytics/{movie_id}")
async def get_analytics_for_move(movie_id: int):
    exec = cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id, ))
    movie = exec.fetchone()
    res = dict(movie);
    input_df = pd.DataFrame([res])
    predictions_df = predict_model(estimator=model, data=input_df)
    res['predicted_revenue'] = predictions_df.iloc[0]['prediction_label']

    return res

class Movie(BaseModel):
    budget: int
    # genres: List[str] = None
    release_month: int
    runtime: int
    popularity: float
    vote_count: int
    vote_average: float
    original_language: str
    number_of_spoken_languages: int 
    number_of_production_companies: int
    number_of_production_countries: int

@app.post("/predict")
async def predict(movie: Movie):
    movie_dict = dict(movie);
    movie_dict['release_date'] = 0
    movie_dict['genres'] = ""
    input_df = pd.DataFrame([movie_dict])
    predictions_df = predict_model(estimator=model, data=input_df)
    print(predictions_df)
    print({'predicted_revenue': predictions_df.iloc[0]['prediction_label']})
    return {'predicted_revenue': predictions_df.iloc[0]['prediction_label']}
