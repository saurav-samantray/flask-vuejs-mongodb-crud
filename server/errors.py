from werkzeug.exceptions import HTTPException

class InternalServerError(HTTPException):
	pass

class SchemaValidationError(HTTPException):
	pass

class UserNotFoundError(HTTPException):
    pass

class EmailAlreadyExistError(HTTPException):
    pass

errors = {
	"InternalServerError": {
        "message": "Oops something wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Required fields missing",
         "status": 400
     },
    "UserNotFoundError": {
        "message": "User not found in database",
        "status": 400
    },
    "EmailAlreadyExistError": {
        "message": "User with specified email already exists in database",
        "status": 400
    },

}