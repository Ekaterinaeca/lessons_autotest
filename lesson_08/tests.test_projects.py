import pytest

class TestProjectsAPI:
    """Тесты для работы с проектами Yougile."""

    @pytest.mark.positive
    def test_create_project_positive(self, projects_api):
        """Позитивный тест создания проекта."""
        project_name = "Test Project"
        response = projects_api.create_project(project_name)
        assert response.status_code == 201
        assert response.json()["name"] == project_name

    @pytest.mark.negative
    def test_create_project_negative(self, projects_api):
        """Негативный тест: попытка создать проект без имени."""
        response = projects_api.create_project("")
        assert response.status_code == 400  

    @pytest.mark.positive
    def test_get_project_positive(self, projects_api, created_project_id):
        """Позитивный тест получения проекта."""
        response = projects_api.get_project(created_project_id)
        assert response.status_code == 200
        assert "id" in response.json()

    @pytest.mark.negative
    def test_get_project_negative(self, projects_api):
        """Негативный тест: попытка получить несуществующий проект."""
        response = projects_api.get_project("invalid_id_123")
        assert response.status_code == 404  

    @pytest.mark.positive
    def test_update_project_positive(self, projects_api, created_project_id):
        """Позитивный тест обновления проекта."""
        new_name = "Updated Project Name"
        response = projects_api.update_project(created_project_id, new_name)
        assert response.status_code == 200
        assert response.json()["name"] == new_name

    @pytest.mark.negative
    def test_update_project_negative(self, projects_api):
        """Негативный тест: попытка обновить несуществующий проект."""
        response = projects_api.update_project("invalid_id_123", "New Name")
        assert response.status_code == 404  