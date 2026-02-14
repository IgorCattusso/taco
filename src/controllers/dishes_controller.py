from flask import Flask, jsonify, request
from injector import inject

from src.use_cases.dishes_use_cases.get_all_dishes_use_case import GetAllDishesUseCase
from src.use_cases.dishes_use_cases.get_dish_use_case import GetDishUseCase
from src.use_cases.dishes_use_cases.create_dish_use_case import CreateDishUseCase
from src.use_cases.dishes_use_cases.update_dish_use_case import UpdateDishUseCase
from src.use_cases.dishes_use_cases.delete_dish_use_case import DeleteDishUseCase
from src.services.utils.utils import Utils
from src.dto.dish import DishDTO


class DishesController:
    @inject
    def __init__(
            self,
            app: Flask,
            utils: Utils,
            get_all_dishes_use_case: GetAllDishesUseCase,
            get_dish_use_case: GetDishUseCase,
            create_dish_use_case: CreateDishUseCase,
            update_dish_use_case: UpdateDishUseCase,
            delete_dish_use_case: DeleteDishUseCase,
        ) -> None:
        self.app = app
        self.utils = utils
        self.get_all_dishes_use_case = get_all_dishes_use_case
        self.get_dish_use_case = get_dish_use_case
        self.create_dish_use_case = create_dish_use_case
        self.update_dish_use_case = update_dish_use_case
        self.delete_dish_use_case = delete_dish_use_case

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/dishes',
            view_func=self.get_all_dishes,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/dishes/<string:dish_uuid>',
            view_func=self.get_dish,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/dishes',
            view_func=self.create_dish,
            methods=['POST']
        )
        self.app.add_url_rule(
            '/taco/dishes/<string:dish_uuid>',
            view_func=self.update_dish,
            methods=['PUT']
        )
        self.app.add_url_rule(
            '/taco/dishes/<string:dish_uuid>',
            view_func=self.delete_dish,
            methods=['DELETE']
        )

    def get_all_dishes(self):
        try:
            dishes = self.get_all_dishes_use_case.execute()

            return jsonify([dish.__dict__ for dish in dishes]), 200

        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def get_dish(self, dish_uuid: str):
        try:
            if self.utils.invalid_uuid(dish_uuid):
                raise ValueError("Field 'uuid' is invalid")

            dish = self.get_dish_use_case.execute(dish_uuid)

            return jsonify(dish.__dict__), 200

        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def create_dish(self):
        try:
            payload = request.get_json()

            dish = DishDTO.from_dict(payload)
            if not getattr(dish, 'name', None):
                raise ValueError("Field 'name' is required")

            return self.create_dish_use_case.execute(dish)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def update_dish(self, dish_uuid: str):
        try:
            payload = request.get_json()

            if self.utils.invalid_uuid(dish_uuid):
                raise ValueError("Field 'uuid' is invalid")

            dish = DishDTO.from_dict(payload)

            if not getattr(dish, 'name', None):
                raise ValueError("Field 'name' is required")

            return self.update_dish_use_case.execute(dish_uuid, dish)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def delete_dish(self, dish_uuid: str):
        try:
            if self.utils.invalid_uuid(dish_uuid):
                raise ValueError("Field 'uuid' is invalid")

            return self.delete_dish_use_case.execute(dish_uuid)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500
