from flask import Flask, render_template, request, jsonify
import pandas as pd
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Flask app
app = Flask(__name__)

data = pd.read_csv("movies_metadata.csv")

# Droping rows with missing values in important columns
data.dropna(subset=['title', 'genres', 'popularity', 'runtime', 'release_date'], inplace=True)

# Converting columns to appropriate formats
data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
data['genres'] = data['genres'].fillna('').str.lower()  
data['popularity'] = pd.to_numeric(data['popularity'], errors='coerce').fillna(0)
data['runtime'] = pd.to_numeric(data['runtime'], errors='coerce').fillna(0)

# Function to recommend movies by multiple factors
def recommend_movies_by_factors(
    genres=None, min_popularity=0, max_runtime=None, year_range=None, data=data, top_n=10
):
    filtered_df = data

    # Filter by genres
    if genres:
        genres = [g.lower() for g in genres]
        filtered_df = filtered_df[filtered_df['genres'].apply(
            lambda x: any(genre in x for genre in genres)
        )]

    # Filter by popularity
    filtered_df = filtered_df[filtered_df['popularity'] >= min_popularity]

    # Filter by runtime
    if max_runtime:
        filtered_df = filtered_df[filtered_df['runtime'] <= max_runtime]

    # Filter by year range
    if year_range:
        start_year, end_year = year_range
        filtered_df = filtered_df[
            (filtered_df['release_date'].dt.year >= start_year) &
            (filtered_df['release_date'].dt.year <= end_year)
        ]

    # Sort by popularity and return top recommendations
    filtered_df = filtered_df.sort_values(by='popularity', ascending=False)
    return filtered_df.head(top_n)[['title', 'genres', 'popularity', 'release_date', 'runtime']]

# Home route to render the UI
@app.route('/')
def index():
    return render_template('index.html')

# Route to get movie recommendations
@app.route('/recommend', methods=['GET'])
def recommend():
    # Retriving user input from the form
    genres = request.args.getlist('genres')
    min_popularity = float(request.args.get('min_popularity', 0))
    max_runtime = request.args.get('max_runtime', None)
    if max_runtime:
        max_runtime = int(max_runtime)
    year_range = request.args.get('year_range', None)
    if year_range:
        start_year, end_year = map(int, year_range.split('-'))
        year_range = (start_year, end_year)
    top_n = int(request.args.get('top_n', 10))

    # Movie recommendations
    recommendations = recommend_movies_by_factors(
        genres=genres, 
        min_popularity=min_popularity, 
        max_runtime=max_runtime, 
        year_range=year_range, 
        data=data, 
        top_n=top_n
    )

    recommendations = recommendations.to_dict(orient='records')
    
    # Returning recommendations in JSON format for frontend
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
