from flask import Flask, jsonify, request
from injector import inject

from src.use_cases.dishes_use_cases.get_all_dishes_use_case import GetAllDishesUseCase
from src.use_cases.dishes_use_cases.create_dish_use_case import CreateDishUseCase
from src.use_cases.dishes_use_cases.update_dish_use_case import UpdateDishUseCase
from src.services.utils.utils import Utils
from src.dto.dish import Dish


class DishesController:
    @inject
    def __init__(
            self,
            app: Flask,
            utils: Utils,
            get_all_dishes_use_case: GetAllDishesUseCase,
            create_dish_use_case: CreateDishUseCase,
            update_dish_use_case: UpdateDishUseCase,
        ) -> None:
        self.app = app
        self.utils = utils
        self.get_all_dishes_use_case = get_all_dishes_use_case
        self.create_dish_use_case = create_dish_use_case
        self.update_dish_use_case = update_dish_use_case

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/dishes/get-all-dishes',
            view_func=self.get_all_dishes,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/dishes/create-dish',
            view_func=self.create_dish,
            methods=['POST']
        )
        self.app.add_url_rule(
            '/taco/dishes/update-dish',
            view_func=self.update_dish,
            methods=['PUT']
        )

    def get_all_dishes(self):
        try:
            return self.get_all_dishes_use_case.execute()
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def create_dish(self):
        try:
            payload = request.get_json()

            dish = Dish.from_dict(payload)
            if not getattr(dish, 'name', None):
                raise ValueError("Field 'name' is required")

            return self.create_dish_use_case.execute(dish)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def update_dish(self):
        try:
            payload = request.get_json()

            dish = Dish.from_dict(payload)
            if not getattr(dish, 'name', None):
                raise ValueError("Field 'name' is required")
            if not getattr(dish, 'uuid', None):
                raise ValueError("Field 'uuid' is required")

            if self.utils.invalid_uuid(str(dish.uuid)):
                raise ValueError("Field 'uuid' is invalid")

            return self.update_dish_use_case.execute(dish)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500
