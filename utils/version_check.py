from huepy import *
import requests
import json

currentVersion = "v3.2.0"
repo = "https://api.github.com/repos/0xB9/MyBBscan/releases/latest"

response = requests.get(repo)
release = json.loads(response.text or response.content)
latestVersion = release["tag_name"]

def checkVersion():
	if response.ok:
		if latestVersion == currentVersion:
			print (good(lightgreen("MyBBscan is up to date")))
			print ("-"*60)
		else:
			print (bad(red(f"MyBBscan out of date. The latest version is {latestVersion}")))
			print (info(white("Visit https://github.com/0xB9/MyBBscan/releases/latest to download the latest version.")))
			print ("-"*95)
	else:
		print (info(yellow(f"Failed to check for updates, try again later.")))
		print ("-"*60)
