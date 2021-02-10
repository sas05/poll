import werkzeug
from flask_restplus import reqparse


class parsers():
    file_upload = reqparse.RequestParser()
    file_upload.add_argument('xls_file',
                             type=werkzeug.datastructures.FileStorage,
                             location='files',
                             required=True,
                             help='XLS file')
