# Standard Library
from flask import Flask

# Third-Party Libraries
from injector import Module
from psycopg2 import pool

# Configuration and Controllers
from src.config import Config

# Repositories
from src.repository.recipes_repository import RecipesRepository, RecipesRepositoryImpl

# Services

# Use Cases
from src.use_cases.shopping_list_use_cases.generate_shopping_list_use_case import GenerateShoppingListUseCase, GenerateShoppingListUseCaseImpl
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
        binder.bind(RecipesRepository, to=RecipesRepositoryImpl)

        # APIs

        # Use cases
        binder.bind(GenerateShoppingListUseCase, to=GenerateShoppingListUseCaseImpl)
        binder.bind(PrintRecipeUseCase, to=PrintRecipeUseCaseImpl)

        # Controllers
        

        # Other dependencies
        binder.bind(pool.SimpleConnectionPool, to=self.conn_pool)
        binder.bind(Flask, to=self.app)
