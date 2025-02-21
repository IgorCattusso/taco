# Standard Library
from flask import Flask

# Third-Party Libraries
from injector import Module
from psycopg2 import pool

# Configuration
from src.config import Config

# Controllers
from src.controllers.controller import TestController

# Repositories
from src.repository.dishes_repository import DishesRepository, DishesRepositoryImpl
from src.repository.ingredients_repository import IngredientsRepository, IngredientsRepositoryImpl
from src.repository.measurement_units_repository import MeasurementUnitsRepository, MeasurementUnitsRepositoryImpl
from src.repository.nutritional_values_repository import NutritionalValuesRepository, NutritionalValuesRepositoryImpl
from src.repository.preparation_method_repository import PreparationMethodRepository, PreparationMethodRepositoryImpl
from src.repository.recipes_repository import RecipesRepository, RecipesRepositoryImpl

# Services
from src.services.utils.utils import Utils, UtilsImpl

# Use Cases
from src.use_cases.shopping_list_use_cases.generate_shopping_list_use_case import GenerateShoppingListUseCase, \
     GenerateShoppingListUseCaseImpl
from src.use_cases.recipes_use_cases.print_recipe_use_case import PrintRecipeUseCase, PrintRecipeUseCaseImpl


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
        binder.bind(PreparationMethodRepository, to=PreparationMethodRepositoryImpl)
        binder.bind(RecipesRepository, to=RecipesRepositoryImpl)

        # Utility services
        binder.bind(Utils, to=UtilsImpl)

        # Use cases
        binder.bind(GenerateShoppingListUseCase, to=GenerateShoppingListUseCaseImpl)
        binder.bind(PrintRecipeUseCase, to=PrintRecipeUseCaseImpl)

        # Controllers
        binder.bind(TestController, to=TestController)

        # Other dependencies
        binder.bind(pool.SimpleConnectionPool, to=self.conn_pool)
        binder.bind(Flask, to=self.app)
