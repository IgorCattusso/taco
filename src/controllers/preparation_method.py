from flask import Flask, jsonify, request
from injector import inject

from src.use_cases.preparation_methods_use_case.get_all_preparation_methods_use_case import \
    GetAllPreparationMethodsUseCase
from src.use_cases.preparation_methods_use_case.get_preparation_method_use_case import GetPreparationMethodUseCase
from src.use_cases.preparation_methods_use_case.get_preparation_method_by_dish_uuid_use_case import \
    GetPreparationMethodByDishUuidUseCase
from src.use_cases.preparation_methods_use_case.create_preparation_method_use_case import CreatePreparationMethodUseCase
from src.use_cases.preparation_methods_use_case.update_preparation_method_use_case import UpdatePreparationMethodUseCase
from src.use_cases.preparation_methods_use_case.delete_preparation_method_use_case import DeletePreparationMethodUseCase
from src.services.utils.utils import Utils
from src.dto.preparation_method import PreparationMethodDTO


class PreparationMethodsController:
    @inject
    def __init__(
            self,
            app: Flask,
            utils: Utils,
            get_all_preparation_methods_use_case: GetAllPreparationMethodsUseCase,
            get_preparation_method_use_case: GetPreparationMethodUseCase,
            get_preparation_method_by_dish_uuid_use_case: GetPreparationMethodByDishUuidUseCase,
            create_preparation_method_use_case: CreatePreparationMethodUseCase,
            update_preparation_method_use_case: UpdatePreparationMethodUseCase,
            delete_preparation_method_use_case: DeletePreparationMethodUseCase,
        ) -> None:
        self.app = app
        self.utils = utils
        self.get_all_preparation_methods_use_case = get_all_preparation_methods_use_case
        self.get_preparation_method_use_case = get_preparation_method_use_case
        self.get_preparation_method_by_dish_uuid_use_case = get_preparation_method_by_dish_uuid_use_case
        self.create_preparation_method_use_case = create_preparation_method_use_case
        self.update_preparation_method_use_case = update_preparation_method_use_case
        self.delete_preparation_method_use_case = delete_preparation_method_use_case

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/preparation-methods',
            view_func=self.get_all_preparation_methods,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/preparation-methods/<string:preparation_method_uuid>',
            view_func=self.get_preparation_method,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/preparation-methods/by-dish/<string:dish_uuid>',
            view_func=self.get_preparation_method_by_dish_uuid,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/preparation-methods',
            view_func=self.create_preparation_method,
            methods=['POST']
        )
        self.app.add_url_rule(
            '/taco/preparation-methods/<string:preparation_method_uuid>',
            view_func=self.update_preparation_method,
            methods=['PUT']
        )
        self.app.add_url_rule(
            '/taco/preparation-methods/<string:preparation_method_uuid>',
            view_func=self.delete_preparation_method,
            methods=['DELETE']
        )

    def get_all_preparation_methods(self):
        try:
            preparation_methods = self.get_all_preparation_methods_use_case.execute()

            return jsonify([preparation_method.__dict__ for preparation_method in preparation_methods]), 200

        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def get_preparation_method(self, preparation_method_uuid: str):
        try:
            if self.utils.invalid_uuid(preparation_method_uuid):
                raise ValueError("Field 'uuid' is invalid")

            preparation_method = self.get_preparation_method_use_case.execute(preparation_method_uuid)

            return jsonify(preparation_method.__dict__), 200

        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def get_preparation_method_by_dish_uuid(self, dish_uuid: str):
        try:
            if self.utils.invalid_uuid(dish_uuid):
                return jsonify({'message': 'Invalid uuid format!'}), 400

            return self.get_preparation_method_by_dish_uuid_use_case.execute(dish_uuid)
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def create_preparation_method(self):
        try:
            payload = request.get_json()

            preparation_method = PreparationMethodDTO.from_dict(payload)
            if not getattr(preparation_method, 'dish_uuid', None):
                raise ValueError("Field 'dish_uuid' is required")
            if not getattr(preparation_method, 'preparation_method', None):
                raise ValueError("Field 'preparation_method' is required")

            return self.create_preparation_method_use_case.execute(preparation_method)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def update_preparation_method(self, preparation_method_uuid: str):
        try:
            payload = request.get_json()

            if self.utils.invalid_uuid(preparation_method_uuid):
                raise ValueError("Field 'uuid' is invalid")

            preparation_method = PreparationMethodDTO.from_dict(payload)

            if not getattr(preparation_method, 'dish_uuid', None):
                raise ValueError("Field 'dish_uuid' is required")
            if not getattr(preparation_method, 'preparation_method', None):
                raise ValueError("Field 'preparation_method' is required")

            return self.update_preparation_method_use_case.execute(preparation_method_uuid, preparation_method)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def delete_preparation_method(self, preparation_method_uuid: str):
        try:
            if self.utils.invalid_uuid(preparation_method_uuid):
                raise ValueError("Field 'uuid' is invalid")

            return self.delete_preparation_method_use_case.execute(preparation_method_uuid)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500
