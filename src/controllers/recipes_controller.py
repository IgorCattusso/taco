from flask import Flask, jsonify, request
from injector import inject

from src.use_cases.recipes_use_cases.get_all_recipes_use_case import GetAllRecipesUseCase
from src.use_cases.recipes_use_cases.get_recipe_use_case import GetRecipeUseCase
from src.use_cases.recipes_use_cases.get_recipe_by_dish_uuid_use_case import GetRecipeByDishUuidUseCase
from src.use_cases.recipes_use_cases.create_recipe_use_case import CreateRecipeUseCase
from src.use_cases.recipes_use_cases.update_recipe_use_case import UpdateRecipeUseCase
from src.use_cases.recipes_use_cases.delete_recipe_use_case import DeleteRecipeUseCase
from src.services.utils.utils import Utils
from src.dto.recipe import RecipeDTO


class RecipesController:
    @inject
    def __init__(
            self,
            app: Flask,
            utils: Utils,
            get_all_recipes_use_case: GetAllRecipesUseCase,
            get_recipe_use_case: GetRecipeUseCase,
            get_recipe_by_dish_uuid_use_case: GetRecipeByDishUuidUseCase,
            create_recipe_use_case: CreateRecipeUseCase,
            update_recipe_use_case: UpdateRecipeUseCase,
            delete_recipe_use_case: DeleteRecipeUseCase,
        ) -> None:
        self.app = app
        self.utils = utils
        self.get_all_recipes_use_case = get_all_recipes_use_case
        self.get_recipe_use_case = get_recipe_use_case
        self.get_recipe_by_dish_uuid_use_case = get_recipe_by_dish_uuid_use_case
        self.create_recipe_use_case = create_recipe_use_case
        self.update_recipe_use_case = update_recipe_use_case
        self.delete_recipe_use_case = delete_recipe_use_case

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/recipes',
            view_func=self.get_all_recipes,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/recipes/<string:recipe_uuid>',
            view_func=self.get_recipe,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/recipes/by-dish/<string:dish_uuid>',
            view_func=self.get_recipe_by_dish_uuid,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/recipes',
            view_func=self.create_recipe,
            methods=['POST']
        )
        self.app.add_url_rule(
            '/taco/recipes/<string:recipe_uuid>',
            view_func=self.update_recipe,
            methods=['PUT']
        )
        self.app.add_url_rule(
            '/taco/recipes/<string:recipe_uuid>',
            view_func=self.delete_recipe,
            methods=['DELETE']
        )

    def get_all_recipes(self):
        try:
            recipes = self.get_all_recipes_use_case.execute()

            return jsonify([recipe.__dict__ for recipe in recipes]), 200

        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def get_recipe(self, recipe_uuid: str):
        try:
            if self.utils.invalid_uuid(recipe_uuid):
                raise ValueError("Field 'uuid' is invalid")

            recipe = self.get_recipe_use_case.execute(recipe_uuid)

            return jsonify(recipe.__dict__), 200

        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def get_recipe_by_dish_uuid(self, dish_uuid: str):
        if self.utils.invalid_uuid(dish_uuid):
            return jsonify({'message': 'Invalid uuid format!'}), 400

        try:
            return self.get_recipe_by_dish_uuid_use_case.execute(dish_uuid)
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def create_recipe(self):
        try:
            payload = request.get_json()

            recipe = RecipeDTO.from_dict(payload)
            if not getattr(recipe, 'dish_uuid', None):
                raise ValueError("Field 'dish_uuid' is required")
            if not getattr(recipe, 'nutritional_value_uuid', None):
                raise ValueError("Field 'nutritional_value_uuid' is required")
            if not getattr(recipe, 'quantity', None):
                raise ValueError("Field 'quantity' is required")

            return self.create_recipe_use_case.execute(recipe)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def update_recipe(self, recipe_uuid: str):
        try:
            payload = request.get_json()

            if self.utils.invalid_uuid(recipe_uuid):
                raise ValueError("Field 'uuid' is invalid")

            recipe = RecipeDTO.from_dict(payload)

            if not getattr(recipe, 'dish_uuid', None):
                raise ValueError("Field 'dish_uuid' is required")
            if not getattr(recipe, 'nutritional_value_uuid', None):
                raise ValueError("Field 'nutritional_value_uuid' is required")
            if not getattr(recipe, 'quantity', None):
                raise ValueError("Field 'quantity' is required")

            return self.update_recipe_use_case.execute(recipe_uuid, recipe)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def delete_recipe(self, recipe_uuid: str):
        try:
            if self.utils.invalid_uuid(recipe_uuid):
                raise ValueError("Field 'uuid' is invalid")

            return self.delete_recipe_use_case.execute(recipe_uuid)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500
