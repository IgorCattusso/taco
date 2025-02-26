# Third-Party Libraries
from flask import Flask, jsonify
from injector import inject

# Project-specific Modules
from src.use_cases.preparation_methods_use_case.get_preparation_method_by_dish_uuid_use_case \
    import GetPreparationMethodByDishUuidUseCase
from src.services.utils.utils import Utils


class PreparationMethodsController:
    @inject
    def __init__(
            self,
            app: Flask,
            get_preparation_method_by_dish_uuid_use_case: GetPreparationMethodByDishUuidUseCase,
            utils: Utils,
        ) -> None:
        self.app = app
        self.get_preparation_method_by_dish_uuid_use_case = get_preparation_method_by_dish_uuid_use_case
        self.utils = utils

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/preparation-methods/get-preparation-method/<dish_uuid>',
            view_func=self.get_preparation_method_by_dish_uuid,
            methods=['GET']
        )

    def get_preparation_method_by_dish_uuid(self, dish_uuid: str):
        if self.utils.invalid_uuid(dish_uuid):
            return jsonify({'message': 'Invalid uuid format!'}), 400

        try:
            return self.get_preparation_method_by_dish_uuid_use_case.execute(dish_uuid)
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500
