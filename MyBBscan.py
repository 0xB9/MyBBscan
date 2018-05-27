#!/usr/bin/python
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
		'recentthread.php','mc_craft.php','lpop.php','adminnotes.php','modnoteslog.php']

myTabs = ["MyTabs", "1.32", "SQL Injection", "https://www.exploit-db.com/exploits/17595/"]
socialNetworks = ["User Social Networks", "1.2", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/34539/"]
myAwards = ["MyAwards", "2.3", "CSRF", "https://www.exploit-db.com/exploits/39290/"]
myArcade = ["My Arcade", "1.3", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44186/"]
threadToLink = ["Threads to Link", "1.3", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44547/"]
lastThreadsProfile = ["Last User's Threads in Profile", "1.2", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44339/"]
downloads = ["Downloads", "2.0.3", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44400/"]
recentThreadIndex = ["Recent Threads On Index", "17.0", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44420/"]
minecraftMyCode = ["Minecraft Crafting MyCode", "1.2", "Cross-Site Scripting", "[item=10;item da craftare]\')\"onclick=\"alert(\'test\');\" [/item]"]
latestPostProfile = ["Latest Post on Profile", "1.1", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44608/"]
adminNotes = ["Admin Notes", "1.1", "CSRF", "https://www.exploit-db.com/exploits/44624/"]
modNotes = ["Moderator Log Notes", "1.1", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44754/"]

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
			print "Vulnerable Plugin: "+myTabs[0]
			print "Version: "+myTabs[1]
			print "Vulnerability Type: "+myTabs[2]
			print "Information: "+myTabs[3]
			print "-"*60
		elif upload == "usersocial.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+socialNetworks[0]
			print "Version: "+socialNetworks[1]
			print "Vulnerability Type: "+socialNetworks[2]
			print "Information: "+socialNetworks[3]
			print "-"*60
		elif upload == "myawards.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+myAwards[0]
			print "Version: "+myAwards[1]
			print "Vulnerability Type: "+myAwards[2]
			print "Information: "+myAwards[3]
			print "-"*60
		elif upload == "myarcade.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+myArcade[0]
			print "Version: "+myArcade[1]
			print "Vulnerability Type: "+myArcade[2]
			print "Information: "+myArcade[3]
			print "-"*60
		elif upload == "tlink.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+threadToLink[0]
			print "Version: "+threadToLink[1]
			print "Vulnerability Type: "+threadToLink[2]
			print "Information: "+threadToLink[3]
			print "-"*60
		elif upload == "mybbirlastthreadsprofile.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+lastThreadsProfile[0]
			print "Version: "+lastThreadsProfile[1]
			print "Vulnerability Type: "+lastThreadsProfile[2]
			print "Information: "+lastThreadsProfile[3]
			print "-"*60
		elif upload == "downloads.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+downloads[0]
			print "Version: "+downloads[1]
			print "Vulnerability Type: "+downloads[2]
			print "Information: "+downloads[3]
			print "-"*60
		elif upload == "recentthread.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+recentThreadIndex[0]
			print "Version: "+recentThreadIndex[1]
			print "Vulnerability Type: "+recentThreadIndex[2]
			print "Information: "+recentThreadIndex[3]
			print "-"*60
		elif upload == "mc_craft.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+minecraftMyCode[0]
			print "Version: "+minecraftMyCode[1]
			print "Vulnerability Type: "+minecraftMyCode[2]
			print "Information: "+minecraftMyCode[3]
			print "-"*60
		elif upload == "lpop.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+latestPostProfile[0]
			print "Version: "+latestPostProfile[1]
			print "Vulnerability Type: "+latestPostProfile[2]
			print "Information: "+latestPostProfile[3]
			print "-"*60
		elif upload == "adminnotes.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+adminNotes[0]
			print "Version: "+adminNotes[1]
			print "Vulnerability Type: "+adminNotes[2]
			print "Information: "+adminNotes[3]
			print "-"*60
		elif upload == "modnoteslog.php":
			print color.yellow+"[*] Possible Vulnerable Plugin!"+color.end
			print "Vulnerable Plugin: "+modNotes[0]
			print "Version: "+modNotes[1]
			print "Vulnerability Type: "+modNotes[2]
			print "Information: "+modNotes[3]
			print "-"*60
		else:
			pass
	else:
		pass

for upload in files:
	scan(site, upload)

print color.green+"\nScan complete! \n"+color.end
exit()
