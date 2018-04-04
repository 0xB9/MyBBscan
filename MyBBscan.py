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

files = ['mytabs.php','usersocial.php','myawards.php','myarcade.php','tlink.php','mybbirlastthreadsprofile.php','downloads.php',
		'mc_craft.php']

mytabs = ["MyTabs", "1.32", "SQL Injection", "https://www.exploit-db.com/exploits/17595/"]
socialnetworks = ["User Social Networks", "1.2", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/34539/"]
myawards = ["MyAwards", "2.3", "CSRF", "https://www.exploit-db.com/exploits/39290/"]
myarcade = ["My Arcade", "1.3", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44186/"]
tlink = ["Threads to Link", "1.3", "Cross-Site Scripting", "Awaiting..."]
lastthreadprofile = ["Last User's Threads in Profile", "1.2", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44339/"]
downloads = ["Downloads", "2.0.3", "Cross-Site Scripting", "Awaiting..."]
mc_mycode = ["Minecraft Crafting MyCode", "1.2", "Cross-Site Scripting", "[item=10;item da craftare]\')\"onclick=\"alert(\'test\');\" [/item]"]

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
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+mytabs[0]
			print "Version: "+mytabs[1]
			print "Vulnerability Type: "+mytabs[2]
			print "Information: "+mytabs[3]
			print "-"*60
		elif upload == "usersocial.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+socialnetworks[0]
			print "Version: "+socialnetworks[1]
			print "Vulnerability Type: "+socialnetworks[2]
			print "Information: "+socialnetworks[3]
			print "-"*60
		elif upload == "myawards.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+myawards[0]
			print "Version: "+myawards[1]
			print "Vulnerability Type: "+myawards[2]
			print "Information: "+myawards[3]
			print "-"*60
		elif upload == "myarcade.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+myarcade[0]
			print "Version: "+myarcade[1]
			print "Vulnerability Type: "+myarcade[2]
			print "Information: "+myarcade[3]
			print "-"*60
		elif upload == "tlink.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+tlink[0]
			print "Version: "+tlink[1]
			print "Vulnerability Type: "+tlink[2]
			print "Information: "+tlink[3]
			print "-"*60
		elif upload == "mybbirlastthreadsprofile.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+lastthreadsprofile[0]
			print "Version: "+lastthreadsprofile[1]
			print "Vulnerability Type: "+lastthreadsprofile[2]
			print "Information: "+lastthreadsprofile[3]
			print "-"*60
		elif upload == "downloads.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+downloads[0]
			print "Version: "+downloads[1]
			print "Vulnerability Type: "+downloads[2]
			print "Information: "+downloads[3]
			print "-"*60
		elif upload == "mc_craft.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+mc_mycode[0]
			print "Version: "+mc_mycode[1]
			print "Vulnerability Type: "+mc_mycode[2]
			print "Information: "+mc_mycode[3]
			print "-"*60
		else:
			pass
	else:
		pass

for upload in files:
	scan(site, upload)

print color.green+"\nScan complete! \n"+color.end
exit()
