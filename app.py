from flask import Flask, request, jsonify
from flask_cors import CORS
from validation import Validation
from user import User
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
CORS(app)
limiter = Limiter(get_remote_address)
limiter.init_app(app)

class_user = User()


@app.before_request
def validate_customer():
    if request.path=="/user/create" and (request.method=="POST" or request.method=="PUT"):
        class_validation = Validation()
        result_data =class_validation.checking_user_create(request.get_json())
        if result_data:
            return jsonify(result_data)
        pass
            
        


@app.route("/user/create", methods=["POST","PUT"])
@limiter.limit("5/minute")
def fn_create_user():
    user = request.get_json()
    class_user = User(user)
    if request.method=="POST":
        result = class_user.fn_create_user()
    else:
        result = class_user.fn_update_user()
    return jsonify(result)

@app.route("/v1/g/user", methods=["GET"])
@limiter.limit("5/minute")
def fn_get_all_user():
    result = class_user.fn_get_users()
    return jsonify(result)

@app.route("/v1/m/user")
@limiter.limit("5/minute")
def fn_get_mobile_user():
    page = request.args.get("page")
    if page == None: page = 1
    result= class_user.fn_get_mobile_user(page)
    return result

@app.route("/v1/d/user")
@limiter.limit("5/minute")
def fn_get_desktop_user():
    page = request.args.get("page")
    if page == None: page = 1
    result= class_user.fn_get_desktop_user(page)
    return result

@app.route("/user/delete", methods=["DELETE"])
@limiter.limit("5/minute")
def fn_delete_user():
    email = request.args.get("email")
    result = class_user.fn_delete_user(email)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

