import pytest
from sqlalchemy.exc import IntegrityError

# Измененный импорт (без точки)
from models import Student

def test_create_student(db_session):
    """Тест добавления студента"""
    new_student = Student(name="Иван Иванов", email="ivan@example.com")
    db_session.add(new_student)
    db_session.commit()
    
    student = db_session.query(Student).filter_by(email="ivan@example.com").first()
    assert student is not None
    assert student.name == "Иван Иванов"
    assert student.is_active is True
    
    # Очистка
    db_session.delete(student)
    db_session.commit()

def test_update_student(db_session):
    """Тест изменения студента"""
    student = Student(name="Петр Петров", email="petr@example.com")
    db_session.add(student)
    db_session.commit()
    
    student.name = "Петр Сидоров"
    db_session.commit()
    
    updated_student = db_session.query(Student).filter_by(email="petr@example.com").first()
    assert updated_student.name == "Петр Сидоров"
    
    # Очистка
    db_session.delete(updated_student)
    db_session.commit()

def test_soft_delete_student(db_session):
    """Тест мягкого удаления студента"""
    student = Student(name="Сергей Сергеев", email="sergey@example.com")
    db_session.add(student)
    db_session.commit()
    
    student.is_active = False
    db_session.commit()
    
    deleted_student = db_session.query(Student).filter_by(email="sergey@example.com").first()
    assert deleted_student.is_active is False
    
    # Восстановление для повторного запуска
    deleted_student.is_active = True
    db_session.commit()
    
    # Полная очистка
    db_session.delete(deleted_student)
    db_session.commit()