from flask import Flask, jsonify, request
from injector import inject

from src.use_cases.nutritional_values_use_cases.get_all_nutritional_values_use_case import GetAllNutritionalValuesUseCase
from src.use_cases.nutritional_values_use_cases.get_nutritional_value_use_case import GetNutritionalValueUseCase
from src.use_cases.nutritional_values_use_cases.create_nutritional_value_use_case import CreateNutritionalValueUseCase
from src.use_cases.nutritional_values_use_cases.update_nutritional_value_use_case import UpdateNutritionalValueUseCase
from src.use_cases.nutritional_values_use_cases.delete_nutritional_value_use_case import DeleteNutritionalValueUseCase
from src.services.utils.utils import Utils
from src.dto.nutritional_value import NutritionalValueDTO


class NutritionalValuesController:
    @inject
    def __init__(
            self,
            app: Flask,
            utils: Utils,
            get_all_nutritional_values_use_case: GetAllNutritionalValuesUseCase,
            get_nutritional_value_use_case: GetNutritionalValueUseCase,
            create_nutritional_value_use_case: CreateNutritionalValueUseCase,
            update_nutritional_value_use_case: UpdateNutritionalValueUseCase,
            delete_nutritional_value_use_case: DeleteNutritionalValueUseCase,
        ) -> None:
        self.app = app
        self.utils = utils
        self.get_all_nutritional_values_use_case = get_all_nutritional_values_use_case
        self.get_nutritional_value_use_case = get_nutritional_value_use_case
        self.create_nutritional_value_use_case = create_nutritional_value_use_case
        self.update_nutritional_value_use_case = update_nutritional_value_use_case
        self.delete_nutritional_value_use_case = delete_nutritional_value_use_case

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/nutritional-values',
            view_func=self.get_all_nutritional_values,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/nutritional-values/<string:nutritional_value_uuid>',
            view_func=self.get_nutritional_value,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/nutritional-values',
            view_func=self.create_nutritional_value,
            methods=['POST']
        )
        self.app.add_url_rule(
            '/taco/nutritional-values/<string:nutritional_value_uuid>',
            view_func=self.update_nutritional_value,
            methods=['PUT']
        )
        self.app.add_url_rule(
            '/taco/nutritional-values/<string:nutritional_value_uuid>',
            view_func=self.delete_nutritional_value,
            methods=['DELETE']
        )

    def get_all_nutritional_values(self):
        try:
            nutritional_values = self.get_all_nutritional_values_use_case.execute()

            return jsonify([nutritional_value.__dict__ for nutritional_value in nutritional_values]), 200

        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def get_nutritional_value(self, nutritional_value_uuid: str):
        try:
            if self.utils.invalid_uuid(nutritional_value_uuid):
                raise ValueError("Field 'uuid' is invalid")

            nutritional_value = self.get_nutritional_value_use_case.execute(nutritional_value_uuid)

            return jsonify(nutritional_value.__dict__), 200

        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def create_nutritional_value(self):
        try:
            payload = request.get_json()

            nutritional_value = NutritionalValueDTO.from_dict(payload)
            if not getattr(nutritional_value, 'ingredient_uuid', None):
                raise ValueError("Field 'ingredient_uuid' is required")
            if not getattr(nutritional_value, 'measurement_unit_uuid', None):
                raise ValueError("Field 'measurement_unit_uuid' is required")

            return self.create_nutritional_value_use_case.execute(nutritional_value)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def update_nutritional_value(self, nutritional_value_uuid: str):
        try:
            payload = request.get_json()

            if self.utils.invalid_uuid(nutritional_value_uuid):
                raise ValueError("Field 'uuid' is invalid")

            nutritional_value = NutritionalValueDTO.from_dict(payload)

            if not getattr(nutritional_value, 'ingredient_uuid', None):
                raise ValueError("Field 'ingredient_uuid' is required")
            if not getattr(nutritional_value, 'measurement_unit_uuid', None):
                raise ValueError("Field 'measurement_unit_uuid' is required")

            return self.update_nutritional_value_use_case.execute(nutritional_value_uuid, nutritional_value)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def delete_nutritional_value(self, nutritional_value_uuid: str):
        try:
            if self.utils.invalid_uuid(nutritional_value_uuid):
                raise ValueError("Field 'uuid' is invalid")

            return self.delete_nutritional_value_use_case.execute(nutritional_value_uuid)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500
