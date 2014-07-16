#This is a test script to test some basic gets from the FB Graph API
# token is taken from Graph Explorer- needs to be refreshed every hour
# run this in interactive mode python -i test_fb to explore the profile and friends objects


import os
import facebook

token="CAACEdEose0cBABDqMM2pDPimbnvrvfINC0BFCHfEaOS1D7SXCNjIuOgwEmyFrluI3qCg0hs4HEZA4CzoHTHwTlzNKznl9wPgM0BCGhsOqoDqZCfL7LkUGI0Y1okjJ4BoZAZC2z4vtWSlPZBaCLCuZAyDhq1UhuKKyWWRMXH7j2bTP5uc8oZCV627sZBKp9sT0vNpkGZBUBfZBXNHZAeg028DFyM"

#token=os.environ.get("FACEBOOK_ACCESS_TOKEN")
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
picture = graph.get_object("me", fields="picture")
photo = picture['picture']['data']['url']

print photo
# friends = graph.get_connections("me", "friends")
# friendslist = friends['data']

# for friend in friendslist:
# 	print friend['name']
