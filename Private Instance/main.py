from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(_name_)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host="DATABASE-ENDPOINT",
        user="USERNAME",
        password="USER_PASSWORD",
        database="DATABASE_NAME"
    )

@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM TABLE-NAME LIMIT 5;")
    usuarios = cursor.fetchall()
    conn.close()
    print(usuarios)


if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)
