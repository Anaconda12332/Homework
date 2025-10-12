"""
Настроить пул соединений к базе данных при помощи asyncpg в фикстуре.
Создать таблицу users для хранения пользователей.
Написать тесты с использованием pytest-asyncio для проверки корректности
работы с базой данных.
Перед каждым тестом очищать таблицу.
Проверить как корректные операции, так и ошибки.

1. Создание таблицы пользователей:
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

2. Очистка таблицы:
TRUNCATE users;

3. Вставка нового пользователя:
INSERT INTO users (name) VALUES ($1);

4. Выбор всех пользователей:
SELECT * FROM users;

5. Поиск пользователя по имени:
SELECT id FROM users WHERE name = $1;


Создайте тестовый файл test_app.py.
Определите асинхронную фикстуру pool при помощи декоратора
Фикстура должна:
Создавать пул соединений с базой данных.
Выполнять SQL для создания таблицы, если она ещё не создана.
Очищать таблицу перед каждым тестом при помощи TRUNCATE.
Закрывать пул соединений после выполнения всех тестов.

Реализуйте тесты:
Тест 1. Добавление одного пользователя и проверка, что он появился в таблице.
Тест 2. Добавление нескольких пользователей и проверка количества строк.
Тест 3. Попытка добавить пользователя с пустым именем.
"""
import pytest
import asyncpg
import pytest_asyncio


@pytest_asyncio.fixture(scope="function")
async def pool():
    p = await asyncpg.create_pool(
        user="postgres",
        database="postgres",
        host="localhost",
        password="admin",
        min_size=2,
        max_size=5
    )
    async with p.acquire() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        )
        """)
        await conn.execute("TRUNCATE users")

    yield p
    await p.close()


@pytest.mark.asyncio
async def test_add_user(pool):
    async with pool.acquire() as conn:
        await conn.execute("INSERT INTO users (name) VALUES ($1)", "John")
        result = await conn.fetch("SELECT * FROM users WHERE name = $1", "John")
        assert len(result) == 1
        assert result[0]["name"] == "John"


@pytest.mark.asyncio
async def test_add_users(pool):
    async with pool.acquire() as conn:
        await conn.execute("INSERT INTO users (name) VALUES ($1)", "John")
        await conn.execute("INSERT INTO users (name) VALUES ($1)", "Alice")
        await conn.execute("INSERT INTO users (name) VALUES ($1)", "Ann")
        await conn.execute("INSERT INTO users (name) VALUES ($1)", "Bob")

        result = await conn.fetch("SELECT * FROM users ORDER BY id")
        assert len(result) == 4
        assert result[2]["name"] == "Ann"


@pytest.mark.asyncio
async def test_add_empty_user(pool):
    async with pool.acquire() as conn:
        with pytest.raises(asyncpg.exceptions.NotNullViolationError):
            await conn.execute("INSERT INTO users (name) VALUES ($1)", None)
        result = await conn.fetch("SELECT * FROM users")
        assert len(result) == 0
