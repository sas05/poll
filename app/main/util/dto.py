from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class VoterDto:
    api = Namespace('voter', description='voter related operations')
    voter = api.model('voter', {
        'id': fields.String(required=True, description='voter ID'),
        'name': fields.String(required=True, description='user name'),
        'email': fields.String(required=True, description='user email'),
    })