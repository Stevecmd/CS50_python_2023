#!/usr/bin/env python3
# The above line ensures that we are using python3

# Run the program by inserting a band name eg weezer:
# python itunes.py weezer

# Soln 1
# import requests # This enables interaction with HTTP / HTTPS requests ie the internet and pretends to be a browser
# import sys

# # We will target two values, name of a band and name of a song
# if len(sys.argv) !=2:
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# # we are using the request method to get a response from the itunes website with our "sys.argv[1] as the search term"
# # we then print the response in json format
# print(response.json())


# Soln 2
# Python has a library called json which format json responses better
import requests # This enables interaction with HTTP / HTTPS requests ie the internet and pretends to be a browser
import sys
import json

# We will target two values, name of a band and name of a song
if len(sys.argv) !=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
# we are using the request method to get a response from the itunes website with our "sys.argv[1] as the search term"
# limit defines how many results you want to get back
# we then print the response in json format

# print(json.dumps(response.json(), indent=2)) # The indent formats the results better
p = response.json()
for result in p["results"]:
    print(result["trackName"])