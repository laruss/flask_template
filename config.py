import logging
import pathlib
from decouple import Config, RepositoryEnv


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

root_path = pathlib.Path(__file__).parent.resolve()
backend_path = root_path / "backend"
frontend_path = root_path / "frontend"
static_path = frontend_path / "static"
css_path = static_path / "css"
js_path = static_path / "js"

env_config = Config(RepositoryEnv(root_path / ".env"))

flask_app_ip = env_config.get("FLASK_APP_IP")
flask_app_port = int(env_config.get("FLASK_APP_PORT"))
flask_app_debug = bool(env_config.get("FLASK_DEBUG"))
