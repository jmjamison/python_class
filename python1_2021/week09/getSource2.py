#!/usr/bin/python3 -tt

#   vim::expandtab:shiftwidth=4:softtabstop=4:smarttab:

from urllib.request import urlopen

def getSource(url):
    response = urlopen(url)  
    html = response.read()
    '''
	builtins.UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 10968: invalid start byte
    '''

    print("html object:", type(html), html)

#   print("html data:", type(data), data)

    return html.decode(errors='ignore')   


def main():
 
    getSource('http://www.google.com')

if __name__ == "__main__":
    main()

