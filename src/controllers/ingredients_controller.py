from flask import Flask, jsonify, request
from injector import inject

from src.services.utils.utils import Utils
from src.dto.ingredient import IngredientDTO
from src.use_cases.ingredients_use_cases.get_all_ingredients_use_case import GetAllIngredientsUseCase
from src.use_cases.ingredients_use_cases.get_ingredient_use_case import GetIngredientUseCase
from src.use_cases.ingredients_use_cases.create_ingredient_use_case import CreateIngredientUseCase
from src.use_cases.ingredients_use_cases.update_ingredient_use_case import UpdateIngredientUseCase
from src.use_cases.ingredients_use_cases.delete_ingredient_use_case import DeleteIngredientUseCase


class IngredientsController:
    @inject
    def __init__(
            self,
            app:Flask,
            utils: Utils,
            get_all_ingredients_use_case: GetAllIngredientsUseCase,
            get_ingredient_use_case: GetIngredientUseCase,
            create_ingredient_use_case: CreateIngredientUseCase,
            update_ingredient_use_case: UpdateIngredientUseCase,
            delete_ingredient_use_case: DeleteIngredientUseCase,
        ) -> None:
        self.app = app
        self.utils = utils
        self.get_all_ingredients_use_case = get_all_ingredients_use_case
        self.get_ingredient_use_case = get_ingredient_use_case
        self.create_ingredient_use_case = create_ingredient_use_case
        self.update_ingredient_use_case = update_ingredient_use_case
        self.delete_ingredient_use_case = delete_ingredient_use_case

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/ingredients',
            view_func=self.get_all_ingredients,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/ingredients/<string:ingredient_uuid>',
            view_func=self.get_ingredient,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/ingredients',
            view_func=self.create_ingredient,
            methods=['POST']
        )
        self.app.add_url_rule(
            '/taco/ingredients/<string:ingredient_uuid>',
            view_func=self.update_ingredient,
            methods=['PUT']
        )
        self.app.add_url_rule(
            '/taco/ingredients/<string:ingredient_uuid>',
            view_func=self.delete_ingredient,
            methods=['DELETE']
        )

    def get_all_ingredients(self):
        try:
            ingredients = self.get_all_ingredients_use_case.execute()

            return jsonify([ingredient.__dict__ for ingredient in ingredients]), 200

        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def get_ingredient(self, ingredient_uuid: str):
        try:
            if self.utils.invalid_uuid(ingredient_uuid):
                raise ValueError("Field 'uuid' is invalid")

            ingredient = self.get_ingredient_use_case.execute(ingredient_uuid)

            return jsonify(ingredient.__dict__), 200

        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def create_ingredient(self):
        try:
            payload = request.get_json()

            ingredient = IngredientDTO.from_dict(payload)
            if not getattr(ingredient, 'name', None):
                raise ValueError("Field 'name' is required")

            return self.create_ingredient_use_case.execute(ingredient)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def update_ingredient(self, ingredient_uuid: str):
        try:
            payload = request.get_json()

            if self.utils.invalid_uuid(ingredient_uuid):
                raise ValueError("Field 'uuid' is invalid")

            ingredient = IngredientDTO.from_dict(payload)

            if not getattr(ingredient, 'name', None):
                raise ValueError("Field 'name' is required")

            return self.update_ingredient_use_case.execute(ingredient_uuid, ingredient)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def delete_ingredient(self, ingredient_uuid: str):
        try:
            if self.utils.invalid_uuid(ingredient_uuid):
                raise ValueError("Field 'uuid' is invalid")

            return self.delete_ingredient_use_case.execute(ingredient_uuid)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500
