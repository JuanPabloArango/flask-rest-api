from werkzeug.security import safe_str_cmp

from models.users import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
    return {'Mensaje': 'Verifique que su usuario y/o contraseña sean correctas.'}, 401

def identity(payload):
    user_id = payload['id']
    user = UserModel.find_by_id(user_id)
    return user
    