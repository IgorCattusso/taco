from flask import Flask, jsonify
from injector import inject

from src.use_cases.dishes_use_cases.get_all_dishes_use_case import GetAllDishesUseCase


class DishesController:
    @inject
    def __init__(
            self,
            app: Flask,
            get_all_dishes_use_case: GetAllDishesUseCase
        ) -> None:
        self.app = app
        self.get_all_dishes_use_case = get_all_dishes_use_case

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/dishes/get-all-dishes',
            view_func=self.get_all_dishes,
            methods=['GET']
        )

    def get_all_dishes(self):
        try:
            return self.get_all_dishes_use_case.execute()
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500
