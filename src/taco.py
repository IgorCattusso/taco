import sys

from flask import Flask
from injector import Injector
from psycopg2 import pool, OperationalError
from waitress import serve

from src.config import Config
from src.controllers.recipes_controller import RecipesController
from src.controllers.dishes_controller import DishesController
from src.controllers.ingredients_controller import IngredientsController
from src.controllers.measurement_units_controller import MeasurementUnitsController
from src.controllers.nutritional_values_controller import NutritionalValuesController
from src.controllers.preparation_method_controller import PreparationMethodsController
from src.taco_injector_module import TacoModule


sys.path.append('/app')


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
        taco_injector.get(RecipesController),
        taco_injector.get(DishesController),
        taco_injector.get(IngredientsController),
        taco_injector.get(MeasurementUnitsController),
        taco_injector.get(NutritionalValuesController),
        taco_injector.get(PreparationMethodsController),
    ]

    for controller in controllers:
        controller.start_routes()

    return app


if __name__ == "__main__":
    taco_app = create_app()

    serve(taco_app, host='0.0.0.0', port=9000)
