import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin





class User(UserMixin,ModelBase):
    __tablename__:str = 'users'

    id: int = sa.Column(sa.Integer,primary_key=True,autoincrement=True)
    user_name: str = sa.Column(sa.String(40),index=True)
    profile_image: str = sa.Column(sa.String(64),nullable=False,default='default_profile.png')
    email : str =sa.Column(sa.String(100),unique=True,index=True)
    password_hash: str = sa.Column(sa.String(160))
    create_at: datetime = sa.Column(sa.DateTime,default=datetime.now,index=True)

    def hashing_password(password):
        return generate_password_hash(password,'sha256',10)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self) -> str:
        return f"Username {self.user_name}"