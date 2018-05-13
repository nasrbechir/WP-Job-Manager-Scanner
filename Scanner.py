#############################
#            ABOUT          #
#############################
# Bechir & Golden : 
#https://www.facebook.com/nasr.bechir
#https://www.facebook.com/Mrm0hm3d
#Greetz To : Darkshadow Anonjocker Iheb Pal

#Lib
import urllib2
import sys
import re

#Var
wp_sites = []
file = ""

 

def scan(url):
	try:
		print "[+] Scanning   : "+str(url)
		tester = urllib2.urlopen(str(url)+"/post-a-job/").read()
		if('<form action="/post-a-job/" method="post" id="submit-job-form" class="job-manager-form" enctype="multipart/form-data">' in tester):
			print "  Vuln => : "+str(url)+"/post-a-job/"
			with open("vuln.txt", "a") as f:
				f.write(url+"\n")
	except:
		pass

#Main
try:
	file = open(sys.argv[1]).readlines()
except :
	print "Usage : "+str(sys.argv[0])+" list.txt"
	sys.exit(1)
print "[+]-------------------------------------------[+]\r\n"
		
print "[+]                Bechir & Golden            [+]\r\n"
print "[+]-------------------------------------------[+]\r\n"
if(len(file) > 0):
	
	
	for s in file:
		s = s.rstrip()
		scan(s)
	
	
		
print "Check Vuln.txt !"
