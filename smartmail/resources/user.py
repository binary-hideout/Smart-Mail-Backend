from flask_restful import Resource, reqparse
from flask import request
from smartmail.models.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)
from marshmallow import ValidationError
from smartmail.blacklist import BLACKLIST
from smartmail.schemas.schemas import UserSchema
import traceback

user_schema = UserSchema()

class UserRegister(Resource):
    @classmethod
    def post(cls):
        user = user_schema.load(request.get_json())
        if UserModel.find_by_username(user.username):
            return {"message": f"ERROR: Username already exists <user={user.username}>"}, 400
        if UserModel.find_by_email(user.email):
            return {"message": f"ERROR: Email already exists <user={user.email}>"}, 400
        try:
            user.save_to_db()
            return {"message": "User registered succesfully"}, 201
        except:
            traceback.print_exc()
            user.delete_from_db()
            return {"message": "Unable to register user"}, 500

class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not User:
            return {"message": "User not found"}, 404
        return user_schema.dump(user), 200
    
    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not User:
            return {"message": "User not found"}, 404
        user.delete_from_db()
        return {"message": "User deleted succesfully"}, 200

class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_data = user_schema.load(request.get_json(), partial=("email",))
        user = UserModel.find_by_username(user_data.username)
        if user and safe_str_cmp(user.password, user_data.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
            }, 200
        return {"message": "Incorrect login data"}, 400

class UserLogout(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        jti = get_jwt()["jti"]
        user_id = get_jwt_identity()
        BLACKLIST.add(jti)
        return {"message": "User logged out"}

class TokenRefresh(Resource):
    @classmethod
    @jwt_required(refresh=True)
    def post(cls):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=True)
        return {"Access Token": new_token}, 200