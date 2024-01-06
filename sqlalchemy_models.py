import sqlalchemy

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users', 
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column('surname', sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column('email', sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column('password', sqlalchemy.String(50), nullable=False)
    # id = sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    # username = sqlalchemy.Column('name', sqlalchemy.String(50), nullable=False),
    # surname = sqlalchemy.Column('surname', sqlalchemy.String(50), nullable=False),
    # email = sqlalchemy.Column('email', sqlalchemy.String(50), nullable=False),
    # password = sqla
)


goods = sqlalchemy.Table(
    'goods', 
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column('description', sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column('price', sqlalchemy.Float, nullable=False)
    # id = sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    # name = sqlalchemy.Column('name', sqlalchemy.String(50), nullable=False),
    # description = sqlalchemy.Column('description', sqlalchemy.String(50), nullable=False),
    # price = sqlalchemy.Column('price', sqlalchemy.Float, nullable=False)
)

orders = sqlalchemy.Table(
    'orders', 
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False),
    sqlalchemy.Column('goods_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('goods.id'), nullable=False),
    sqlalchemy.Column('date', sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column('status', sqlalchemy.String(50), nullable=False)
    # id = sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    # user_id = sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False),
    # goods_id = sqlalchemy.Column('goods_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('goods.id'), nullable=False),
    # date = sqlalchemy.Column('date', sqlalchemy.DateTime, nullable=False),
    # status = sqlalchemy.Column('status', sqlalchemy.String(50), nullable=False)
)


