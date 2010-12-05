import urllib
import sys, zipfile, os, os.path, gzip

ZIPPED_FILE = 'temp_download.zip'
GZIP_FILE = 'temp_download.gz'

class CSVDownloader:
	def __init__(self):
		pass

	def download_file(self, source_url, target_file):
		if source_url.endswith('zip'):
			urllib.urlretrieve(source_url, ZIPPED_FILE)
			self.unzip_file(target_file)
			os.remove(ZIPPED_FILE)
		elif source_url.endswith('gz'):
			urllib.urlretrieve(source_url, GZIP_FILE)
			self.ungzip_file(target_file)
			os.remove(GZIP_FILE)
		else:
			urllib.urlretrieve(source_url, target_file)

	def unzip_file(self, target_file):
		zfobj = zipfile.ZipFile(ZIPPED_FILE)
		for name in zfobj.namelist():
			if name.find(target_file) != -1:
				outfile = open(name, 'wb')
				outfile.write(zfobj.read(name))
				outfile.close()		

	def ungzip_file(self, target_file):
		gzipper = gzip.GzipFile(GZIP_FILE)
		outfile = open(target_file, 'wb')
		outfile.write(gzipper.read())
		outfile.close()
		gzipper.close()
