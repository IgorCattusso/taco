# Standard Library
from flask import Flask

# Third-Party Libraries
from injector import Module
from psycopg2 import pool

# Configuration
from src.config import Config

# Controllers
from src.controllers.dishes_controller import DishesController
from src.controllers.recipes_controller import RecipesController
from src.controllers.ingredients_controller import IngredientsController
from src.controllers.measurement_units_controller import MeasurementUnitsController
from src.controllers.preparation_method import PreparationMethodsController

# Repositories
from src.repository.dishes_repository import DishesRepository, DishesRepositoryImpl
from src.repository.ingredients_repository import IngredientsRepository, IngredientsRepositoryImpl
from src.repository.measurement_units_repository import MeasurementUnitsRepository, MeasurementUnitsRepositoryImpl
from src.repository.nutritional_values_repository import NutritionalValuesRepository, NutritionalValuesRepositoryImpl
from src.repository.preparation_method_repository import PreparationMethodsRepository, PreparationMethodsRepositoryImpl
from src.repository.recipes_repository import RecipesRepository, RecipesRepositoryImpl

# Services
from src.services.utils.utils import Utils, UtilsImpl

# Use Cases
from src.use_cases.shopping_list_use_cases.generate_shopping_list_use_case import GenerateShoppingListUseCase, \
    GenerateShoppingListUseCaseImpl
from src.use_cases.recipes_use_cases.get_recipe_by_dish_uuid_use_case import GetRecipeByDishUuidUseCase, \
    GetRecipeByDishUuidUseCaseImpl
from src.use_cases.dishes_use_cases.get_all_dishes_use_case import GetAllDishesUseCase, GetAllDishesUseCaseImpl
from src.use_cases.ingredients_use_cases.get_all_ingredients_use_case import GetAllIngredientsUseCase, \
    GetAllIngredientsUseCaseImpl
from src.use_cases.measurement_units_use_cases.get_all_measurement_units_use_case import \
    GetAllMeasurementUnitsUseCase, GetAllMeasurementUnitsUseCaseImpl
from src.use_cases.preparation_methods_use_case.get_preparation_method_by_dish_uuid_use_case import \
    GetPreparationMethodByDishUuidUseCase, GetPreparationMethodByDishUuidUseCaseImpl
from src.use_cases.preparation_methods_use_case.delete_preparation_method_use_case import \
    DeletePreparationMethodUseCase, DeletePreparationMethodhUseCaseImpl
from src.use_cases.dishes_use_cases.create_dish_use_case import CreateDishUseCase, CreateDishUseCaseImpl
from src.use_cases.dishes_use_cases.update_dish_use_case import UpdateDishUseCase, UpdateDishUseCaseImpl
from src.use_cases.dishes_use_cases.get_dish_use_case import GetDishUseCase, GetDishUseCaseImpl
from src.use_cases.dishes_use_cases.delete_dish_use_case import DeleteDishUseCase, DeleteDishUseCaseImpl


class TacoModule(Module):
    """
    Dependency injection module for Taco
    """

    def __init__(self, conn_pool: pool.SimpleConnectionPool, app: Flask):
        self.conn_pool = conn_pool
        self.app = app

    def configure(self, binder):
        # Configuration
        binder.bind(Config, to=Config)

        # Database repositories
        binder.bind(DishesRepository, to=DishesRepositoryImpl)
        binder.bind(IngredientsRepository, to=IngredientsRepositoryImpl)
        binder.bind(MeasurementUnitsRepository, to=MeasurementUnitsRepositoryImpl)
        binder.bind(NutritionalValuesRepository, to=NutritionalValuesRepositoryImpl)
        binder.bind(PreparationMethodsRepository, to=PreparationMethodsRepositoryImpl)
        binder.bind(RecipesRepository, to=RecipesRepositoryImpl)

        # Utility services
        binder.bind(Utils, to=UtilsImpl)

        # Use cases
        binder.bind(GenerateShoppingListUseCase, to=GenerateShoppingListUseCaseImpl)
        binder.bind(GetRecipeByDishUuidUseCase, to=GetRecipeByDishUuidUseCaseImpl)
        binder.bind(GetAllDishesUseCase, to=GetAllDishesUseCaseImpl)
        binder.bind(GetAllIngredientsUseCase, to=GetAllIngredientsUseCaseImpl)
        binder.bind(GetAllMeasurementUnitsUseCase, to=GetAllMeasurementUnitsUseCaseImpl)
        binder.bind(GetPreparationMethodByDishUuidUseCase, to=GetPreparationMethodByDishUuidUseCaseImpl)
        binder.bind(DeletePreparationMethodUseCase, to=DeletePreparationMethodhUseCaseImpl)
        binder.bind(CreateDishUseCase, to=CreateDishUseCaseImpl)
        binder.bind(UpdateDishUseCase, to=UpdateDishUseCaseImpl)
        binder.bind(GetDishUseCase, to=GetDishUseCaseImpl)
        binder.bind(DeleteDishUseCase, to=DeleteDishUseCaseImpl)

        # Controllers
        binder.bind(DishesController, to=DishesController)
        binder.bind(RecipesController, to=RecipesController)
        binder.bind(IngredientsController, to=IngredientsController)
        binder.bind(MeasurementUnitsController, to=MeasurementUnitsController)
        binder.bind(PreparationMethodsController, to=PreparationMethodsController)

        # Other dependencies
        binder.bind(pool.SimpleConnectionPool, to=self.conn_pool)
        binder.bind(Flask, to=self.app)
