from flask import request
from flask_restplus import Resource

from ..util.dto import VoterDto
from ..service.voter_service import get_all_voters, save_new_voter

from ..util.parsers import parsers

api = VoterDto.api
_voter = VoterDto.voter


@api.route('/')
class VoterList(Resource):
    @api.doc('list_of_registered_voters')
    @api.marshal_list_with(_voter, envelope='data')
    def get(self):
        """List all registered voters"""
        return get_all_voters()

    @api.response(201, 'Voter successfully created.')
    @api.doc('create a new voter')
    @api.expect(_voter, validate=True)
    def post(self):
        """creates a new voter"""
        data = request.json
        return save_new_voter(data=data)


@api.route('/bulk-loading')
class VoterList(Resource):
    @api.response(201, 'Bulk voter list successfully uploaded.')
    @api.doc('create new voters')
    @api.expect(parsers.file_upload)
    def post(self):
        api.abort(404)
