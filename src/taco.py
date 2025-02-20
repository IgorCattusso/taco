import sys

# Third-Party Libraries
from flask import Flask
from injector import Injector
from psycopg2 import pool, OperationalError
from waitress import serve

# Project-specific Modules
from src.config import Config
from src.controllers.controller import TestController
from src.use_cases.shopping_list_use_cases.generate_shopping_list_use_case import GenerateShoppingListUseCase
from src.use_cases.recipes_use_cases.print_recipe_use_case import PrintRecipeUseCase
from src.taco_injector_module import TacoModule


sys.path.append('/app')  # required due to the fact that the app is running inside a docker container


def _get_db_pool():
    taco_config = Config()

    db_params = {
        'host': taco_config.database_host,
        'database': taco_config.database_name,
        'port': taco_config.database_port,
        'user': taco_config.database_user,
        'password': taco_config.database_password
    }
    return pool.SimpleConnectionPool(
        minconn=1,
        maxconn=20,
        **db_params
    )


def _is_connection_pool_working(pool_to_check):
    try:
        conn = pool_to_check.getconn()
        pool_to_check.putconn(conn)
        return True
    except OperationalError:
        return False


def create_app():
    app = Flask(__name__)

    conn_pool = _get_db_pool()

    if not _is_connection_pool_working(conn_pool):
        raise OperationalError("Connection pool is not working")

    taco_injector = Injector(modules=[TacoModule(conn_pool, app)])

    # Create controllers
    controllers = [
        taco_injector.get(TestController),
    ]

    for controller in controllers:
        controller.start_routes()

    return app


if __name__ == "__main__":
    # Create APP
    taco_app = create_app()

    # Start server
    serve(taco_app, host='0.0.0.0', port=9000)
