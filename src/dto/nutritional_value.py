class NutritionalValueDTO:
    def __init__(
            self,
            uuid=None,
            ingredient_uuid=None,
            measurement_unit_uuid=None,
            calories=None,
            fats=None,
            carbohydrates=None,
            proteins=None,
            sodium=None,
            fiber=None
        ):
        self.uuid = uuid
        self.ingredient_uuid = ingredient_uuid
        self.measurement_unit_uuid = measurement_unit_uuid
        self.calories = calories
        self.fats = fats
        self.carbohydrates = carbohydrates
        self.proteins = proteins
        self.sodium = sodium
        self.fiber = fiber

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            uuid=data_dict.get('uuid', None),
            ingredient_uuid=data_dict.get('ingredient_uuid', None),
            measurement_unit_uuid=data_dict.get('measurement_unit_uuid', None),
            calories=data_dict.get('calories', None),
            fats=data_dict.get('fats', None),
            carbohydrates=data_dict.get('carbohydrates', None),
            proteins=data_dict.get('proteins', None),
            sodium=data_dict.get('sodium', None),
            fiber=data_dict.get('fiber', None),
        )
