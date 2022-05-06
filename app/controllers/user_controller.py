import secrets
from http import HTTPStatus

from app.models.user_model import UserModel
from flask import current_app, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def create_user():
    data = request.get_json()
    correct_keys = ['name', 'last_name', 'email', 'password']
    validate_keys = correct_keys - data.keys()

    try:

        for key, value in data.items():
            if key == 'name' or key == 'last_name':
                data[key] = value.title()
            if key == 'email':
                data[key] = value.lower()

            if not key in correct_keys:
                return {
                    'error': {'valid_keys': correct_keys, 'key_sended': key}
                }, HTTPStatus.BAD_REQUEST

        if len(validate_keys) != 0:
            return {
                'error': {'misssing_keys': validate_keys}
            }, HTTPStatus.BAD_REQUEST

        session: Session = current_app.db.session

        new_user = UserModel(**data)
        session.add(new_user)
        session.commit()

        return jsonify(new_user), HTTPStatus.CREATED

    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:
            return {'error': 'User alredy exists'}, HTTPStatus.CONFLICT


def signin():
    data = request.get_json()

    user: UserModel = UserModel.query.filter_by(email=data['email']).first()

    if not user or not user.check_password(data['password']):
        return {'error': 'Email and password missmatch!'}, HTTPStatus.NOT_FOUND

    token = create_access_token(user)

    return jsonify({'token': token}), HTTPStatus.OK


@jwt_required()
def get_home():

    users = UserModel.query.all()

    return jsonify(users), HTTPStatus.OK


@jwt_required()
def put_home():
    data = request.get_json()
    correct_keys = ['name', 'last_name', 'email', 'password']

    session: Session = current_app.db.session
    user_to_update = UserModel.query.filter(
        UserModel.email == data['email']
    ).first()

    if not user_to_update:
        return {'error': 'User not exists!'}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        if key == 'name' or key == 'lastname':
            data[key] = value.title()
        if key == 'email':
            data[key] = value.lower()
        if not value:
            return {
                'error': f'{key.upper()} is empty!'
            }, HTTPStatus.BAD_REQUEST

        if not key in correct_keys:
            return {
                'error': {'valid_keys': correct_keys, 'key_sended': key}
            }, HTTPStatus.BAD_REQUEST

        if type(value) != str:
            return {
                'error': 'The values only accept Strings'
            }, HTTPStatus.BAD_REQUEST

        setattr(user_to_update, key, value)

    session.add(user_to_update)
    session.commit()

    return jsonify(user_to_update), HTTPStatus.OK


@jwt_required()
def delete_user():
    user = UserModel.query.first()

    session: Session = current_app.db.session

    if not user:
        return {'error': "user doesn't exists!"}, HTTPStatus.NOT_FOUND

    session.delete(user)
    session.commit()

    return {'msg': f'User {user.name} has been deleted.'}, HTTPStatus.OK
