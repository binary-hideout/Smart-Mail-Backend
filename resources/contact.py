from flask_restful import Resource

class Contact(Resource):
    def get(self):
        return {"content": "contact"}
    
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

class ContactList(Resource):
    def get(self):
        return {"content": "contacts"}