from pydantic import BaseModel, Field
from datetime import datetime

# • Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
# • Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
# • Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.


class User(BaseModel):
    id: int = Field(None, description='id')
    name: str = Field(min_length=3, max_length=15, description='name')
    surname: str = Field(min_length=3, max_length=15, description='surname')
    email: str = Field(description='email')
    password: str = Field(min_length=3, max_length=15, description='password')


class UserIn(BaseModel):
    name: str = Field(min_length=3, max_length=15, description='name')
    surname: str = Field(min_length=3, max_length=15, description='surname')
    email: str = Field(description='email')
    password: str = Field(min_length=3, max_length=15, description='password')


class Order(BaseModel):
    id: int = Field(None, description='id')
    user_id: int
    goods_id: int
    # date: datetime = Field(default=datetime.now(), description='date')
    date: str = Field(..., description='date')
    status: str


class OrderIn(BaseModel):
    user_id: int
    goods_id: int
    # date: datetime = Field(default=datetime.now(), description='date')
    date: str = Field(..., description='date')
    status: str


class Goods(BaseModel):
    id: int = Field(None, description='id')
    name: str = Field(min_length=3, max_length=15, description='name')
    description: str = Field(
        min_length=3, max_length=15, description='description')
    price: float = Field(ge=1, description='price')


class GoodsIn(BaseModel):
    name: str = Field(min_length=3, max_length=15, description='name')
    description: str = Field(
        min_length=3, max_length=15, description='description')
    price: float = Field(ge=1, description='price')
