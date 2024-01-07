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
)


goods = sqlalchemy.Table(
    'goods',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column('description', sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column('price', sqlalchemy.Float, nullable=False)
)

orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id'), nullable=False),
    sqlalchemy.Column('goods_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('goods.id'), nullable=False),
    sqlalchemy.Column('date', sqlalchemy.String(50), nullable=False),
    sqlalchemy.Column('status', sqlalchemy.String(50), nullable=False)
)
