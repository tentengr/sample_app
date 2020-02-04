from flask import request
from flask_restful import Resource
# from flask_jwt_extended import jwt_required

# from vodafone_api.models import User
# from vodafone_api.extensions import ma, db
from vodafone_api.commons.pagination import paginate


# class DatetimeSchema(ma.ModelSchema):

#     id = ma.Int(dump_only=True)
#     datetime = ma.String(load_only=True, required=True)

#     # class Meta:
#     #     model = User
#     #     sqla_session = db.session


class DatetimeResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - api
      parameters:
        - in: path
          name: datetime_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  user: UserSchema
        404:
          description: datetime does not exists
    put:
      tags:
        - api
      parameters:
        - in: path
          name: datetime_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              UserSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: datetime updated
                  user: UserSchema
        404:
          description: datetime does not exists
    delete:
      tags:
        - api
      parameters:
        - in: path
          name: datetime_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: datetime deleted
        404:
          description: datetime does not exists
    """
    def get(self):
    	return {"datetime": "get verb"}

    def put(self):
    	return {"datetime": "post verb"}

    def delete(self):
    	return {"datetime": "delete verb"}
    	

class DatetimeList(Resource):
	pass