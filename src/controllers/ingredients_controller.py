from flask import Flask, jsonify
from injector import inject

from src.use_cases.ingredients_use_cases.get_all_ingredients_use_case import GetAllIngredientsUseCase


class IngredientsController:
    @inject
    def __init__(self, app: Flask, get_all_ingredients_use_case: GetAllIngredientsUseCase) -> None:
        self.app = app
        self.get_all_ingredients_use_case = get_all_ingredients_use_case

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/ingredients/get-all-ingredients',
            view_func=self.get_all_ingredients,
            methods=['GET']
        )

    def get_all_ingredients(self):
        try:
            return self.get_all_ingredients_use_case.execute()
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500
