from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from db import db
from security import authenticate, identity
from resources.users import User
from resources.items import Item, ItemList
from resources.stores import Store, StoreList

app = Flask(__name__)
app.secret_key = 'juan arango'

db.init_app(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

@app.before_first_request
def create_tables():
    db.create_all()

api = Api(app)
jwt = (app, authenticate, identity)

api.add_resource(User, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/item')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/store')

if __name__ == '__main__':
    app.run(debug = True)