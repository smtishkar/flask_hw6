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
from random import randint, choice
from typing import List
import datetime

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


@app.get("/fake_orders/{count}")
async def create_note(count: int):
    for i in range(count):
        query = orders.insert().values(user_id=randint(0,10), goods_id=randint(0,10), date=f'2024-01-{i+1}', status= f'{choice(["in progress", "done", "canceled"])}')            
        await database.execute(query)
    return {'message': f'{count} fake orders created'}


@app.get('/users/', response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)

@app.get('/orders/', response_model=List[Order])
async def read_users():
    query = orders.select()
    return await database.fetch_all(query)

@app.get('/goods/', response_model=List[Goods])
async def read_users():
    query = goods.select()
    return await database.fetch_all(query)

@app.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)

@app.get('/orders/{order_id}', response_model=Order)
async def read_user(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@app.get('/goods/{goods_id}', response_model=Goods)
async def read_user(goods_id: int):
    query = goods.select().where(goods.c.id == goods_id)
    return await database.fetch_one(query)

@app.post('/users/', response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(
        name=user.name,
        surname=user.surname,
        email=user.email,
        password=user.password
        )
    last_record_id = await database.execute(query)
    return {**user.dict(), 'id': last_record_id}


@app.post('/orders/', response_model=Order)
async def create_order(order: OrderIn):
    query = orders.insert().values(
        user_id=order.user_id,
        goods_id=order.goods_id,
        date=order.date,
        status=order.status
        )
    last_record_id = await database.execute(query)
    return {**order.dict(), 'id': last_record_id}


@app.post('/goods/', response_model=Goods)
async def create_good(good: GoodsIn):
    query = goods.insert().values(
        name=good.name,
        description=good.description,
        price=good.price
        )
    last_record_id = await database.execute(query)
    return {**good.dict(), 'id': last_record_id}