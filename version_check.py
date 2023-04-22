import requests
import json

repo_url = "https://api.github.com/repos/{owner}/{repo}/releases/latest"
owner = "0xB9"
repo = "MyBBscan"

response = requests.get(repo_url.format(owner=owner, repo=repo))
release = json.loads(response.text or response.content)
latest_version = release["tag_name"]