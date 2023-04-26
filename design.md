# SDK Design Summary

This SDK provides a Python client for interacting with an API that provides information about The Lord of the Rings trilogy.

Project structure: 

- `resources` is a module that contains modules for each endpoint of the API we're interacting with. 
In this case, we have movie.py and quote.py.

- `client.py` A file that provides a Client class for making HTTP requests to the API. 
This class provides methods for making GET requests(can be extended to make POST, PUT, DELETE, etc.) to the API,
and handles the authentication and authorization required to interact with the API.

- `exceptions.py` is a file that contains a custom exception class that can be raised when an error occurs while interacting with the API in the SDK, 
providing a more informative error message to the user.

- `models.py` A file that provides classes for modeling the data returned by the API, so that it's easier to interact with it. 
These classes define attributes that correspond to the fields returned by the API, and provide methods for working with that data.

- `tests` is a module that contains tests to ensure the functionality of your SDK.

Overall, this SDK design follows a common pattern of organizing code into separate modules for each endpoint of an API, 
using models to represent data returned by the API, and providing unit tests to ensure the functionality and correctness of the SDK. 
The use of a custom exception class also helps provide more informative error messages to the user when errors occur.

