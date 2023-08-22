import json
from typing import Union

import flask


def _response(
    data: dict, status: int = 200, mimetype: str = "application/json"
) -> flask.Response:
    return flask.Response(json.dumps(data), status=status, mimetype=mimetype)


def not_found_response(data: dict = None) -> flask.Response:
    data = data or {"error": "item not found"}

    return _response(data, status=404)


def internal_error_response(data: dict = None) -> flask.Response:
    data = data or {"error": "internal server error"}

    return _response(data, status=500)


def success_response(
    data: Union[dict, list] = None, message: str = None
) -> flask.Response:
    data = {"message": message} if message else (data or {"success": True})

    return _response(data)
