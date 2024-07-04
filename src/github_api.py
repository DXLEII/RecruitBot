import requests
from config import GITHUB_TOKEN, OWNER, REPO

github_api_url = f"https://api.github.com/repos/{OWNER}/{REPO}"

def get_latest_commit_sha():
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'
    }
    try:
        response = requests.get(f"{github_api_url}/commits", headers=headers)
        response.raise_for_status()
        commits = response.json()
        if commits:
            return commits[0]['sha']
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching latest commit: {e}")
        return None

def get_stars_count():
    try:
        response = requests.get(github_api_url)
        response.raise_for_status()
        repo_info = response.json()
        return repo_info['stargazers_count']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching stars count: {e}")
        return None
