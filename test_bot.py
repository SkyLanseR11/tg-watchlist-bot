# Курс https://stepik.org/course/120924/syllabus
# Телеграм-боты на Python и AIOgram. Введение в профессию

from typing import Literal
from dataclasses import dataclass


# Примеры использования аннотации типов
UserDict = dict[Literal["name"] | Literal["second_name"] | Literal["username"], str]

user: UserDict = {"name": "Илья", "second_name": "Ильич", "username": "ilyusha123"}
print(user)


def say_something(number: int, word: str) -> str:
    word = word.capitalize()
    return word * number


# Класс для создания типа, например, для бд
class User:
    def __init__(self, user_id, name, age, email):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.email = email


def get_user_info(user: User) -> str:
    return f"Возраст пользователя {user.name} - {user.age}, " f"а email - {user.email}"


user_1 = User(42, "Vasiliy", 23, "vasya_pupkin@pochta.ru")
print(get_user_info(user_1))


# А теперь с использованием декоратора @dataclass
@dataclass
class DatabaseConfig:
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_password: str  # Пароль к базе данных
    database: str  # Название базы данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


config = Config(
    tg_bot=TgBot(token=BOT_TOKEN, admin_ids=ADMIN_IDS),
    db=DatabaseConfig(
        db_host=DB_HOST, db_user=DB_USER, db_password=DB_PASSWORD, database=DATABASE
    ),
)
