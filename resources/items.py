from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.items import ItemModel

class ItemList(Resource):
    def get(self):
        items = [item.json() for item in ItemModel.query.all()]
        return {'Artículos': items}, 201

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required = True, type = str, help = 'Nombre del producto.')
    parser.add_argument('price', required = True, type = float, help = 'Precio del producto.')
    parser.add_argument('store_id', required = True, type = int, help = 'Tienda donde está el producto.')
    
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if not item:
            return {'Mensaje': 'El artículo no ha sido hallado en base de datos.'}, 404
        return item.json(), 201
    
    def post(self, name):
        data = Item.parser.parse_args()
        
        item = ItemModel.find_by_name(data['name'])
        if item:
            return {'Mensaje': 'Este artículo ya existe en la base de datos.'}, 409
        else:
            item = ItemModel(name, data['price'], data['store_id'])
            item.save_to_db()
            return {'Mensaje': 'Artículo creado.'}, 201
    
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'Mensaje': 'Artículo eliminado.'}, 201
        return {'Mensaje': 'El artículo que trata de eliminar no se encuentra en base de datos.'}, 404
    
    def put(self, name):
        data = Item.parser.parse_args()
        
        item = ItemModel.find_by_name(name)
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, data['price'], data['store_id'])
        item.save_to_db()
        return {'Mensaje': 'El artículo ha sido creado/actualizado.'}, 201
            
            