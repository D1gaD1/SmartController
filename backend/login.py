from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = '192.168.8.147'
app.config['MYSQL_USER'] = 'admindb'
app.config['MYSQL_PASSWORD'] = 'Passw0rd'
app.config['MYSQL_DB'] = 'user_data'

mysql = MySQL(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    cur = mysql.connection.cursor()
    cur.execute('SELECT password FROM users WHERE username = %s', (username,))
    result = cur.fetchone()

    if result is None:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404
    
    hashed_password = result[0]

    if not check_password_hash(hashed_password, password):
        return jsonify({'status': 'error', 'message': 'Password is incorrect'}), 400
    
    return jsonify({'status': 'success', 'message': 'Logged in successfully'}), 200

@app.route('/getDeviceList', methods=['GET'])
def getDeviceList():
    # Using a MySQL cursor to execute a SQL statement
    cur = mysql.connection.cursor()

    # Execute the SQL command to select all devices from the `devices` table
    cur.execute('SELECT device_name FROM devices')

    # Fetch all results from the cursor
    device_list = cur.fetchall()

    # Convert the tuple into a list and return
    return jsonify(list(device_list)), 200

@app.route('/getLogs', methods=['GET'])
def getLogs():
    # Open log.txt file in read mode
    with open('log.txt', 'r') as log_file:
        # Read all lines from log_file
        log_list = log_file.readlines()
    return jsonify(log_list), 200
    
@app.route('/addDevice', methods=['POST', 'OPTIONS'])
def addDevice():
    if request.method == 'OPTIONS':
        # Allows the browser to continue with the "real" request
        response = app.make_default_options_response()
    elif request.method == 'POST':
        device_name = request.json.get('deviceName')
        
        # Your logic to add device goes here.
        # It should add device_name to the connected devices list in your database

        response = jsonify({'status': 'success', 'message': 'Device added successfully'})

    # Allow CORS
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = "Content-Type"
    return response


if __name__ == '__main__':
    app.run(debug=True)
