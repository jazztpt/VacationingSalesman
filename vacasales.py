import fileinput
import os
import requests # this requires the requests library: pip install requests

cities_list = []

for line in fileinput.input():
    cities_list.append(line.strip())

# putting secrets in an enironment variable for security
KEY = os.environ["MAPS_API_KEY"]


def main():
    output = []
    def input_cities_return_distances(cities_list):
        for index, origin, destination in get_next_city(cities_list):
            response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&key={2}".format(origin,destination,KEY))
            try:
                thedistance = response.json()['rows'][0]['elements'][0]['distance']['value']
            except KeyError:
                output.append("can't calculate distance...")

            output.append(thedistance/1000) # distance value expressed in meters
        return output

    def get_next_city(cities_list):
        for index, city in enumerate(cities_list):
            try:
                if index == 0:
                    continue
                origin = cities_list[index-1]
                destination = city
                yield(index, origin, destination)
            except IndexError:
                print "Your file must include more than on city."

    try:
        output = input_cities_return_distances(cities_list)
        print "Success!  Your vacation itinerary is:"
        for index, origin, destination in get_next_city(cities_list):
            distance_between = output[index-1]
            print "    {0} -> {1}:  {2} km".format(origin, destination, str(distance_between))
    except:
        print "We're sorry, we've encountered an unexpected error.  Please contact your vacation administrator for support."



if __name__ == "__main__":
    main()