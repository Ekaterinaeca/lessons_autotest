import requests
from base64 import b64encode


class ProjectsAPI:
    def __init__(self, base_url, auth_credentials):
        self.base_url = base_url
        # Формируем Basic Auth заголовок
        auth_str = f"{auth_credentials[0]}:{auth_credentials[1]}"
        auth_bytes = b64encode(auth_str.encode('utf-8')).decode('utf-8')
        self.headers = {
            "Authorization": f"Basic {auth_bytes}",
            "Content-Type": "application/json"
        }

    def create_project(self, name: str):
        """[POST] Создание проекта."""
        url = f"{self.base_url}/api-v2/projects"
        payload = {"name": name}
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response

    def get_project(self, project_id: str):
        """[GET] Получение проекта по ID."""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response

    def update_project(self, project_id: str, new_name: str):
        """[PUT] Обновление проекта."""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        payload = {"name": new_name}
        response = requests.put(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response

    def delete_project(self, project_id: str):
        """[DELETE] Удаление проекта."""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
        return response