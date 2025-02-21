class NutritionalValues:
    def __init__(
            self,
            uuid=None,
            ingredient_uuid=None,
            measurement_unit_uuid=None,
            calories=None, fats=None,
            carbohydrates=None,
            proteins=None,
            sodium=None,
            fiber=None,
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
