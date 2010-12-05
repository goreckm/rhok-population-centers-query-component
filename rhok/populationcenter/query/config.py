SOURCES = {
	#source name is the key
	'geonames': 
		{
			# the name of the source file (could be the source file within the zip to extract)
			'filename': 'allCountries.txt', 
			# the delimiter in the csv			
			'delimiter': '\t', 
			# the column in the csv representing city			
			'cityCol': 1,
			# the column in the csv representing population
			'popCol': 14, 
			# the column in the csv representing latitude
			'latCol': 4, 
			# the column in the csv representing longitude
			'lngCol': 5,
			# the column in the csv representing the country
			'countryCol': 8,
			# the column in the csv representing the region
			#'regionCol': 10,
			# the url from which to download the source file
			'download_source': 'http://download.geonames.org/export/dump/allCountries.zip'},
	'maxmind': 
		{
			'filename': 'worldcitiespop.txt', 
			'delimiter': ',', 
			'cityCol': 1,
			'popCol': 4, 
			'latCol': 5, 
			'lngCol': 6,
			'countryCol': 0,
			'regionCol': 3,
			'download_source': 'http://www.maxmind.com/download/worldcities/worldcitiespop.txt.gz'}
	}

