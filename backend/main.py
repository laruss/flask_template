import logging

import flask
from flask import send_from_directory
from flask_cors import CORS

import config
from backend.helpers.utils import internal_error_response
from backend.routes.api import api_bp

app = flask.Flask(__name__)
CORS(app)

app.register_blueprint(api_bp)

logger = logging.getLogger(__name__)

error_handler = Exception if config.flask_app_debug else 500


@app.route("/static/css/<path:path>")
def send_css(path):
    return send_from_directory(f"{config.css_path}", path)


@app.route("/static/js/<path:path>")
def send_js(path):
    return send_from_directory(f"{config.js_path}", path)


@app.errorhandler(404)
def page_not_found(e):
    return flask.jsonify({"error": "route not found"}), 404


@app.errorhandler(error_handler)
def internal_server_error(e):
    logger.warning(f"Internal server error: {type(e)} {e}")
    return internal_error_response({"error": str(e)})


if __name__ == "__main__":
    app.run(
        debug=config.flask_app_debug,
        host=config.flask_app_ip,
        port=config.flask_app_port
    )
