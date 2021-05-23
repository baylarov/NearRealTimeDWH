from flask import Flask, jsonify
from postgres_conn import ConnectionCursor
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Kırmızı Oda was here.'


@app.route('/employees/all/', methods=['GET'])
def all_employees():
    query = 'select * from RTDWOrder.employees'
    with ConnectionCursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return jsonify(result)


@app.route('/employees/<id>', methods=['GET'])
def employee_id(id):
    query = f"select * from RTDWOrder.employees where id={id}"
    with ConnectionCursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
