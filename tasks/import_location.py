from settings import variables
from config.literal import locations
from database.database import Database

def import_location():
    feed_database = Database(variables.COLLECTION_LOCATION)

    for location in locations:
        location_exist = feed_database.get_collection().find_one({'city': location})
        if not(location_exist):
            feed_database.insert_one_data({'city': location})

    return