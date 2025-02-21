# Third-Party Libraries
from flask import Flask, request, jsonify
from injector import inject

# Project-specific Modules
from src.use_cases.recipes_use_cases.get_recipe_use_case import GetRecipeUseCase


class TestController:
    @inject
    def __init__(
            self,
            app: Flask,
            get_recipe_use_case: GetRecipeUseCase
    ) -> None:
        self.app = app
        self.print_recipe_use_case = get_recipe_use_case

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/recipes/get-recipe/<recipe_uuid>',
            view_func=self.get_recipe_by_uuid,
            methods=['GET']
        )

    def get_recipe_by_uuid(self, recipe_uuid: str):
        try:
            return self.print_recipe_use_case.execute(recipe_uuid)

        except Exception as e:
            return jsonify({'message': str(e)}), 500
