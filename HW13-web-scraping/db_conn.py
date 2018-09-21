#!/opt/anaconda3/bin/python
# coding: utf-8

# Module used to connect Python with MongoDb
import pymongo
import scrape as knife

conn = 'mongodb://localhost:27017'
mongo = pymongo.MongoClient(conn)

mars_db = mongo.db.mars
mars_data = knife.scrape()

mars_db.update(
	{},
	mars_data,
	upsert=True
)
