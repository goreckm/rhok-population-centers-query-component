import csv

class CSVExporter:
	def __init__(self, filename):
		self.writer = csv.writer(open(filename, 'wb'))

	def write_line(self, row):
		self.writer.writerow([row['city'], row['pop'], row['lat'] + ' ' + row['lng']])
