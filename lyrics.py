import time, urllib2

#gets html code
def gethtml(url):
	try:
		req = urllib2.Request(url)
		return urllib2.urlopen(req).read()
	except Exception, e:
		time.sleep(2)
		return ''

#trimms the html code
def trimmer(url,start,end):
	text = gethtml(url)
	#print(text)
	i = len(text)
	j=0
	
	startLen = len(start)
	endLen = len(end)

	trim=""
	aux = 0
	while(j<=i and aux == 0):
		if(text[j:j+startLen] == start):
			k = j+startLen
			while(text[k:k+endLen] != end):
				k+=1
			trim=text[j+startLen:k]
			print(trim)
			aux = 1
		j+=1
	return trim

song = 'octavarium'

urlSite = trimmer("https://www.google.com.br/#q="+song+"+letra",'html',"</ht")
print(urlSite)
jooj ='/dream-theater/183114/'
lyrics = trimmer('https://www.letras.mus.br/demi-lovato/sorry-not-sorry/','<article>','</article>')

print(lyrics)

code = open("lyrics.html","w")
code.write('<!DOCTYPE html>')
code.write('<html>')
code.write(lyrics)
code.write('</html>')
code.close()