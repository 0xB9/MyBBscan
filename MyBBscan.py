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

files = ['kingchat.php','profilewfc.php','awaylist.php','hmflags.php','profileskype.php','socialsites.php',
'dymy_ua.php','profilefacebook.php','AJAXChat.php','youtube.php','tipsoftheday.php','profileblogs.php',
'bank.php','SuscribeUsers.php','profilealbums.php','mystatus.php','userbarplugin.php','afsignatures.php','mytabs.php']

AJAXChat = ["MyBB AJAX Chat", "XSS", "https://www.exploit-db.com/exploits/23354/"]
kingchat = ["MyBB Kingchat", "XSS & SQL Injection", "https://www.exploit-db.com/exploits/23249/ \nhttp://www.exploit-db.com/exploits/23105/"]
profilewfc = ["MyBB Profile Wii Friend","SQL UPDATE Injection & XSS", "https://www.exploit-db.com/exploits/23888/"]
awaylist  = ["MyBB AwayList", "SQL Injection", "https://www.exploit-db.com/exploits/23625/"]
hmflags = ["MyBB HM My Country Flags", "SQL Injection", "https://www.exploit-db.com/exploits/23624/"]
profileskype = ["MyBB Profile Skype ID", "SQL Injection & XSS", "https://www.exploit-db.com/exploits/23425/"]
socialsites = ["MyBB Social Sites", "XSS", "https://www.exploit-db.com/exploits/23382/"]
dymy_ua = ["MyBB DyMy User Agent", "SQL Injection", "https://www.exploit-db.com/exploits/23359/"]
profilefacebook = ["MyBB Facebook Profile", "XSS", "https://www.exploit-db.com/exploits/23355/"]
youtube = ["MyBB MyYoutube", "Post SQL Injection", "https://www.exploit-db.com/exploits/23353/"]
tipsoftheday = ["MyBB TipsOfTheDay", "Stored XSS & SQL Injection", "https://www.exploit-db.com/exploits/23322/"]
profileblogs = ["MyBB Profile Blogs","SQL Injection & Stored XSS", "https://www.exploit-db.com/exploits/23287/"]
bank = ["MyBB Bank-v3", "Post SQL Injection", "https://www.exploit-db.com/exploits/23284/"]
SuscribeUsers = ["MyBB Follower User", "SQL Injection", "https://www.exploit-db.com/exploits/22405/"]
profilealbums = ["MyBB Profile Albums", "SQL Injection", "https://www.exploit-db.com/exploits/22003/"]
mystatus = ["MyBB MyStatus", "SQL Injection", "https://www.exploit-db.com/exploits/17972/"]
userbar = ["MyBB Forum Userbar", "SQL Injection", "https://www.exploit-db.com/exploits/17962/"]
afsignatures = ["MyBB Advanced Forum Signatures", "SQL Injection", "https://www.exploit-db.com/exploits/17961/"]
mytabs = ["MyBB MyTabs", "SQL Injection", "https://www.exploit-db.com/exploits/17595/"]

def banner():
	print color.green+"MyBBscan\n"+color.end+"By: "+color.blue+"root "+color.end+"from "+color.blue+"https://HackRally.net\n"+color.end
banner()
time.sleep(2)

print "-"*60
print color.green+"Example:"+color.end+" MyBBwebsite.com"
print "-"*60

site = raw_input(color.green+"Enter MyBB forum URL-> "+color.end)

print (color.green+"[*] Scanning "+color.end+"{}...\n").format(site)
print "-"*60

def connection_status(site, plugin_file):
    connection = httplib.HTTPConnection(site)
    connection.request("HEAD", plugin_file)
    return connection.getresponse().status


def scan(site, upload):
	status = connection_status(site, "/inc/plugins/"+upload)
	if status == 200:
		if upload == "AJAXChat.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+AJAXChat[0]+" Version: 1.0" # checked
			print "Vulnerability Type: "+AJAXChat[1]
			print "Information: "+AJAXChat[2]
			print "-"*60
		elif upload == "kingchat.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+kingchat[0]+" Version: 1.0"
			print "Vulnerability Type: "+kingchat[1]
			print "Information: "+kingchat[2]
			print "-"*60
		elif upload == "profilewfc.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+profilewfc[0]+" Version: 1.0"
			print "Vulnerability Type: "+profilewfc[1]
			print "Information: "+profilewfc[2]
			print "-"*60
		elif upload == "awaylist.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+awaylist[0]+" Version: Unknown"
			print "Vulnerability Type: "+awaylist[1]
			print "Information: "+awaylist[2]
			print "-"*60
		elif upload == "hmflags.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+hmflags[0]+" Version: Unknown"
			print "Vulnerability Type: "+hmflags[1]
			print "Information: "+hmflags[2]
			print "-"*60
		elif upload == "profileskype.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+profileskype[0]+" Version: 1.0"
			print "Vulnerability Type: "+profileskype[1]
			print "Information: "+profileskype[2]
			print "-"*60
		elif upload == "socialsites.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+socialsites[0]+" Version: 0.2.2"
			print "Vulnerability Type: "+socialsites[1]
			print "Information: "+socialsites[2]
			print "-"*60
		elif upload == "dymy_ua.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+dymy_ua[0]+" Version: 1.0"
			print "Vulnerability Type: "+dymy_ua[1]
			print "Information: "+dymy_ua[2]
			print "-"*60
		elif upload == "profilefacebook.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+profilefacebook[0]+" Version: 2.4"
			print "Vulnerability Type: "+profilefacebook[1]
			print "Information: "+profilefacebook[2]
			print "-"*60
		elif upload == "youtube.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+youtube[0]+" Version: 1.0"
			print "Vulnerability Type: "+youtube[1]
			print "Information: "+youtube[2]
			print "-"*60
		elif upload == "tipsoftheday.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+tipsoftheday[0]+" Version: 1.0"
			print "Vulnerability Type: "+tipsoftheday[1]
			print "Information: "+tipsoftheday[2]
			print "-"*60
		elif upload == "profileblogs.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+profileblogs[0]+" Version: 1.2"
			print "Vulnerability Type: "+profileblogs[1]
			print "Information: "+profileblogs[2]
			print "-"*60
		elif upload == "bank.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+bank[0]+" Version: 3.0"
			print "Vulnerability Type: "+bank[1]
			print "Information: "+bank[2]
			print "-"*60
		elif upload == "SuscribeUsers.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+SuscribeUsers[0]+" Version: 1.5"
			print "Vulnerability Type: "+SuscribeUsers[1]
			print "Information: "+SuscribeUsers[2]
			print "-"*60
		elif upload == "profilealbums.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+profilealbums[0]+" Version: 0.9"
			print "Vulnerability Type: "+profilealbums[1]
			print "Information: "+profilealbums[2]
			print "-"*60
		elif upload == "mystatus.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+mystatus[0]+" Version: 3.1"
			print "Vulnerability Type: "+mystatus[1]
			print "Information: "+mystatus[2]
			print "-"*60
		elif upload == "userbarplugin.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+userbar[0]+" Version: 2.2"
			print "Vulnerability Type: "+userbar[1]
			print "Information: "+userbar[2]
			print "-"*60
		elif upload == "afsignatures.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+afsignatures[0]+" Version: 2.0.4"
			print "Vulnerability Type: "+afsignatures[1]
			print "Information: "+afsignatures[2]
			print "-"*60
		elif upload == "mytabs.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+mytabs[0]+" Version: 1.32"
			print "Vulnerability Type: "+mytabs[1]
			print "Information: "+mytabs[2]
			print "-"*60
		else:
			pass
	else:
		pass

for upload in files:
	scan(site, upload)

print color.green+"\nScan complete! "+color.end
print "Press ENTER to exit"
raw_input()
