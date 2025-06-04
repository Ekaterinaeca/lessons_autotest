import requests

class ProjectsAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, name: str):
        """[POST] Создание проекта"""
        url = f"{self.base_url}/api-v2/projects"
        payload = {"name": name}
        return requests.post(url, json=payload, headers=self.headers)

    def get_project(self, project_id: str):
        """[GET] Получение проекта по ID"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id: str, new_name: str):
        """[PUT] Обновление проекта"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        payload = {"name": new_name}
        return requests.put(url, json=payload, headers=self.headers)