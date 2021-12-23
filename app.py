from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.users import User
from resources.items import Item, ItemList
from resources.stores import Store, StoreList

app = Flask(__name__)
app.secret_key = 'juan arango'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

api = Api(app)
jwt = (app, authenticate, identity)

api.add_resource(User, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/item')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/store')

if __name__ == '__main__':
    app.run(debug = True)