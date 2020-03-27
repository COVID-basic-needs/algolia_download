import os
import csv

from algoliasearch.search_client import SearchClient

client = SearchClient.create(os.environ['ALGOLIA_APP_ID'], os.environ['ALGOLIA_API_KEY'])
index = client.init_index('us_foodbank')
res = index.browse_objects()

csv_path = 'path/to/nkh.csv'
with open(csv_path, 'w') as fp:
	writer = csv.writer(fp)

	header = [
		'siteName', 
		'siteStatus',	
		'siteAddress', 
		'siteState',	
		'siteZip', 
		'contactPhone', 
		'startDate',	
		'endDate', 
		'daysofOperation', 
		'breakfastTime', 
		'lunchTime', 
		'snackTimeAM', 
		'snackTimePM', 
		'dinnerSupperTime'
	]
	writer.write(header)

	for hit in res:
		data = [
			hit['siteName'],
			hit['siteStatus'],
			hit['siteAddress'],
			hit['siteState'],
			hit['siteZip'],
			hit['contactPhone'],
			hit['startDate'],
			hit['endDate'],
			hit['daysofOperation'],
			hit['breakfastTime'],
			hit['lunchTime'],
			hit['snackTimeAM'],
			hit['snackTimePM'],
			hit['dinnerSupperTime'],
		]
		# TODO: format data
	    writer.write(data)
