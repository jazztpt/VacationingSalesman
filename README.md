Definitely pressed for time on this one!

I dived in using google maps distance matrix api rather than spend time researching -- I wanted to finish on time.  But with more time I would probably have used something different, probably this:
https://developers.google.com/api-client-library/python/apis/mapsengine/v1?hl=en
if not something like py-googlemaps or another python library.

I created a function as you described, one which 'accepts an ordered list of strings, each string of the form above designating a "City, Country"' and 'returns a list with the distance, in either km or miles, between each successive pair of cities" even though I would create a different structure that included the cities with their distance between (which would also lend itself to memoization if given a really large list) and the text version with its truncated & more readable distance.

Went with more of a "script" style rather than using classes & objects, just for diversity :)

It became clear that I need to figure out how to get the api to return as the crow flies distances rather than driving -- the international cities returned no result :/  That's where the more fully functional api client library would have come in handy.

Created a generator for the repeated code cuz it was fun...though any list of cities is probably not large enough to warrant one.

Put secrets in an environment variable for security.

HOW TO RUN:
First add your google maps api key as the environment variable MAPS_API_KEY
I tried to do exactly what you asked for, so to run do this:
python vacasales.py < cities.txt

Language:
Python, becuase I love it, especially for coding quickly/prototyping
