from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pycaret.regression import load_model, predict_model
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

@app.get("/exploration")
async def getExploration(x_param: str, genres = None):
    # FIXME: SQL Injection alert !!!!!!!!!!!!
    query = f"SELECT {x_param} as x, revenue as y FROM MOVIES"
    if (genres):
        genres = genres.split(", ")
        genres = map(lambda genre: f"genres LIKE '%{genre}%'", genres)
        query = query + " WHERE " + (" AND ").join(genres)

    query = query + " LIMIT 10000"

    pairs_q = cursor.execute(query)
    pairs = pairs_q.fetchall();

    count_all_movies_q = cursor.execute("SELECT COUNT(*) FROM movies")
    total_number_of_movies = count_all_movies_q.fetchone()['COUNT(*)']

    average_revenue_q = cursor.execute("SELECT AVG(revenue) FROM movies")
    average_revenue = average_revenue_q.fetchone()['AVG(revenue)']

    average_budget_q = cursor.execute("SELECT AVG(budget) FROM movies")
    average_budget = average_budget_q.fetchone()['AVG(budget)']

    highest_revenue_q = cursor.execute("SELECT MAX(revenue) FROM movies")
    highest_revenue = highest_revenue_q.fetchone()['MAX(revenue)']

    return {
        "plot_dataset": pairs,
        "total_number_of_movies": total_number_of_movies,
        "average_revenue": average_revenue,
        "average_budget": average_budget,
        "highest_revenue": highest_revenue
    }
