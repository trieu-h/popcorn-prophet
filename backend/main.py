from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

conn = sqlite3.connect('movies.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/movies")
async def get_movies(title:str = "", last_id: int | None = None):
    title = title.strip()
    if title == "":
        return []

    if last_id:
        res = cursor.execute("SELECT * FROM movies WHERE id > ? AND title LIKE ? LIMIT 12", (last_id, '%'+title+'%'));
    else:
        res = cursor.execute("SELECT * FROM movies WHERE title LIKE ? LIMIT 12", ('%'+title+'%', ));

    result = res.fetchall();
    return result

@app.get("/predict")
async def make_prediction():
    result = {
        "verdict": "Blockbuster",
        "confidence": "89"
    }
    return result
