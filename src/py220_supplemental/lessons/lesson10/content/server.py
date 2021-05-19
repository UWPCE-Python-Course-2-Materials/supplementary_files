from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask import jsonify


class Employees(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from employees")
        result = {"employees": [i[0] for i in query.cursor.fetchall()]}
        conn.close()
        return jsonify(result)


class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {"data": [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        conn.close()
        return jsonify(result)


class Employees_Name(Resource):
    def get(self, employee_id: int):
        conn = db_connect.connect()
        query = conn.execute(
            "select * from employees where EmployeeId =%d " % int(employee_id)
        )
        result = {"data": [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        conn.close()
        return jsonify(result)


if __name__ == "__main__":

    db_connect = create_engine("sqlite:///chinook.db")

    app = Flask(__name__)

    api = Api(app)
    api.add_resource(Employees, "/employees")  # Route_1
    api.add_resource(Tracks, "/tracks")  # Route_2
    api.add_resource(Employees_Name, "/employees/<employee_id>")  # Route_3

    app.run(port="5002")

    db_connect.dispose()
