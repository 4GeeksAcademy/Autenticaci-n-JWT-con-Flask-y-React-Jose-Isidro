"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def add_User():
    email = request.json.get("email")
    password =request.json.get("password")

    if not email or not password:
        return jsonify({"msg" : "Se requiere de un email y password"})
    
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"msg": "User ya existente"})
    
    new_user = User(
        email = email,
        password = password,
        is_active = True
    )
    db.session.add(new_user)
    db.session.commit()

    # 7️⃣ Responder
    return jsonify({"msg": "Nuevo usuario creado"}), 201

@api.route('/login', methods=['POST'])
def access_User():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # Consulta la base de datos por el nombre de usuario y la contraseña
    user = User.query.filter_by(email=email, password=password).first()

    if user is None:
        # el usuario no se encontró en la base de datos
        return jsonify({"msg": "Bad email or password"}), 401
    
    # Crea un nuevo token con el id de usuario dentro
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id })

@api.route('/private' , methods=['GET'])
@jwt_required()
def get_protec():

    current_user = get_jwt_identity()

    user = User.query.get(current_user)

    if not user:
        return jsonify({"msg" :"Usuario no encontrado"})
    
    return jsonify({"msg" :"Usuario encontrado","usuario": user.serialize()}), 200
