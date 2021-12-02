from urllib.request import urlopen

def getSource(url):
	response = urlopen(url)  
	html = response.read()
	'''
	builtins.UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 10968: invalid start byte
	'''
	return html.decode()   #  this is were I get the error

 
getSource('http://www.google.com')
