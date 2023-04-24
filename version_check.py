import requests
import json

currentVersion = "v3.0"
repo = "https://api.github.com/repos/0xB9/MyBBscan/releases/latest"

response = requests.get(repo)
release = json.loads(response.text or response.content)
latestVersion = release["tag_name"]