# Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
# — Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
# — Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
# — Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.
# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
# • Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.

# Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
# Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.

# Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет"

import databases
from pydantic_models import User, UserIn, Order, OrderIn, Goods, GoodsIn
from sqlalchemy_models import users, goods, orders, metadata
from sqlalchemy import create_engine, select, insert, update, delete, MetaData
from fastapi import FastAPI

DATABASE_URL = 'sqlite:///shop.db'

database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# metadata = MetaData()
metadata.create_all(engine)

app = FastAPI()



@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get('/')
async def root():
    return {"message": "Welcome to my shop"}

@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'user{i}', surname=f'surname{i}', email=f'mail{i}@mail.ru', password=f'password{i}')
        await database.execute(query)
    return {'message': f'{count} fake users created'}

@app.get("/fake_goods/{count}")
async def create_note(count: int):
    for i in range(count):
        query = goods.insert().values(name=f'name {i}', description=f'description {i}', price=f'{10* (i+1)}')
        await database.execute(query)
    return {'message': f'{count} fake goods created'}