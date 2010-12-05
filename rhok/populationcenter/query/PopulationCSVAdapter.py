import csv


class PopulationCSVAdapter:


	def __init__(self, filename, cityColumn, populationColumn, latColumn, lngColumn):
		csv.field_size_limit(1000000000)
		self.reader = csv.reader(open(filename, 'rb'), delimiter='\t')
		
		self.cityColumn = cityColumn
		self.populationColumn = populationColumn
		self.latColumn = latColumn
		self.lngColumn = lngColumn

	def __iter__(self):
		return self
		
	def next(self):
		current_row = self.reader.next()
		result = {'city': current_row[self.cityColumn], 'pop': current_row[self.populationColumn],
				'lat': current_row[self.latColumn],'lng': current_row[self.lngColumn]}
		return result




