# ================================== Note =======================================
# If you encounter an error indicating that the IMDb module is not found, it means
# that the IMDb library is not installed. To install the library, use the following
# command in your terminal (Command Prompt or Windows PowerShell):
#
#     pip install pandas imdbpy
#
# After installation, it is recommended to restart your system to ensure proper
# configuration of the library.
#
# Additionally, make sure to create a CSV file in the same folder where you plan
# to save the scraped data. If the program encounters an error, it could be due
# to an issue with the API, as APIs sometimes reject requests. In such cases,
# wait a few minutes and try again. Be aware that repeated failed attempts may
# result in your IP address being blocked, as many websites restrict data scraping
# to protect privacy and avoid copyright issues.
#
# Group Members:
# - Zulqarnain Ahmed (BSE-23S-088)
# - Syed Zubair Sarwar (BSE-23S-086)
# ===============================================================================

import csv
import time
from imdb import IMDb

# Create an instance of the IMDb class
ia = IMDb()

# Function to fetch movie details
def fetch_movie_details(movie_id):
    try:
        movie = ia.get_movie(movie_id)
        return {
            'movie_id': movie_id,
            'title': movie.get('title'),
            'genres': ', '.join(movie.get('genres', [])),
        }
    except Exception as e:
        print(f"Error fetching movie {movie_id}: {e}")
        return None

# List to store movie data
movies_data = []

# Fetch details for 60,000 movies
for movie_id in range(1, 62425):
    movie_details = fetch_movie_details(movie_id)
    if movie_details:
        movies_data.append(movie_details)
    
    # Print progress every 100 movies
    if movie_id % 100 == 0:
        print(f"Fetched {movie_id} movies")
    
    # Respectful delay to avoid rate limiting
    time.sleep(0.5)

# Write data to CSV file
with open('movies.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['movie_id', 'title', 'genres']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for movie in movies_data:
        writer.writerow(movie)

print("Data scraping complete. Saved to movies.csv")
