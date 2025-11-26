export type Status = 'Released';

export type Movie = {
  id: number;
  adult: string; // "True" | False" -> Probably fine for now
  backdrop_path: string;
  budget: number;
  genres: string;
  homepage: string;
  imdb_id: string;
  keywords: string;
  original_language: string;
  original_title: string;
  overview: string;
  popularity: number;
  poster_path: string | null;
  production_companies: string;
  production_countries: string;
  release_date: string;
  revenue: number;
  runtime: number;
  spoken_languages: string;
  status: Status;
  tagline: string;
  vote_average: number;
  vote_count: number;
  number_of_production_companies: number;
  number_of_production_countries: number;
  number_of_spoken_languages: number;
  release_month: number;
  predicted_revenue?: number;
}

export type Prediction {
  predicted_revenue: number;
}
