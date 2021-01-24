from flask import Response, request
from flask import current_app as app
from db.models import User
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError
from errors import InternalServerError, SchemaValidationError, UserNotFoundError, EmailAlreadyExistError


class UsersApi(Resource):
	def get(self):
		users = User.objects().to_json()
		return Response(users, mimetype="application/json", status=200)

	def delete(self):
		user = User.objects.delete()
		return '', 200

	def post(self):
		try:
			body = request.get_json()
			user = User(**body).save()
			id = user.id
			return {'id': str(id)}, 201
		except NotUniqueError:
			raise EmailAlreadyExistError
		except ValidationError:
			raise SchemaValidationError
		except Exception as e:
			app.logger.error(e)
			raise InternalServerError

class UserApi(Resource):
	def put(self, id):
		body = request.get_json()
		User.objects.get(id=id).update(**body)
		return '', 200

	def get(self, id):
		try:
			users = User.objects.get(id=id).to_json()
			return Response(users, mimetype="application/json", status=200)
		except DoesNotExist:
			raise UserNotFoundError

	def delete(self, id):
		user = User.objects.get(id=id).delete()
		return '', 200