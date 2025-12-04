import pandas as pd
import sqlite3
import csv
from pycaret.regression import load_model, predict_model

model = load_model('../data-analysis/et_movie_revenue')
df = pd.read_csv("../data-analysis/movies.csv")

movies = df.copy()
movies = movies[(movies['adult'] == False) & (movies['status'] == 'Released')]
movies = movies.dropna(subset=['production_companies', 'production_countries', 'spoken_languages', 'release_date'])

movies['release_month'] = movies['release_date'].apply(lambda s: int(s.split('-')[1]))
movies['number_of_production_companies'] = movies['production_companies'].apply(lambda s: len(s.split(',')))
movies['number_of_production_countries'] = movies['production_countries'].apply(lambda s: len(s.split(',')))
movies['number_of_spoken_languages'] = movies['spoken_languages'].apply(lambda s: len(s.split(',')))
movies = predict_model(estimator=model, data=movies)
movies = movies.rename(columns={'prediction_label': 'predicted_revenue'})

conn = sqlite3.connect('movies.db');
print("Connecting to database")
cursor = conn.cursor();

cursor.execute("DROP TABLE IF EXISTS \"movies\"")

cursor.execute("""CREATE TABLE "movies" (
	"id"	INTEGER,
	"title"	TEXT,
	"vote_average"	REAL,
	"vote_count"	INTEGER,
	"status"	TEXT,
	"release_date"	TEXT,
	"revenue"	INTEGER,
	"runtime"	INTEGER,
	"adult"	TEXT,
	"backdrop_path"	TEXT,
	"budget"	INTEGER,
	"homepage"	TEXT,
	"imdb_id"	TEXT,
	"original_language"	TEXT,
	"original_title"	TEXT,
	"overview"	TEXT,
	"popularity"	REAL,
	"poster_path"	TEXT,
	"tagline"	TEXT,
	"genres"	TEXT,
	"production_companies"	TEXT,
	"production_countries"	TEXT,
	"spoken_languages"	TEXT,
	"keywords"	TEXT, 
    "release_month" INTEGER,
    "number_of_production_companies" INTEGER, 
    "number_of_production_countries" INTEGER, 
    "number_of_spoken_languages" INTEGER, 
    "predicted_revenue" REAL,
	PRIMARY KEY("id")
) """)
print("\"movies\" table created")

cursor.execute("DROP TABLE IF EXISTS \"metrics\"")

cursor.execute("""CREATE TABLE "metrics" (
    "MAE" REAL,
    "MSE" REAL,
    "RMSE" REAL,
    "R2" REAL,
    "RMSLE" REAL,
    "MAPE" REAL
) """)
print("\"metrics\" table created")

print("Inserting data into tables...")

with open('../data-analysis/metrics.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""INSERT INTO metrics(MAE, MSE, RMSE, R2, RMSLE, MAPE) VALUES (?, ?, ?, ?, ?, ?)""", 
                          (row['MAE'], row['MSE'], row['RMSE'], row['R2'], row['RMSLE'], row['MAPE']))

try:
    movies.to_sql("movies", conn, if_exists='replace', index=False, method="multi", chunksize=10)

except Exception as e:
    print(f"Error during transaction, rolling back: {e}")

conn.close()

