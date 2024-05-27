import requests
import zipfile
import os
from io import BytesIO

def download_and_extract_github_repo(owner, repo, save_path):
    """
    :param owner: Владелец репозитория
    :param repo: Название репозитория
    :param save_path: Путь к папке, куда будут распакованы файлы
    """
    url = f"https://github.com/{owner}/{repo}/archive/refs/heads/main.zip"
    response = requests.get(url)
    
    if response.status_code == 200:
        with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(save_path)
        print(f"Репозиторий {repo} успешно скачан и распакован в {save_path}")
    else:
        print(f"Не удалось скачать репозиторий: статус код {response.status_code}")


owner = "timonoTV"  # Замените на владельца репозитория
repo = "virus"  # Замените на название репозитория
save_path = "repository"  # Путь к папке для распаковки

# Создаем папку, если её не существует
os.makedirs(save_path, exist_ok=True)

download_and_extract_github_repo(owner, repo, save_path)
