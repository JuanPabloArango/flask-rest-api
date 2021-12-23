from flask_restful import Resource, reqparse

from models.users import UserModel

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', required = True, type = str, help = 'Nombre de usuario que desea emplear.')
    parser.add_argument('password', required = True, type = str, help = 'Contraseña que desea emplear.')
    
    def post(self):
        data = User.parser.parse_args()
        
        user = UserModel.find_by_username(data['username'])
        if user:
            return {'Mensaje': 'Este nombre de usuario ya está en uso.'}, 409
        else:
            user = UserModel(**data)
            user.save_to_db()
            return {'Mensaje': 'Se ha registrado correctamente.'}, 201
