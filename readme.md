# Movie Recommendation System

## Overview

This project is a Python-based movie recommendation system built using Flask and Pandas. It processes a movie dataset and allows users to filter and explore movie recommendations based on various criteria such as genres, popularity, runtime, and release year range.

---

## Features

- **Data Preprocessing:**
  - Handles missing values and converts data to appropriate formats.
  - Columns like `genres`, `popularity`, `runtime`, and `release_date` are cleaned for consistent analysis.

- **Exploratory Data Analysis (EDA):**
  - Analyze the top 5 movies based on popularity, runtime, ratings, and vote count.
  - Visualize the results using Seaborn and Matplotlib.

- **Recommendation Functionality:**
  - Multi-factor filtering based on genres, popularity, runtime, and release year range.
  - Allows users to specify multiple filters and get personalized recommendations.

- **Flask Web Interface:**
  - Web-based UI for inputting filters and displaying recommendations.

---

## Prerequisites

- Python 3.7+
- Flask
- Pandas
- Matplotlib
- Seaborn

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the `movies_metadata.csv` file is present in the project directory. This dataset contains metadata for movies.

---

## Usage

1. **Run the Flask Application:**
   ```bash
   python app.py
   ```

2. **Access the Web Interface:**
   Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

3. **Filter Movies:**
   - Select genres, set popularity thresholds, runtime limits, and release year range.
   - View recommended movies on the same page.

---

## Directory Structure

```
movie-recommendation-system/
├── app.py               # Main Flask application
├── movies_metadata.csv  # Dataset file
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # HTML template for the web interface
└── static/
    └── styles.css       # (Optional) Custom CSS for the UI
```

---

## Dataset Details

The `movies_metadata.csv` dataset includes the following key columns:
- `title`: Movie title.
- `genres`: List of genres the movie belongs to.
- `popularity`: Popularity score of the movie.
- `runtime`: Movie duration in minutes.
- `release_date`: Release date of the movie.
- `vote_average`: Average rating given by users.
- `vote_count`: Number of votes the movie received.

---

## Example API Usage

You can send GET requests to `/recommend` with the following parameters:

- `genres`: List of genres to filter by (e.g., `Action`, `Comedy`).
- `min_popularity`: Minimum popularity threshold (default: `0`).
- `max_runtime`: Maximum runtime in minutes.
- `year_range`: Release year range in `YYYY-YYYY` format.
- `top_n`: Number of recommendations to return (default: `10`).

Example request:
```
http://127.0.0.1:5000/recommend?genres=Action&min_popularity=50&max_runtime=120&year_range=2000-2020&top_n=5
```

---

## Future Improvements

- Add support for user ratings and collaborative filtering.
- Enhance UI with more interactive filters.
- Include additional datasets for better recommendations.
- Deploy the application to a cloud platform like AWS or Heroku.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Acknowledgements

- The dataset used in this project is sourced from [Kaggle](https://www.kaggle.com).

---


