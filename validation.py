from cerberus import Validator

class Validation():
    def __init__(self):
        self.SCHEMA_CREATE_USER = {
            "email": {"type": "string", "required": True, "minlength": 3},
            "name": {"type": "string", "required": True, "minlength": 2},
            "age":{"type": "number", "required": True, "minlength": 1},
            "role": {"type": "string", "required": True, "minlength":4}
        }

    def checking_user_create(self,data):
        checking= Validator(self.SCHEMA_CREATE_USER)
        if not checking.validate(data):
            return {
                "payload": None,
                "error": checking.errors
            }        
