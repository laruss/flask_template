from flask import Blueprint

from backend.helpers.utils import success_response

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/", methods=["GET"])
def index():
    return success_response()
