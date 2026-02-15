from flask import Flask, jsonify, request
from injector import inject

from src.use_cases.measurement_units_use_cases.get_all_measurement_units_use_case import GetAllMeasurementUnitsUseCase
from src.use_cases.measurement_units_use_cases.get_measurement_unit_use_case import GetMeasurementUnitUseCase
from src.use_cases.measurement_units_use_cases.create_measurement_unit_use_case import CreateMeasurementUnitUseCase
from src.use_cases.measurement_units_use_cases.update_measurement_unit_use_case import UpdateMeasurementUnitUseCase
from src.use_cases.measurement_units_use_cases.delete_measurement_unit_use_case import DeleteMeasurementUnitUseCase
from src.services.utils.utils import Utils
from src.dto.measurement_unit import MeasurementUnitDTO


class MeasurementUnitsController:
    @inject
    def __init__(
            self,
            app: Flask,
            utils: Utils,
            get_all_measurement_units_use_case: GetAllMeasurementUnitsUseCase,
            get_measurement_unit_use_case: GetMeasurementUnitUseCase,
            create_measurement_unit_use_case: CreateMeasurementUnitUseCase,
            update_measurement_unit_use_case: UpdateMeasurementUnitUseCase,
            delete_measurement_unit_use_case: DeleteMeasurementUnitUseCase,
        ) -> None:
        self.app = app
        self.utils = utils
        self.get_all_measurement_units_use_case = get_all_measurement_units_use_case
        self.get_measurement_unit_use_case = get_measurement_unit_use_case
        self.create_measurement_unit_use_case = create_measurement_unit_use_case
        self.update_measurement_unit_use_case = update_measurement_unit_use_case
        self.delete_measurement_unit_use_case = delete_measurement_unit_use_case

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/measurement-units',
            view_func=self.get_all_measurement_units,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/measurement-units/<string:measurement_unit_uuid>',
            view_func=self.get_measurement_unit,
            methods=['GET']
        )
        self.app.add_url_rule(
            '/taco/measurement-units',
            view_func=self.create_measurement_unit,
            methods=['POST']
        )
        self.app.add_url_rule(
            '/taco/measurement-units/<string:measurement_unit_uuid>',
            view_func=self.update_measurement_unit,
            methods=['PUT']
        )
        self.app.add_url_rule(
            '/taco/measurement-units/<string:measurement_unit_uuid>',
            view_func=self.delete_measurement_unit,
            methods=['DELETE']
        )

    def get_all_measurement_units(self):
        try:
            measurement_units = self.get_all_measurement_units_use_case.execute()

            return jsonify([measurement_unit.__dict__ for measurement_unit in measurement_units]), 200

        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def get_measurement_unit(self, measurement_unit_uuid: str):
        try:
            if self.utils.invalid_uuid(measurement_unit_uuid):
                raise ValueError("Field 'uuid' is invalid")

            measurement_unit = self.get_measurement_unit_use_case.execute(measurement_unit_uuid)

            return jsonify(measurement_unit.__dict__), 200

        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def create_measurement_unit(self):
        try:
            payload = request.get_json()

            measurement_unit = MeasurementUnitDTO.from_dict(payload)
            if not getattr(measurement_unit, 'name', None):
                raise ValueError("Field 'name' is required")
            if not getattr(measurement_unit, 'abbreviation', None):
                raise ValueError("Field 'abbreviation' is required")

            return self.create_measurement_unit_use_case.execute(measurement_unit)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def update_measurement_unit(self, measurement_unit_uuid: str):
        try:
            payload = request.get_json()

            if self.utils.invalid_uuid(measurement_unit_uuid):
                raise ValueError("Field 'uuid' is invalid")

            measurement_unit = MeasurementUnitDTO.from_dict(payload)

            if not getattr(measurement_unit, 'name', None):
                raise ValueError("Field 'name' is required")
            if not getattr(measurement_unit, 'abbreviation', None):
                raise ValueError("Field 'abbreviation' is required")

            return self.update_measurement_unit_use_case.execute(measurement_unit_uuid, measurement_unit)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500

    def delete_measurement_unit(self, measurement_unit_uuid: str):
        try:
            if self.utils.invalid_uuid(measurement_unit_uuid):
                raise ValueError("Field 'uuid' is invalid")

            return self.delete_measurement_unit_use_case.execute(measurement_unit_uuid)

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500
