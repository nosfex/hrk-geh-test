from flask import Flask, request, jsonify
import psycopg2
from config import config
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello World!"

@app.route('/config_db/')
def config_db():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute('SELECT version()')

        db_version = cur.fecthone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Connection closed')
@app.route('/get/', methods=['GET'])
def get_test():
    name = request.args.get("name",None)
    print(f"got name {name}")
    response = {}

    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_test():
    name = request.form.get('name')
    print(name)

    if name:
        return jsonify({               
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })
