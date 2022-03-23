from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class Adoption:
    def __init__(self, data):
        self.id = data["id"]
        self.full_name = data["full_name"]
        self.address = data["address"]
        self.city = data["city"]
        self.state = data["state"]
        self.zip_code = data["zip_code"]
        self.phone_number = data["phone_number"]
        self.email = data["email"]


    @classmethod
    def create(cls,data):
        query = "INSERT INTO adoption (full_name, address, city, state, zip_code, phone_number, email, created_at, updated_at) VALUE (%(full_name)s, %(address)s, %(city)s, %(state)s, %(zip_code)s, %(phone_number)s, %(email)s, NOW(), NOW());"
        results = connectToMySQL("dogs").query_db(query,data)
        print(results)
        return results