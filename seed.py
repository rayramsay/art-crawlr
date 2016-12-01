import os
import json
import googlemaps

from model import Artwork
# from server import app

############# GLOBALS ##############
# Remember to ``source secrets.sh``!
GMAPS = googlemaps.Client(key=os.environ['GOOGLE_API_SERVER_KEY'])
####################################


def get_zipcode(lat, lng):
    """Given lat and lng, returns zipcode."""

    latlng = str(lat) + ',' + str(lng)
    result = GMAPS.reverse_geocode(latlng)
    zipcode = result[0]['address_components'][7]['long_name']
    return zipcode


def load_artworks(start, stop):
    """Load artworks from seed data into database."""

    print "Loading Artworks"

    art_seed = open("seed_data/SF_Civic_Art_Collection.json")
    json_dict = json.load(art_seed)
    art_list = json_dict['data']

    for item in art_list[start:stop]:
        artist = item[11]
        credit_line = item[13]
        latlongdict = json.loads(item[15])
        lng = latlongdict['coordinates'][0]
        lat = latlongdict['coordinates'][1]
        location_description = item[16]
        medium = item[17]
        title = item[19]
        zipcode = get_zipcode(lat, lng)

        print zipcode

        artwork = Artwork(artist=artist,
                        credit_line=credit_line,
                        lat=lat,
                        lng=lng,
                        location_description=location_description,
                        medium=medium,
                        title=title,
                        # address=address,
                        zipcode=zipcode)

    #     # We need to add to the session or it won't ever be stored
        db.session.add(artwork)

    # # Once we're done, we should commit our work
    db.session.commit()


################################################################################

#if __name__ == "__main__":
    #connect_to_db(app)

    # In case tables haven't been created, create them
    # db.create_all()

    # Import different types of data
    # load_artworks()
