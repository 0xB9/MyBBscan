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
'bank.php','SuscribeUsers.php','profilealbums.php','mystatus.php','userbarplugin.php','afsignatures.php','mytabs.php','usersocial.php','myawards.php']

AJAXChat = ["MyBB AJAX Chat", "1.0", "XSS", "https://www.exploit-db.com/exploits/23354/"]
kingchat = ["MyBB Kingchat", "1.0", "XSS & SQL Injection", "https://www.exploit-db.com/exploits/23249/ \nhttps://www.exploit-db.com/exploits/23105/"]
profilewfc = ["MyBB Profile Wii Friend", "1.0", "SQL UPDATE Injection & XSS", "https://www.exploit-db.com/exploits/23888/"]
awaylist  = ["MyBB AwayList", "1.6.7", "SQL Injection", "https://www.exploit-db.com/exploits/23625/"]
hmflags = ["MyBB HM My Country Flags", "Unknown", "SQL Injection", "https://www.exploit-db.com/exploits/23624/"]
profileskype = ["MyBB Profile Skype ID", "1.0", "SQL Injection & XSS", "https://www.exploit-db.com/exploits/23425/"]
socialsites = ["MyBB Social Sites", "0.2.2", "XSS", "https://www.exploit-db.com/exploits/23382/"]
dymy_ua = ["MyBB DyMy User Agent", "1.0", "SQL Injection", "https://www.exploit-db.com/exploits/23359/"]
profilefacebook = ["MyBB Facebook Profile", "2.4", "XSS", "https://www.exploit-db.com/exploits/23355/"]
youtube = ["MyBB MyYoutube", "1.0", "Post SQL Injection", "https://www.exploit-db.com/exploits/23353/"]
tipsoftheday = ["MyBB TipsOfTheDay", "1.0", "Stored XSS & SQL Injection", "https://www.exploit-db.com/exploits/23322/"]
profileblogs = ["MyBB Profile Blogs", "1.2", "SQL Injection & Stored XSS", "https://www.exploit-db.com/exploits/23287/"]
bank = ["MyBB Bank", "3.0", "Post SQL Injection", "https://www.exploit-db.com/exploits/23284/"]
SuscribeUsers = ["MyBB Follower User", "1.5", "SQL Injection", "https://www.exploit-db.com/exploits/22405/"]
profilealbums = ["MyBB Profile Albums", "0.9", "SQL Injection", "https://www.exploit-db.com/exploits/22003/"]
mystatus = ["MyBB MyStatus", "3.1", "SQL Injection", "https://www.exploit-db.com/exploits/17972/"]
userbar = ["MyBB Forum Userbar", "2.2", "SQL Injection", "https://www.exploit-db.com/exploits/17962/"]
afsignatures = ["MyBB Advanced Forum Signatures", "2.0.4", "SQL Injection", "https://www.exploit-db.com/exploits/17961/"]
mytabs = ["MyBB MyTabs", "1.32", "SQL Injection", "https://www.exploit-db.com/exploits/17595/"]
socialnetworks = ["MyBB User Social Networks", "1.2", "XSS", "https://www.exploit-db.com/exploits/34539/"]
myawards = ["MyBB MyAwards", "2.3", "Cross-Site Request Forgery", "https://www.exploit-db.com/exploits/39290/"]

def banner():
	print color.green+"MyBBscan\n"+color.end+"By: "+color.blue+"root "+color.end+"from "+color.blue+"https://LuxorForums.com\n"+color.end
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
		if upload == "AJAXChat.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+AJAXChat[0]
			print "Version: "+AJAXChat[1]
			print "Vulnerability Type: "+AJAXChat[2]
			print "Information: "+AJAXChat[3]
			print "-"*60
		elif upload == "kingchat.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+kingchat[0]
			print "Version: "+kingchat[1]
			print "Vulnerability Type: "+kingchat[2]
			print "Information: "+kingchat[3]
			print "-"*60
		elif upload == "profilewfc.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+profilewfc[0]
			print "Version: "+profilewfc[1]
			print "Vulnerability Type: "+profilewfc[2]
			print "Information: "+profilewfc[3]
			print "-"*60
		elif upload == "awaylist.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+awaylist[0]
			print "Version: "+awaylist[1]
			print "Vulnerability Type: "+awaylist[2]
			print "Information: "+awaylist[3]
			print "-"*60
		elif upload == "hmflags.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+hmflags[0]
			print "Version: "+hmflags[1]
			print "Vulnerability Type: "+hmflags[2]
			print "Information: "+hmflags[3]
			print "-"*60
		elif upload == "profileskype.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+profileskype[0]
			print "Version: "+profileskype[1]
			print "Vulnerability Type: "+profileskype[2]
			print "Information: "+profileskype[3]
			print "-"*60
		elif upload == "socialsites.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+socialsites[0]
			print "Version: "+socialsites[1]
			print "Vulnerability Type: "+socialsites[2]
			print "Information: "+socialsites[3]
			print "-"*60
		elif upload == "dymy_ua.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+dymy_ua[0]
			print "Version: "+dymy_ua[1]
			print "Vulnerability Type: "+dymy_ua[2]
			print "Information: "+dymy_ua[3]
			print "-"*60
		elif upload == "profilefacebook.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+profilefacebook[0]
			print "Version: "+profilefacebook[1]
			print "Vulnerability Type: "+profilefacebook[2]
			print "Information: "+profilefacebook[3]
			print "-"*60
		elif upload == "youtube.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+youtube[0]
			print "Version: "+youtube[1]
			print "Vulnerability Type: "+youtube[2]
			print "Information: "+youtube[3]
			print "-"*60
		elif upload == "tipsoftheday.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+tipsoftheday[0]
			print "Version: "+tipsoftheday[1]
			print "Vulnerability Type: "+tipsoftheday[2]
			print "Information: "+tipsoftheday[3]
			print "-"*60
		elif upload == "profileblogs.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+profileblogs[0]
			print "Version: "+profileblogs[1]
			print "Vulnerability Type: "+profileblogs[2]
			print "Information: "+profileblogs[3]
			print "-"*60
		elif upload == "bank.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+bank[0]
			print "Version: "+bank[1]
			print "Vulnerability Type: "+bank[2]
			print "Information: "+bank[3]
			print "-"*60
		elif upload == "SuscribeUsers.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+SuscribeUsers[0]
			print "Version: "+SuscribeUsers[1]
			print "Vulnerability Type: "+SuscribeUsers[2]
			print "Information: "+SuscribeUsers[3]
			print "-"*60
		elif upload == "profilealbums.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+profilealbums[0]
			print "Version: "+profilealbums[1]
			print "Vulnerability Type: "+profilealbums[2]
			print "Information: "+profilealbums[3]
			print "-"*60
		elif upload == "mystatus.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+mystatus[0]
			print "Version: "+mystatus[1]
			print "Vulnerability Type: "+mystatus[2]
			print "Information: "+mystatus[3]
			print "-"*60
		elif upload == "userbarplugin.php":
			print color.yellow+"[*] Possible Vulnerable Plugin! \n"+color.end+"Vulnerable Plugin: "+userbar[0]
			print "Version: "+userbar[1]
			print "Vulnerability Type: "+userbar[2]
			print "Information: "+userbar[3]
			print "-"*60
		elif upload == "afsignatures.php":
			print color.red+"[*] Warning! \n"+color.end+"Vulnerable Plugin: "+afsignatures[0]
			print "Version: "+afsignatures[1]
			print "Vulnerability Type: "+afsignatures[2]
			print "Information: "+afsignatures[3]
			print "-"*60
		elif upload == "mytabs.php":
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
		else:
			pass
	else:
		pass

for upload in files:
	scan(site, upload)

print color.green+"\nScan complete! \n"+color.end
exit()
