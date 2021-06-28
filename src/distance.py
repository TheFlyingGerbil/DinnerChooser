import requests
import json
# call the OSMR API
r = requests.get(f"http://router.project-osrm.org/route/v1/car/{-122.17986},{47.41711};{-122.19786},{47.44439}?overview=false")
# then you load the response using the json libray
# by default you get only one alternative so you access 0-th element of the `routes`
routes = json.loads(r.content)
print(type(routes))
#print(routes)
route_1 = routes.get("routes")[0]