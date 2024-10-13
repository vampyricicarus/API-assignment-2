from flask import Flask, Jsonify
from flask_marshmallow import Marshmallow
from Marshmallow import fields

app = Flask(__name__)
ma = Marshmallow(app)

@app.route('/members', methods=['POST'])
def add_member():
    try:
        conn = get_db_connection()
        if conn == None:
            return Jsonify("Error: connection failed"), 500
        cursor = conn.cursor()
        query = add_member("name", "age", "email")
        cursor.execute(query)
        cursor.commit()
        return members_schema.jsonify(members)
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    try:
        conn = get_db_connection()
        if conn == None:
            return Jsonify({"Error: connection failed"}), 500
        cursor = conn.cursor(dictionaries=True)

        query = "SELECT * FROM members"

        cursor.execute(query)

        return members_schema.jsonify(members)
    except Error as e:
        print(f"Error: {e}")
        return Jsonify({"Error Internal server error"})
    finally:
        if conn and conn.isconnected():
            cursor.close()
            conn.close()

@app.route("/members/update", methods=["PUT"])
def update_member():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE FROM members VALUES %s, %s, %s"
        cursor.execute(query, "name", "age", "email")
        cursor.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

@app.route("/members/delete", methods=["DELETE"])
def delete_member():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM members VALUES %s, %s, %s"
        cursory.execute(query, "name", "age", "email")
        cursor.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()