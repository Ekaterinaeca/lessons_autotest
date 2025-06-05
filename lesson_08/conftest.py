import os
import pytest
from dotenv import load_dotenv
from api_projects import ProjectsAPI


load_dotenv()  # Загружает данные из .env


def get_auth():
    """Получение данных аутентификации."""
    login = os.getenv("YOUGILE_LOGIN")
    password = os.getenv("YOUGILE_PASSWORD")
    return (login, password)


@pytest.fixture
def projects_api():
    """Фикстура для API клиента."""
    base_url = "https://ru.yougile.com/api-v2"
    auth_credentials = get_auth()
    return ProjectsAPI(base_url, auth_credentials)


@pytest.fixture
def created_project_id(projects_api):
    """Фикстура для временного проекта."""
    project = projects_api.create_project("Temp Project")
    project_id = project.json()["id"]
    yield project_id
    # Удаление проекта после теста
    projects_api.delete_project(project_id)