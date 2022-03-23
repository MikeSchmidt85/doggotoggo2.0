from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL


class VIP:
    def __init__(self, data):
        self.id = data["id"]
        self.your_name = data["your_name"]
        self.your_dogs_name = data["your_dogs_name"]
        self.gender = data["gender"]
        self.email = data["email"]


    @classmethod
    def create(cls,data):
        query = "INSERT INTO vip (your_name, your_dogs_name, gender, email, created_at, updated_at) VALUE (%(your_name)s, %(your_dogs_name)s, %(gender)s, %(email)s, NOW(), NOW());"
        results = connectToMySQL("dogs").query_db(query,data)
        print(results)
        return results
