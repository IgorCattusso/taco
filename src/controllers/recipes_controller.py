from flask import Flask, jsonify
from injector import inject

from src.use_cases.recipes_use_cases.get_recipe_by_dish_uuid_use_case import GetRecipeByDishUuidUseCase
from src.services.utils.utils import Utils


class RecipesController:
    @inject
    def __init__(
            self,
            app: Flask,
            get_recipe_by_dish_uuid_use_case: GetRecipeByDishUuidUseCase,
            utils: Utils,
        ) -> None:
        self.app = app
        self.get_recipe_by_dish_uuid_use_case = get_recipe_by_dish_uuid_use_case
        self.utils = utils

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/recipes/get-recipe/<dish_uuid>',
            view_func=self.get_recipe_by_uuid,
            methods=['GET']
        )

    def get_recipe_by_uuid(self, dish_uuid: str):
        if self.utils.invalid_uuid(dish_uuid):
            return jsonify({'message': 'Invalid uuid format!'}), 400

        try:
            return self.get_recipe_by_dish_uuid_use_case.execute(dish_uuid)
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500
