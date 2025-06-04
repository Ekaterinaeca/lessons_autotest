import os
from dotenv import load_dotenv

load_dotenv()  # Загружает данные из .env

def get_auth():
    login = os.getenv("YOUGILE_LOGIN")  # Заменить на emeil
    password = os.getenv("YOUGILE_PASSWORD") #Заменить на пароль
    return (login, password)  # Для Basic Auth
