import pandas as pd
df = pd.read_csv("../data-analysis/movies.csv")
movies = df.copy()
movies = movies[(movies['adult'] == False) & (movies['status'] == 'Released')]
movies = movies.dropna(subset=['production_companies', 'production_countries', 'spoken_languages', 'release_date'])
movies['release_month'] = movies['release_date'].apply(lambda s: int(s.split('-')[1]))
movies['number_of_production_companies'] = movies['production_companies'].apply(lambda s: len(s.split(',')))
movies['number_of_production_countries'] = movies['production_countries'].apply(lambda s: len(s.split(',')))
movies['number_of_spoken_languages'] = movies['spoken_languages'].apply(lambda s: len(s.split(',')))
movies.to_csv('movies-db.csv', index=False)

