from flask_restful import Resource


class Contact(Resource):
    def get(self, email: str):
        return {"content": f"GET: contact <email={email}>"}

    def post(self, email: str):
        return {"content": f"POST: contact <email={email}>"}

    def put(self, email: str):
        return {"content": f"PUT: contact <email={email}>"}

    def delete(self, email: str):
        return {"content": f"DELETE: contact <email={email}>"}


class ContactList(Resource):
    def get(self):
        return {"content": "GET: contacts"}
