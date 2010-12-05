from PopulationCSVAdapter import *
from CSVExporter import *
from FusionExporter import *
from CSVDownloader import *
from config import *

class PopulationCenters:
	def __init__(self, source, exporter):
		self.exporter = exporter
		self.source = source

	def export(self):
		reader = PopulationCSVAdapter(SOURCES[self.source])

		if self.exporter == 'csv':
			output_file = raw_input("Please enter the output csv filename: ")
			writer = CSVExporter(output_file)			
		else:
			table_name = raw_input("Please enter a table name for Google Fusion Tables: ")
			writer = FusionExporter(table_name)

		for row in reader:
			if row != None and row['pop'] != '0' and row['pop'] != '':
				writer.write_line(row)

	def download_file(self):
		print 'Downloading the file... this may take a while...'
		source = SOURCES[self.source]
		downloader = CSVDownloader()
		downloader.download_file(source['download_source'], source['filename'])

if __name__ == '__main__':
	data_source = raw_input("Please enter data source(geonames or maxmind): ")
	output_format = raw_input("Please enter output format(csv or fusion): ")
	pc = PopulationCenters(data_source, output_format)
	pc.download_file()
	pc.export()

