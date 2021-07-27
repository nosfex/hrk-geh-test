from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello World!"
@app.route('/get/', methods=['GET'])
def get_test():
    name = request.args.get("name",None)
    print(f"got name {name}")
    response = {}

    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_test():
    param = request.form.get('name')
    print(param)

    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })
