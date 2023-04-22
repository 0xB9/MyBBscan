import requests
import json

repo_url = "https://api.github.com/repos/0xB9/MyBBscan/releases/latest"

response = requests.get(repo_url)
release = json.loads(response.text or response.content)
latest_version = release["tag_name"]