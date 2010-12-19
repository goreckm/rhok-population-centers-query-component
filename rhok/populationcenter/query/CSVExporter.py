import csv

class CSVExporter:
	def __init__(self, filename):
		self.writer = csv.writer(open(filename, 'wb'))

	def write_line(self, row):
		if 'region' in row:
			region = row['region']
		else:
			region = ''

		self.writer.writerow([row['city'], row['pop'], row['lat'], row['lng'], row['country'], region])

	def close(self):
		pass
