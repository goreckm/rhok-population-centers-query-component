import csv


class PopulationCSVAdapter:


	def __init__(self, opts):
		csv.field_size_limit(1000000000)
		self.reader = csv.reader(open(opts['filename'], 'rb'), delimiter=opts['delimiter'])
		
		self.cityColumn = opts['cityCol']
		self.populationColumn = opts['popCol']
		self.latColumn = opts['latCol']
		self.lngColumn = opts['lngCol']
		self.countryColumn = opts['countryCol']
		if 'regionCol' in opts:
			self.regionColumn = opts['regionCol']
		else:
			self.regionColumn = None

	def __iter__(self):
		return self
		
	def next(self):
		current_row = self.reader.next()
		result = {'city': current_row[self.cityColumn], 'pop': current_row[self.populationColumn],
				'lat': current_row[self.latColumn],'lng': current_row[self.lngColumn],
				'country': current_row[self.countryColumn]}
		if self.regionColumn != None:
			result['region'] = current_row[self.regionColumn]
		return result




