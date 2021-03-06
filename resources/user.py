import sqlite3
from flask_restful import Resource, reqparse
from models.usermodel import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )

    def post(self):

        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']) is not None: # check if username already exists
            return {"message": "User with that name already exists"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "Account created"}, 201 # 201 is created

