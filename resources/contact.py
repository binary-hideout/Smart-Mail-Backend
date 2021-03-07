from flask_restful import Resource

class Contact(Resource):
    def get(self):
        return {"content": "GET: contact"}
    
    def post(self):
        return {"content": "POST: contact"}

    def put(self):
        return {"content": "PUT: contact"}

    def delete(self):
        return {"content": "DELETE: contact"}

class ContactList(Resource):
    def get(self):
        return {"content": "GET: contacts"}