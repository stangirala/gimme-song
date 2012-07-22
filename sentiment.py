import subprocess
import json
from pprint import pprint
<<<<<<< HEAD
from HTMLParser import HTMLParser

def parseHTML(lyrics):

	
=======

>>>>>>> 4c8988e641dbf4048ae4b6479ad63d2650042ac3

def curlTextProcessing(text):

	curl = "curl -d " + "\"text=" + text + "\"" + " http://text-processing.com/api/sentiment/"

	child = subprocess.Popen(curl, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

	commsout, commserr = child.communicate()

	data = json.loads(commsout)
	#pprint(data)
	#print "NEG: ", data["probability"]["neg"]

	return [data["probability"]["pos"], data["probability"]["neg"], data["probability"]["neutral"]]

<<<<<<< HEAD

if __name__ == '__main__':
	text = "Hey Jude, don't make it bad."

	l = []
	l = curlTextProcessing(text)

	print l
=======
#if __name__ == '__main__':
#	text = "Hey Jude, don't make it bad."

#	l = []
#	l = curlTextProcessing(text)

#	print l
>>>>>>> 4c8988e641dbf4048ae4b6479ad63d2650042ac3
