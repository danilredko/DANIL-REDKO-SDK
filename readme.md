The Lord of the Rings SDK

This SDK provides a Python client for interacting with an API that provides information about The Lord of the Rings trilogy.

# Installation
You can install this SDK using pip:
```python
pip install the-lord-of-the-rings-test-sdk==0.1
```
# Configuration
To use this SDK, you need to import the `Client` class and create an instance with the `BASE_URL` of the API and `API_KEY` as an argument:
```python
from the_lord_of_the_rings_sdk.client import Client

API_BASE_URL = "https://the-one-api.dev/v2/"
API_KEY = "your-api-key"
client = Client(API_BASE_URL, API_KEY)
```
# Available Types

| Object | Description                                    |
|--------|------------------------------------------------|
| Client | Client object for making HTTP requests to the API | 
| Movie  | Movie Object                    |


## Movie object 
| Property            | Description                                       |
|---------------------|---------------------------------------------------|
| title               | The title of the movie. | 
| runtime             | The runtime of the movie in minutes.                                 |
| budget              | The budget of the movie in millions of dollars. | 
| revenue             | The box office revenue of the movie in millions of dollars.                                 |
| award_nominations   |  The number of Academy Award nominations the movie received. | 
| award_wins          | The number of Academy Awards the movie won.                                 |
| rotten_tomato_score | The Rotten Tomatoes score of the movie, represented as a percentage.                                 |


# Get all movies
To retrieve information about all movies in The Lord of the Rings trilogy, you can use the get_movies() method:
```python
movies = client.movie.get_movies()
```

# Get a specific movie
To retrieve information about a specific movie in The Lord of the Rings trilogy, you can use the get_movie_by_id() method, which takes the movie ID as an argument:
```python
movie = client.movie.get_movie_by_id(movie_id="5cd95395de30eff6ebccde5c")
```

# Testing

Before running tests, make sure that the `BASE_URL` and `API_KEY` environment variables are set.

To run the tests, execute the following command in the terminal:

```shell
python -m unittest the_lord_of_the_rings_sdk.tests.test 
```
This should be a result: 
```shell
....
----------------------------------------------------------------------
Ran 4 tests in 2.068s

OK
```
