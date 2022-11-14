from optparse import Values
from flask import jsonify, make_response

def success(values, message):
    return make_response(jsonify({
        #'success': True,
        'message': message,
        'data': values
    }), 200)

def BadRequest(values, message):
    return make_response(jsonify({
        # 'success': False,
        'message': message,
        'data': values
    }), 400)