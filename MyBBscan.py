#!/usr/bin/python
import sys
import os
import httplib
import time


class color:
	green = '\033[92m'
	blue = '\033[94m'
	yellow = '\033[93m'
	red = '\033[91m'
	grey = '\033[90m'
	end = '\033[0m'

files = ['mytabs.php','usersocial.php','myawards.php','myarcade.php','tlink.php','mybbirlastthreadsprofile.php']

mytabs = ["MyTabs", "1.32", "SQL Injection", "https://www.exploit-db.com/exploits/17595/"]
socialnetworks = ["User Social Networks", "1.2", "XSS", "https://www.exploit-db.com/exploits/34539/"]
myawards = ["MyAwards", "2.3", "Cross-Site Request Forgery", "https://www.exploit-db.com/exploits/39290/"]
myarcade = ["My Arcade", "1.3", "Persistant XSS", "https://www.exploit-db.com/exploits/44186/"]
tlink = ["Threads to Link", "1.3", "Persistant XSS", " "]
lastthreadsprofile = ["Last User's Threads in Profile", "1.2", "Persistant XSS", "https://www.exploit-db.com/exploits/44339/"]

def banner():
	print color.green+"MyBBscan\n"+color.end+"By: "+color.blue+"0xB9 "+color.end+"from "+color.blue+"https://LuxorForums.com\n"+color.end
banner()
time.sleep(2)

print "-"*60
print color.green+"Example:"+color.end+" MyBBforum.com or subdomain.MyBBforum.com"
print "-"*60

site = raw_input(color.green+"Enter MyBB forum URL-> "+color.end)

print (color.green+"[*] Scanning "+color.end+"{}...\n").format(site)
print "-"*60

def connection_status(site, plugin_file):
    connection = httplib.HTTPSConnection(site)
    connection.request("HEAD", plugin_file)
    return connection.getresponse().status


def scan(site, upload):
	status = connection_status(site, "/inc/plugins/"+upload)
	if status == 200:
		if upload == "mytabs.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+mytabs[0]
			print "Version: "+mytabs[1]
			print "Vulnerability Type: "+mytabs[2]
			print "Information: "+mytabs[3]
			print "-"*60
		elif upload == "usersocial.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+socialnetworks[0]
			print "Version: "+socialnetworks[1]
			print "Vulnerability Type: "+socialnetworks[2]
			print "Information: "+socialnetworks[3]
			print "-"*60
		elif upload == "myawards.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+myawards[0]
			print "Version: "+myawards[1]
			print "Vulnerability Type: "+myawards[2]
			print "Information: "+myawards[3]
			print "-"*60
		elif upload == "myarcade.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+myarcade[0]
			print "Version: "+myarcade[1]
			print "Vulnerability Type: "+myarcade[2]
			print "Information: "+myarcade[3]
			print "-"*60
		elif upload == "tlink.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+tlink[0]
			print "Version: "+tlink[1]
			print "Vulnerability Type: "+tlink[2]
			print "Information: "+tlink[3]
			print "-"*60
		elif upload == "mybbirlastthreadsprofile.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+lastthreadsprofile[0]
			print "Version: "+lastthreadsprofile[1]
			print "Vulnerability Type: "+lastthreadsprofile[2]
			print "Information: "+lastthreadsprofile[3]
			print "-"*60
		else:
			pass
	else:
		pass

for upload in files:
	scan(site, upload)

print color.green+"\nScan complete! \n"+color.end
exit()
