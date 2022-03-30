from flask_restful import Resource, Api
from flask import request
import uuid
from utils.models.user import User
from utils.db import db

class HomeRoute(Resource):
    def get(self):
        users = db.session.query(User).all()
        users = [user.to_json() for user in users]
        return {'data': users}
    
    def post(self):
        # is_testing = request.form['testing']
        # print(is_testing)
        user_id = str(uuid.uuid4())
        first_name = request.form['name']
        last_name = request.form['last_name']
        email = request.form['email']
        user = User(user_id = user_id, first_name=first_name, last_name=last_name, email=email)
        db.session.add(user) # Add user to database
        db.session.commit() # Commit (save) change to database
        return {'data': user.to_json()}

class HomeRouteWithId(Resource):
    def get(self, id):
        data_object = db.session.query(User).filter(User.user_id == id).first()
        if data_object:
            return {'data': data_object.to_json()}
        else:
            return {'data': 'Not found'}, 404
    
    def put(self, id):
        data_object = db.session.query(User).filter(User.user_id == id).first()
        if data_object:
            for key in request.form.keys():
                setattr(data_object, key, request.form[key])
            db.session.commit()
            return {'data': data_object.to_json()}
        else:
            return {'data': 'Not found'}, 404

    def delete(self, id):
        data_object = db.session.query(User).filter(User.user_id == id).first()
        if data_object:
            db.session.delete(data_object)
            db.session.commit()
            return {'data': 'DELETED'}
        else:
            return {'data': 'Not found'}, 404
