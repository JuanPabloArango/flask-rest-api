from flask_restful import Resource, reqparse

from models.stores import StoreModel

class Store(Resource):
    
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 201
        return {'Mensaje': 'La tienda que busca no existe en la base de datos.'}, 404
    
    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'Mensaje': 'Esta tienda ya existe'}, 409
        else:
            store = StoreModel(name)
            store.save_to_db()
            return {'Mensaje': 'La tienda ha sido creada.'}, 201
        
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'Mensaje': 'La tienda ha sido eliminada.'}, 201
        else:
            return {'Mensaje': 'Esta tienda no existe'}, 409
        
class StoreList(Resource):
    def get(self):
        return {'Tiendas': [store.json() for store in StoreModel.query.all()]}