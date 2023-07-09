from flask import Flask, jsonify, request, session, redirect, url_for
from ctl.LoginCtl import LoginCtl
from ctl.StudentCtl import StudentCtl
from ctl.AppResult import AppResult
from ctl.UserRegCtl import UserRegCtl


app = Flask(__name__)
# app.secret_key = 12345

# define a simple route
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to CuickDev!'})

# get the class object from given name
def get_class(class_name, *args, **kwargs):
    try:
        obj = globals()[class_name](*args, **kwargs)
        return obj
    except KeyError:
        print("Class", class_name, "does not exist!")
        return None    

# define a route with parameters
@app.route('/ctl/<string:name>', methods=['GET','POST'])
def callCtl(name):
    print(request.method)
    str = name + "Ctl"
    obj = get_class(str)
    res = obj.execute()
    return jsonify(res.to_dict())

@app.route('/ctl/<string:name>/<int:id>', methods=['GET'])
def callCtlWithID(name,id):
    str = name + "Ctl"
    obj = get_class(str)
    obj.setId(id)
    res = obj.execute()
    return jsonify(res.to_dict())

@app.route('/ctl/<string:name>/<string:method>', methods=['GET','POST'])
def callCtlMethod(name,method):
    str = name + "Ctl"
    # Create an instance of the class
    obj = get_class(str)
    # Get the method using getattr()
    method = getattr(obj, method) 
    # Call the method
    res = method()
    return jsonify(res.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
