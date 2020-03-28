import os
import csv
import sys

from algoliasearch.search_client import SearchClient

def dump_to_csv(csv_path):
    client = SearchClient.create('JWHPBFC4T1', '0d4e43a67ee4dd5d1ea7a667aded6c7e')
    index = client.init_index('us_foodbank')
    res = index.browse_objects()

    with open(csv_path, 'w') as fp:
        writer = csv.writer(fp)

        header = ['siteName', 'siteStatus', 'siteAddress', 'siteState', 'siteZip', 'contactPhone', 'startDate',
                  'endDate', 'daysofOperation', 'breakfastTime', 'lunchTime', 'snackTimeAM', 'snackTimePM',
                  'dinnerSupperTime']
        writer.writerow(header)

        for hit in res:
            data = []
            for col in header:
                data.append(hit[col])

            writer.writerow(data)


if __name__ == '__main__':
	if len(sys.argv) == 2:
		csv_path = sys.argv[1]
	else:
		csv_path = '/path/to/nkh.csv'

	dump_to_csv(csv_path)
