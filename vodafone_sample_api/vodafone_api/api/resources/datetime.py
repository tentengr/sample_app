from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from vodafone_api.models import Datetime
from vodafone_api.extensions import ma, db
from vodafone_api.commons.pagination import paginate


class DatetimeSchema(ma.ModelSchema):

    id = ma.Int(dump_only=True)

    class Meta:
        model = Datetime
        sql_session = db.session


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
                  user: DatetimeSchema
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
              DatetimeSchema
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
                  user: DatetimeSchema
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

    method_decorators = [jwt_required]

    def get(self, datetime_id):
        schema = DatetimeSchema()
        datetime = Datetime.query.get_or_404(datetime_id)
        return {"datetime": schema.dump(datetime)}

    def put(self, datetime_id):
        schema = DatetimeSchema(partial=True)
        datetime = Datetime.query.get_or_404(datetime_id)
        datetime = schema.load(request.json, instance=datetime)

        db.session.commit()

        return {"msg": "datetime updated", "datetime": schema.dump(datetime)}

    def delete(self, datetime_id):
        datetime = Datetime.query.get_or_404(datetime_id)
        db.session.delete(datetime)
        db.session.commit()

        return {"msg": "datetime deleted"}


class DatetimeList(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - api
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/DatetimeSchema'
    post:
      tags:
        - api
      requestBody:
        content:
          application/json:
            schema:
              DatetimeSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: datetime created
                  user: DatetimeSchema
    """

    method_decorators = [jwt_required]

    def get(self):
        schema = DatetimeSchema(many=True)
        query = Datetime.query
        return paginate(query, schema)

    def post(self):
        schema = DatetimeSchema()
        datetime = schema.load(request.json)

        db.session.add(datetime)
        db.session.commit()

        return {"msg": "datetime created", "datetime": schema.dump(datetime)}, 201
