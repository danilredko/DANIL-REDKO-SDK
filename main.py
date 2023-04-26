import os

from the_lord_of_the_rings_sdk.client import Client

API_BASE_URL = os.environ.get("BASE_URL")
API_KEY = os.environ.get("API_KEY")
client = Client(API_BASE_URL, API_KEY)

print(client.movie.get_movies())
print(client.movie.get_movie_by_id(movie_id="5cd95395de30eff-6ebccde5c"))
