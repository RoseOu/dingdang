# coding: utf-8
"""
sql models

    use: Flask-SQLAlchemy
    -- http://flask-sqlalchemy.pocoo.org/2.1/

"""

from . import db, login_manager
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin, current_user
from itsdangerous import JSONWebSignatureSerializer as Serializer

# permissions
class Permission:
    """
    1. COMMENT: 0x01
    2. MODERATE_COMMENTS: 0x02
    3. ADMINISTER: 0x04
    """
    COMMENT = 0x01
    MODERATE_COMMENTS = 0x02
    ADMINISTER = 0x04


# user roles
class Role(db.Model):
    """
    1. Administrator
    2. User
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.COMMENT, True),
            'Administrator': (
                Permission.COMMENT |
                Permission.MODERATE_COMMENTS |
                Permission.ADMINISTER,
                False
            )
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model, UserMixin):
    """user"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(192), unique=True, index=True)
    email = db.Column(db.String(192))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'),default=2)
    password_hash = db.Column(db.String(192))
    security_question = db.Column(db.String(192))
    security_answer = db.Column(db.String(192))
    avatar = db.Column(db.String(192))
    birthday = db.Column(db.String(128))
    middlehobby = db.relationship('MiddleHobby', backref='user', lazy='dynamic')
    address = db.relationship('Address', backref='user', lazy='dynamic')
    collect = db.relationship('Collect', backref='user', lazy='dynamic')
    cart = db.relationship('Cart', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    order = db.relationship('Order', backref='user', lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def is_admin(self):
        if self.role_id == 1:
            return True
        return False

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def generate_auth_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def __repr__(self):
        return "<User %r>" % self.username


class AnonymousUser(AnonymousUserMixin):
    """ anonymous user """
    def is_admin(self):
        return False

login_manager.anonymous_user = AnonymousUser

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(192))
    author = db.Column(db.String(192))
    translator = db.Column(db.String(192))
    market_price = db.Column(db.Float)
    selling_price = db.Column(db.Float)
    press = db.Column(db.String(192))
    edition = db.Column(db.Integer,default=1)
    publication_time = db.Column(db.String(128))
    version = db.Column(db.String(64))
    series = db.Column(db.String(64))
    middlecategory = db.relationship('MiddleCategory', backref='book', lazy='dynamic')
    language = db.Column(db.String(64))
    binding = db.Column(db.String(64))
    introduction = db.Column(db.Text)
    catalog = db.Column(db.Text)
    inventory = db.Column(db.Integer)
    number = db.Column(db.String(64))
    image = db.relationship('Image', backref='book', lazy='dynamic')
    purchase =  db.relationship('Purchase', backref='book', lazy='dynamic')
    collect = db.relationship('Collect', backref='book', lazy='dynamic')
    cart = db.relationship('Cart', backref='book', lazy='dynamic')
    comment = db.relationship('Comment', backref='book', lazy='dynamic')
    middledetail = db.relationship('MiddleDetail', backref='book', lazy='dynamic')

    def __repr__(self):
        return "<Book %r>" % self.name

class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.String(192))
    phone = db.Column(db.String(64))
    postcode = db.Column(db.String(64))
    name = db.Column(db.String(64))
    is_default = db.Column(db.Boolean,default=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return "<Address %r>" % self.location

class Hobby(db.Model):
    __tablename__ = 'hobbies'
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(64))
    middlehobby = db.relationship('MiddleHobby', backref='hobby', lazy='dynamic')

    def __repr__(self):
        return "<Hobby %r>" % self.body

class MiddleHobby(db.Model):
    __tablename__ = 'middlehobbies'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    hobby_id = db.Column(db.Integer,db.ForeignKey('hobbies.id'))

    def __repr__(self):
        return "<MiddleHobby %r>" % self.MiddleHobby

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(64))

    def __repr__(self):
        return "<Category %r>" % self.body

class MiddleCategory(db.Model):
    __tablename__ = 'middlecategories'
    id = db.Column(db.Integer,primary_key=True)
    book_id = db.Column(db.Integer,db.ForeignKey('books.id'))
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))

    def __repr__(self):
        return "<MiddleCategory %r>" % self.id

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer,primary_key=True)
    url = db.Column(db.String(192))
    book_id = db.Column(db.Integer,db.ForeignKey('books.id'))

    def __repr__(self):
        return "<Image %r>" % self.url

class Purchase(db.Model):
    __tablename__ = 'purchases'
    id = db.Column(db.Integer,primary_key=True)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    date = db.Column(db.String(64))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    def __repr__(self):
        return "<Purchase %r>" % self.id

class Collect(db.Model):
    __tablename__ = 'collects'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer,db.ForeignKey('books.id'))

    def __repr__(self):
        return "<Collect %r>" % self.id

class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer,db.ForeignKey('books.id'))
    count = db.Column(db.Integer)

    def __repr__(self):
        return "<Cart %r>" % self.id

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.String(64))
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer,db.ForeignKey('books.id'))

    def __repr__(self):
        return "<Comment %r>" % self.id

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer,primary_key=True)
    number = db.Column(db.String(64))
    freight = db.Column(db.Float,default=0)
    paynumber = db.Column(db.String(64))
    cost = db.Column(db.Float)
    create_time = db.Column(db.String(64))
    pay_time = db.Column(db.String(64))
    delivery_time = db.Column(db.String(64))
    deal_time = db.Column(db.String(64))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    detail = db.relationship('Detail', backref='order', lazy='dynamic')

    def __repr__(self):
        return "<Order %r>" % self.id

class Detail(db.Model):
    __tablename__ = 'details'
    id = db.Column(db.Integer,primary_key=True)
    count = db.Column(db.Integer)
    cost = db.Column(db.Float)
    order_id = db.Column(db.Integer,db.ForeignKey('orders.id'))
    middledetail = db.relationship('MiddleDetail', backref='detail', lazy='dynamic')

    def __repr__(self):
        return "<Detail %r>" % self.id

class MiddleDetail(db.Model):
    __tablename__ = 'middledetails'
    id = db.Column(db.Integer,primary_key=True)
    detail_id = db.Column(db.Integer,db.ForeignKey('details.id'))
    book_id = db.Column(db.Integer,db.ForeignKey('books.id'))

    def __repr__(self):
        return "<MiddleDetail %r>" % self.id

