#This is a test script to test some basic gets from the FB Graph API
# token is taken from Graph Explorer- needs to be refreshed every hour
# run this in interactive mode python -i test_fb to explore the profile and friends objects


import os
import facebook

token="CAACEdEose0cBAAxtuBGalsZC2aZAZBm2x1L2zixtZCA3zbjfZAiukpbBZCjI6SNkR95jekixh64mWtw4qxZBLYxyZC677nSMor74jxmzxli7W4OuHtSugXiyBZCxK88UbSTyu7YUg4eYyFIMuHAzwmWlqDZAUggPgSAk0y9iphvYqHZBl1dVkvBr0vtt1nil9a9Lv1LCS2ZBmPyon7wAYfmVDzyI"

#token=os.environ.get("FACEBOOK_ACCESS_TOKEN")
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")
friendslist = friends['data']

for friend in friendslist:
	print friend['name']
