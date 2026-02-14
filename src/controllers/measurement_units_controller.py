from flask import Flask, jsonify
from injector import inject

from src.use_cases.measurement_units_use_cases.get_all_measurement_units_use_case import GetAllMeasurementUnitsUseCase


class MeasurementUnitsController:
    @inject
    def __init__(
            self,
            app: Flask,
            get_all_measurement_units_use_case: GetAllMeasurementUnitsUseCase
        ) -> None:
        self.app = app
        self.get_all_measurement_units_use_case = get_all_measurement_units_use_case

    def start_routes(self):
        self.app.add_url_rule(
            '/taco/measurement-units/get-all-measurement-units',
            view_func=self.get_all_measurement_units,
            methods=['GET']
        )

    def get_all_measurement_units(self):
        try:
            return self.get_all_measurement_units_use_case.execute()
        except ValueError as e:
            return jsonify({'message': str(e)}), 404
        except RuntimeError as e:
            return jsonify({'message': str(e)}), 500
