import ftclient
import urllib2

class FusionExporter:
	def __init__(self, table_id):
		auth_token = ftclient.GetAuthToken()
		self.ft = ftclient.FTClient(auth_token)
		
		self.max_per_batch = 500
		self.col_keys = ['City', 'Population', 'Location']
		self.col_keys = ','.join(["'%s'" % s for s in self.col_keys])
		self.table_id = table_id
		self.clear_batch()

	def write_line(self, row):
		row = [row['city'], row['pop'], row['lat'] + ' ' + row['lng']]
		row = [r.replace("'", "''") for r in row]
		fixed_line = ','.join(["'%s'" % s for s in row])
		query = 'INSERT INTO %s (%s) VALUES (%s)' % (
			self.table_id, self.col_keys, fixed_line)
		self.queries.append(query)
		self.num_in_batch += 1
		if self.num_in_batch >= self.max_per_batch:
			self.write_batch()
            

	def clear_batch(self):
		self.queries = []
		self.num_in_batch = 0
		

	def write_batch(self):
		try:
			full_query = ';'.join(self.queries)
			self.ft.runPostQuery(full_query)
		except urllib2.HTTPError:
			# Had an error with all the INSERTS; do them one at a time
			print 'Exception hit, subdividing:'
			for query in self.queries:
				try:
					self.ft.runPostQuery(query)
				except urllib2.HTTPError, e2:
					print 'Error at query %s:' % query
					print e2
		self.clear_batch()
		#exit after first batch upload
		exit()

	def close(self):
		self.write_batch()

