from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from vodafone_api.extensions import apispec
from vodafone_api.api.resources import UserResource, UserList
from vodafone_api.api.resources import DatetimeResource, DatetimeList
from vodafone_api.api.resources.user import UserSchema
from vodafone_api.api.resources.datetime import DatetimeSchema


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)


api.add_resource(UserResource, "/users/<int:user_id>")
api.add_resource(UserList, "/users")

api.add_resource(DatetimeResource, "/datetime/<int:datetime_id>")
api.add_resource(DatetimeList, "/datetime")


@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("UserSchema", schema=UserSchema)
    apispec.spec.path(view=UserResource, app=current_app)
    apispec.spec.path(view=UserList, app=current_app)

    apispec.spec.components.schema("DatetimeSchema", schema=DatetimeSchema)
    apispec.spec.path(view=DatetimeResource, app=current_app)
    apispec.spec.path(view=DatetimeList, app=current_app)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marhsmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
