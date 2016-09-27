#import socket

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('www.google.co.in', 80))
#mysock.send('GET http://www.google.co.in HTTP/1.0\n\n')

#while True:
#	data = mysock.recv(512)
#	if ( len(data) < 1 ):
#		break
#	print data
	
#mysock.close()

########################################

#import urllib
#fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')

#for line in fhand:
#	print line.strip()

########################################

import requests
url = 'http://www.mfgx.net/sv/mfgx/login.jsp'
values = {'j_username': 'pkumari-kob',
			'j_password': 'pkumari-kob'}
			
r = requests.post(url, data=values)
print r.content