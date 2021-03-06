#!/usr/bin/python
from huepy import * 	#pip install huepy
import http.client
import time


files = ['mytabs.php','usersocial.php','myawards.php','myarcade.php','tlink.php','mybbirlastthreadsprofile.php','downloads.php',
		'recentthread.php','lpop.php','adminnotes.php','modnoteslog.php','changstats.php','recent_threads.php','newthreads.php',
		'thankyoulike.php','ougc_awards.php','ip_history_logs.php','trashbin.php','timeline_cp.php','threadredirect.php',
		'trends.php','deleteaccount.php','ougc_feedback.php']

myTabs = ["MyTabs", "1.32", "SQL Injection", "https://www.exploit-db.com/exploits/17595/"]
socialNetworks = ["User Social Networks", "1.2", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/34539/"]
myAwards = ["MyAwards", "2.3", "CSRF", "https://www.exploit-db.com/exploits/39290/"]
myArcade = ["My Arcade", "1.3", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44186/"]
threadToLink = ["Threads to Link", "1.3", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44547/"]
lastThreadsProfile = ["Last User's Threads in Profile", "1.2", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44339/"]
downloads = ["Downloads", "2.0.3", "Cross-Site Scripting", "SQLi", "https://www.exploit-db.com/exploits/44400/", "https://www.exploit-db.com/exploits/45747/"]
recentThreadIndex = ["Recent Threads On Index", "17.0", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44420/"]
latestPostProfile = ["Latest Post on Profile", "1.1", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44608/"]
adminNotes = ["Admin Notes", "1.1", "Cross-Site Request Forgery", "https://www.exploit-db.com/exploits/44624/"]
modNotes = ["Moderator Log Notes", "1.1", "Cross-Site Scripting & CSRF", "https://www.exploit-db.com/exploits/44754/", "https://www.exploit-db.com/exploits/45224/"]
advancedStats = ["ChangUonDyU - Advanced Statistics", "1.0.2", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44795/"]
recentThreads = ["Recent Threads", "1.0", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/44833/"]
newThreads = ["New Threads", "1.1", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/45057/"]
thankyouLike = ["Thank You/Like", "3.0.0", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/45178/"]
ougcAwards = ["OUGC Awards", "1.8.3", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/46080/"]
ipLogs = ["User IP History Logs", "1.0.2", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/46273/"]
trashbin = ["Trash Bin", "1.1.3", "Cross-Site Scripting & CSRF", "https://www.exploit-db.com/exploits/46384"]
timeline = ["Timeline", "1.0", "Cross-Site Scripting & CSRF", "https://www.exploit-db.com/exploits/49467"]
threadRedirect = ["Thread Redirect", "0.2.1", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/49505"]
trendWidget = ["Trending Widget", "1.2", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/49504"]
deleteAccount = ["Delete Account", "1.4", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/49500"]
ougcFeedback = ["OUGC Feedback", "1.8.22", "Cross-Site Scripting", "https://www.exploit-db.com/exploits/49635"]

def credits():
	print (lightgreen("MyBBscan"))
	print (white("Made By: ") + lightblue("0xB9"))
	print (white("Twitter: ") + lightblue("0xB9sec"))
	print ("")
credits()
time.sleep(2)

print ("-"*60)
print (lightgreen("Example: ") + white("MyBBforum.com or subdomain.MyBBforum.com"))
print ("-"*60)

site = input(lightgreen("Enter MyBB forum URL-> "))

print (run(lightgreen("Scanning ") + bold(red("{}".format(site)))))
print ("-"*60)

def connection_status(site, plugin_file):
    connection = http.client.HTTPSConnection(site)
    connection.request("HEAD", plugin_file)
    return connection.getresponse().status


def scan(site, upload):
	status = connection_status(site, "/inc/plugins/"+upload)
	if status == 200:
		if upload == "mytabs.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+myTabs[0])
			print ("Version: "+myTabs[1])
			print ("Vulnerability Type: "+myTabs[2])
			print ("Information: "+myTabs[3])
			print ("-"*60)
		elif upload == "usersocial.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+socialNetworks[0])
			print ("Version: "+socialNetworks[1])
			print ("Vulnerability Type: "+socialNetworks[2])
			print ("Information: "+socialNetworks[3])
			print ("-"*60)
		elif upload == "myawards.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+myAwards[0])
			print ("Version: "+myAwards[1])
			print ("Vulnerability Type: "+myAwards[2])
			print ("Information: "+myAwards[3])
			print ("-"*60)
		elif upload == "myarcade.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+myArcade[0])
			print ("Version: "+myArcade[1])
			print ("Vulnerability Type: "+myArcade[2])
			print ("Information: "+myArcade[3])
			print ("-"*60)
		elif upload == "tlink.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+threadToLink[0])
			print ("Version: "+threadToLink[1])
			print ("Vulnerability Type: "+threadToLink[2])
			print ("Information: "+threadToLink[3])
			print ("-"*60)
		elif upload == "mybbirlastthreadsprofile.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+lastThreadsProfile[0])
			print ("Version: "+lastThreadsProfile[1])
			print ("Vulnerability Type: "+lastThreadsProfile[2])
			print ("Information: "+lastThreadsProfile[3])
			print ("-"*60)
		elif upload == "downloads.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+downloads[0])
			print ("Version: "+downloads[1])
			print ("Vulnerability Type: "+downloads[2]+" & "+downloads[3])
			print ("XSS: "+downloads[4])
			print ("SQLi: "+downloads[5])
			print ("-"*60)
		elif upload == "recentthread.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+recentThreadIndex[0])
			print ("Version: "+recentThreadIndex[1])
			print ("Vulnerability Type: "+recentThreadIndex[2])
			print ("Information: "+recentThreadIndex[3])
			print ("-"*60)
		elif upload == "lpop.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+latestPostProfile[0])
			print ("Version: "+latestPostProfile[1])
			print ("Vulnerability Type: "+latestPostProfile[2])
			print ("Information: "+latestPostProfile[3])
			print ("-"*60)
		elif upload == "adminnotes.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+adminNotes[0])
			print ("Version: "+adminNotes[1])
			print ("Vulnerability Type: "+adminNotes[2])
			print ("Information: "+adminNotes[3])
			print ("-"*60)
		elif upload == "modnoteslog.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+modNotes[0])
			print ("Version: "+modNotes[1])
			print ("Vulnerability Type: "+modNotes[2])
			print ("XSS: "+modNotes[3])
			print ("CSRF: "+modNotes[4])
			print ("-"*60)
		elif upload == "changstats.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+advancedStats[0])
			print ("Version: "+advancedStats[1])
			print ("Vulnerability Type: "+advancedStats[2])
			print ("Information: "+advancedStats[3])
			print ("-"*60)
		elif upload == "recent_threads.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+recentThreads[0])
			print ("Version: "+recentThreads[1])
			print ("Vulnerability Type: "+recentThreads[2])
			print ("Information: "+recentThreads[3])
			print ("-"*60)
		elif upload == "newthreads.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+newThreads[0])
			print ("Version: "+newThreads[1])
			print ("Vulnerability Type: "+newThreads[2])
			print ("Information: "+newThreads[3])
			print ("-"*60)
		elif upload == "thankyoulike.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+thankyouLike[0])
			print ("Version: "+thankyouLike[1])
			print ("Vulnerability Type: "+thankyouLike[2])
			print ("Information: "+thankyouLike[3])
			print ("-"*60)
		elif upload == "ougc_awards.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+ougcAwards[0])
			print ("Version: "+ougcAwards[1])
			print ("Vulnerability Type: "+ougcAwards[2])
			print ("Information: "+ougcAwards[3])
			print ("-"*60)
		elif upload == "ip_history_logs.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+ipLogs[0])
			print ("Version: "+ipLogs[1])
			print ("Vulnerability Type: "+ipLogs[2])
			print ("Information: "+ipLogs[3])
			print ("-"*60)
		elif upload == "trashbin.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+trashbin[0])
			print ("Version: "+trashbin[1])
			print ("Vulnerability Type: "+trashbin[2])
			print ("Information: "+trashbin[3])
			print ("-"*60)
		elif upload == "timeline_cp.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+timeline[0])
			print ("Version: "+timeline[1])
			print ("Vulnerability Type: "+timeline[2])
			print ("Information: "+timeline[3])
			print ("-"*60)
		elif upload == "threadredirect.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+threadRedirect[0])
			print ("Version: "+threadRedirect[1])
			print ("Vulnerability Type: "+threadRedirect[2])
			print ("Information: "+threadRedirect[3])
			print ("-"*60)
		elif upload == "trends.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+trendWidget[0])
			print ("Version: "+trendWidget[1])
			print ("Vulnerability Type: "+trendWidget[2])
			print ("Information: "+trendWidget[3])
			print ("-"*60)
		elif upload == "deleteaccount.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+deleteAccount[0])
			print ("Version: "+deleteAccount[1])
			print ("Vulnerability Type: "+deleteAccount[2])
			print ("Information: "+deleteAccount[3])
			print ("-"*60)
		elif upload == "ougc_feedback.php":
			print (info(bold(yellow("Possible Vulnerable Plugin!"))))
			print ("Vulnerable Plugin: "+ougcFeedback[0])
			print ("Version: "+ougcFeedback[1])
			print ("Vulnerability Type: "+ougcFeedback[2])
			print ("Information: "+ougcFeedback[3])
			print ("-"*60)					
		else:
			pass
	else:
		pass

for upload in files:
	scan(site, upload)

print ("")
print (good(lightgreen("Scan complete!")))
print ("")
exit()
