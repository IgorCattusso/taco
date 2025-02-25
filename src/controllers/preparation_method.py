# Third-Party Libraries
from flask import Flask, jsonify
from injector import inject

# Project-specific Modules
from src.use_cases.preparation_methods_use_case.get_preparation_method_by_dish_uuid_use_case \
    import GetPreparationMethodByDishUuidUseCase


class PreparationMethodsController:
    @inject
    def __init__(
            self,
            app: Flask,
            get_preparation_method_by_dish_uuid_use_case: GetPreparationMethodByDishUuidUseCase
        ) -> None:
        self.app = app
        self.get_preparation_method_by_dish_uuid_use_case = get_preparation_method_by_dish_uuid_use_case

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/preparation-methods/get-preparation-method/<dish_uuid>',
            view_func=self.get_preparation_method_by_uuid,
            methods=['GET']
        )

    def get_preparation_method_by_uuid(self, dish_uuid: str):
        try:
            return self.get_preparation_method_by_dish_uuid_use_case.execute(dish_uuid)

        except Exception as e:
            return jsonify({'message': str(e)}), 500
