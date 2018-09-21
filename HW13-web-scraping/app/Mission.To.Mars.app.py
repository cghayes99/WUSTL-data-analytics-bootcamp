#!/opt/anaconda3/bin/python
# coding: utf-8

'''
###################################################################################
# @script   Mission To Mars    mission.to.mars.app.py                             #
# @version  1.0.0                                                                 #
#---------------------------------------------------------------------------------#
# FLASK API                                                                       #
#                                                                                 #
# Modification History                                                            #
#                                                                                 #
# Date        Name             Description                                        #
# ----------  -----------      ----------------------------------                 #
# 2018/09/18  (chris)          Original script                                    #
#                                                                                 #
###################################################################################
'''

## Imports
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape as knife

## FLASH init
app = Flask(__name__)

## Mongo init
conn = 'mongodb://localhost:27017'
mongo = pymongo.MongoClient(conn)

'''
	/
'''
@app.route("/")
def get_docroot():
	mars_db = mongo.db.mars.find_one()
	return render_template("index.html", mars=mars_db)

'''
	/scrape
'''
@app.route("/scrape")
def get_scrape():
	mars_data = knife.scrape()

	mars_db = mongo.db.mars
	mars_db.update(
		{},
		mars_data,
		upsert=True
	)	

	return redirect("http://localhost:5000/", code=302)

## Main functionality
if __name__ == '__main__':
	app.run(debug=True)