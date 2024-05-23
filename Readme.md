# Movie Data Scraping and Recommendation System

## Introduction

This project aims to scrape detailed movie data from IMDb and subsequently develop a movie recommendation system. The scraped data includes movie titles, genres, and unique IMDb IDs. This data will be used to create a recommendation system that can suggest movies based on user preferences.

## Data Scraping

### Scope and Objectives

The goal of the data scraping component is to collect essential movie details for up to 30,000 movies from the IMDb database. The specific data points collected are:

- **Movie ID**: The unique identifier for each movie in the IMDb database.
- **Title**: The official title of the movie.
- **Genres**: The genres associated with the movie (e.g., Drama, Action, Comedy).

### Methodology

1. **IMDb API Usage**:
   - An instance of the `IMDb` class from the `imdbpy` package is used to interface with the IMDb database.
   - For each movie ID in the range from 1 to 60,000, the script retrieves the movie's details.

2. **Data Extraction and Storage**:
   - The relevant details (Movie ID, Title, Genres) are extracted for each movie.
   - The data is stored in a CSV file for subsequent use in the recommendation system.

3. **Rate Limiting Consideration**:
   - To avoid being rate-limited by IMDb, the script includes a delay of 0.5 seconds between successive API requests.

## Recommendation System Development

### Overview

The recommendation system will use the scraped movie data to suggest movies to users based on their preferences. Several algorithms can be employed to create an effective recommendation system, each with its strengths and applicability depending on the context and available data.

### Algorithms Used

1. **Content-Based Filtering**:
   - Recommends movies similar to those a user has liked in the past based on movie attributes such as genres, directors, and cast.

2. **Collaborative Filtering**:
   - Recommends movies based on the preferences of other users with similar tastes.
   - Types include User-User Collaborative Filtering and Item-Item Collaborative Filtering.

3. **Hybrid Methods**:
   - Combines both content-based and collaborative filtering methods to leverage the advantages of both.

### Implementation Plan

1. **Data Preprocessing**:
   - Clean and preprocess the scraped data, ensuring consistency and handling missing values.
   - Convert categorical data (e.g., genres) into numerical format suitable for similarity calculations.

2. **Model Training**:
   - Train content-based filtering models using the preprocessed movie attributes.
   - Train collaborative filtering models using user-movie interaction data (e.g., user ratings).

3. **Evaluation and Optimization**:
   - Evaluate the recommendation system using metrics such as precision, recall, and F1-score.
   - Optimize the model parameters to improve recommendation accuracy.

4. **Deployment**:
   - Deploy the recommendation system as a web or mobile application where users can receive movie suggestions based on their preferences.

## Requirements

- Python 3.x
- pandas
- imdbpy

## Credits 
- This project is made by Zulqarnain Ahmed. 
- I'm the student of Sindh Madressatul Islam University Karachi.
- Currently I'm doing software engineering and I'm in 3rd Semester 
- It's our Semester end Project
- This is only the data which are used in our project consisting of movies data which will be used in our project.
