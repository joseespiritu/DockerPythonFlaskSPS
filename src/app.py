from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost/rest_api_sps'
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({"response": "hello world"})

@app.route('/api/sps/helloworld/v1', methods=['POST'])
def create_user():
    #Receiving Data
    username = request.json['username']
    email = request.json['email']

    if username and email:
        id = mongo.db.users.insert(
            {'username': username,
            'email': email}
        )
        response = {
            'id': str(id),
            'username': username,
            'email': email
        }
        return response
    else:
        return not_found()

    return {'message': 'received'}

@app.route('/api/sps/helloworld/v1', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')

@app.route('/api/sps/helloworld/v1/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(user)
    return Response(response, mimetype='application/json')

@app.route('/api/sps/helloworld/v1/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id':ObjectId(id)})
    response = jsonify({'message': 'User ' + id + 'was Deleted successfully'})
    return response

@app.route('/api/sps/helloworld/v1/<id>', methods=['PUT'])
def update_user(id):
    username = request.json['username']
    email = request.json['email']

    if username and email:
        mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': {
            'username': username,
            'email': email
        }})
        response = jsonify({'message': 'User ' + id + ' was updated successfully' })
        return response

@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        "message": "Resource not found: " + request.url,
        "status": 404
    })
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="4000", debug="true")