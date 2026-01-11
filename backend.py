import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # TOKEN BURADA
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = "auto-created-repo"

API_URL = "https://api.github.com"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def create_repo():
    url = f"{API_URL}/user/repos"
    data = {
        "name": REPO_NAME,
        "private": False
    }
    r = requests.post(url, headers=headers, json=data)
    if r.status_code == 201:
        print("✅ Repo oluşturuldu")
    else:
        print("❌ Repo oluşturulamadı:", r.text)

def upload_file(repo_path, local_path):
    with open(local_path, "rb") as f:
        content = base64.b64encode(f.read()).decode()

    url = f"{API_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/{repo_path}"
    data = {
        "message": f"add {repo_path}",
        "content": content
    }

    r = requests.put(url, headers=headers, json=data)
    if r.status_code in [200, 201]:
        print(f"✅ Yüklendi: {repo_path}")
    else:
        print(f"❌ Hata ({repo_path}):", r.text)

if __name__ == "__main__":
    create_repo()

    upload_file("backend.py", "backend.py")
    upload_file("requirements.txt", "requirements.txt")
    upload_file("10numaran.mp3", "10numaran.mp3")
    upload_file("templates/index.html", "templates/index.html")
