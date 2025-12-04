from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pycaret.regression import load_model, predict_model, pull, setup
from pydantic import BaseModel
import pandas as pd
import sqlite3

conn = sqlite3.connect('movies.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
model = load_model('../data-analysis/et_movie_revenue')

class Movie(BaseModel):
    budget: int
    genres: str
    release_month: int
    runtime: int
    popularity: float
    vote_count: int
    vote_average: float
    original_language: str
    number_of_spoken_languages: int 
    number_of_production_companies: int
    number_of_production_countries: int

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

    return res.fetchall()

@app.get("/analytics/{movie_id}")
async def get_analytics_for_move(movie_id: int):
    exec = cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id, ))
    movie = exec.fetchone()
    return pd.DataFrame([dict(movie)])

@app.post("/predict")
async def predict(movie: Movie):
    movie_dict = dict(movie);
    input_df = pd.DataFrame([movie_dict])
    predictions_df = predict_model(estimator=model, data=input_df)
    metrics = cursor.execute("SELECT * FROM metrics")
    metrics_row = metrics.fetchone()
    return {'predicted_revenue': predictions_df.iloc[0]['prediction_label'], **metrics_row}
