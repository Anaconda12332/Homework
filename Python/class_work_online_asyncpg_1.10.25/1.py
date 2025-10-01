"""
Вам предстоит создать небольшое асинхронное приложение на Python, которое
подключается к базе данных PostgreSQL с помощью пула соединений (asyncpg.create_pool).
Подключится к базе данных PostgreSQL с использованием пула соединений.
Создать таблицу students.
Добавить в таблицу несколько тестовых записей с именами и возрастами студентов.
Прочитать данные из таблицы и вывести их в консоль.
Корректно закрыть пул соединений после завершения работы.

Требования к заданию
Используйте библиотеку asyncpg.
Все операции должны выполняться через пул соединений.
Запросы к базе данных будут даны вам в готовом виде, поэтому знания SQL не требуются.
Программа должна быть написана с использованием асинхронного стиля (async def, await, asyncio.run).
После выполнения программа должна выводить список всех студентов в консоль в понятном формате.

SQL-запрос для создания таблицы:
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL
);

SQL-запрос для добавления данных:
INSERT INTO students (name, age) VALUES ($1, $2);

SQL-запрос для чтения данных:
SELECT id, name, age FROM students;

Создайте новый файл main.py.
Настройте подключение к базе данных с помощью пула соединений.
Реализуйте функции:
для создания таблицы,
для добавления тестовых данных,
для чтения данных из таблицы.
Выведите полученные данные о студентах в консоль.
Закройте пул соединений после завершения работы.
"""
import asyncio
import asyncpg


async def create_table(pool):
    async with pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INT NOT NULL
        );
    """)


async def insert_data(pool, students):
    async with pool.acquire() as conn:
        for name, age in students:
            await conn.execute(
                "INSERT INTO students (name, age) VALUES ($1, $2)",
                name, age
            )


async def read_data(pool):
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT id, name, age FROM students;")
        for row in rows:
            print(f"{row['id']}: {row['name']} ({row['age']} years old)")


async def main():
    try:
        pool = await asyncpg.create_pool(
            user="postgres",
            database="postgres",
            password="admin",
            host="localhost",
            max_size=5,
            min_size=2,
            timeout=3.0
        )
        students = [
            ("John Doe", 25),
            ('Oliver Jones', 23),
            ('Emily Smith', 21)
        ]

        tasks1 = asyncio.create_task(create_table(pool))
        tasks2 = asyncio.create_task(insert_data(pool, students))
        tasks3 = asyncio.create_task(read_data(pool))

        await asyncio.gather(tasks1, tasks2, tasks3)
    finally:
        await pool.close()

asyncio.run(main())
