from pymongo import MongoClient
import logging
import os
import datetime
import json
import random

def get_collection(collection_name='twitter_numbers'):
	client = MongoClient(os.environ['MONGODB_URI'])

	# Get default DB (the free plan provides only one at the moment)
	db = client.get_default_database()

	# Get your collection
	return db[collection_name]


def store_entry(freqs):
	collection = get_collection()
	entry = {
				"_id":datetime.datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-%f-')+str(random.randint(1e6,9e6)),
				"frequency":json.dumps(freqs)
			}
	entry_id = collection.insert_one(entry).inserted_id
	logging.info('Successfully inserted entry with id ' + str(entry_id))
