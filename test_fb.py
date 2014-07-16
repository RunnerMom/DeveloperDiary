#This is a test script to test some basic gets from the FB Graph API
# token is taken from Graph Explorer- needs to be refreshed every hour
# run this in interactive mode python -i test_fb to explore the profile and friends objects


import os
import facebook

token="CAACEdEose0cBAPuqvGGTZAPav8RAKHIEUvTZANRyLEWmtv42snDlUQ7sWlXD0kEO4JEk8UaepUWcUERNGasx7IAGf7wTyBcP4xJLhMGYXVSqxwBbAFiBiMWVQ9Y8K9QEZCtCJBZAyF98xjhEoF9ULyns0WOQYn8DAG2S8GWjxc12NF9TwIXaxKuEALguuKU2D4RLwZCEDthPjw0yp6ulP"

#token=os.environ.get("FACEBOOK_ACCESS_TOKEN")
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

