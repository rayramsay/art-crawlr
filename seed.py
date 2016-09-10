import os
import json
import googlemaps

#from model import Artwork

#from model import connect_to_db, db
#from server import app

# Remember to ``source secrets.sh``!
# gmaps = googlemaps.Client(key=os.environ['GOOGLE_API_SERVER_KEY'])


def get_zip(lat, lng):
    """Given lat and lng, returns zipcode."""

    reverse_geocode_result = gmaps.reverse_geocode((lat, lng))
    zipcode = reverse_geocode_result[0]["address_components"][-1]["long_name"]

    return zipcode


# def dictify(string):
#     """Given a JSON string, make it into a dictionary."""
#     return json.loads(string)


def load_artworks():
    """Load artworks from seed data into database."""

    print "Artworks"

    # Read SF_Civic_Art_Collection.csv file and insert data.
    
art_seed = open("seed_data/SF_Civic_Art_Collection.json")
json_dict = json.load(art_seed)
art_list = json_dict['data']

for item in art_list:
    artist = item[11]
    credit_line = item[13]
    latlongstring = json.loads(item[15])
    lat = latlongstring['coordinates'][0]
    lng = latlongstring['coordinates'][1]
    location_description = item[16]
    medium = item[17]
    title = item[19]




        #lat, lng = geometry["coordinates"]

        #zipcode = get_zip(lat, lng)

        #print artist, credit_line, geometry, lat, lng, location_description, medium, title, zipcode



    #     artwork = Artwork(
    #                     artist=artist,
    #                     credit_line=credit_line,
    #                     lat=lat,
    #                     lng=lng,
    #                     location_description=location_description,
    #                     medium=medium,
    #                     title=title,
    #                     zipcode=zipcode


    #                      )

    #     # We need to add to the session or it won't ever be stored
    #     db.session.add(artwork)

    # # Once we're done, we should commit our work
    # db.session.commit()


################################################################################

# if __name__ == "__main__":
#     connect_to_db(app)

#     # In case tables haven't been created, create them
#     db.create_all()

#     # Import different types of data
#     load_artworks()
