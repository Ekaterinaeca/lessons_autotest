import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base, Student

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()