from PopulationCSVAdapter import *
from CSVExporter import *
from FusionExporter import *

class PopulationCentersQuery:
	def __init__(self):
		self.reader = PopulationCSVAdapter('allCountries.txt', 1, 14, 4, 5)
		#self.writer = CSVExporter('export.csv')
		self.writer = FusionExporter('341140')

	def query(self):
		pass
		for row in self.reader:
			if row != None and row['pop'] != '0':
				self.writer.write_line(row)


q = PopulationCentersQuery()
q.query()
