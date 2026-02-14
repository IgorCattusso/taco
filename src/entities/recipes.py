class Recipe:
    def __init__(self, uuid=None, dish_uuid=None, nutritional_value__uuid=None, quantity=None):
        self.uuid = uuid
        self.dish_uuid = dish_uuid
        self.nutritional_value__uuid = nutritional_value__uuid
        self.quantity = quantity

class RecipeIngredients:
    def __init__(
            self,
            uuid=None,
            dish_uuid=None,
            ingredient_uuid=None,
            measurement_unit_uuid=None,
            dish_name=None,
            ingredient_name=None,
            measurement_unit=None,
            quantity=None,
        ):
        self.uuid=uuid
        self.dish_uuid=dish_uuid
        self.ingredient_uuid=ingredient_uuid
        self.measurement_unit_uuid=measurement_unit_uuid
        self.dish_name=dish_name
        self.ingredient_name=ingredient_name
        self.measurement_unit=measurement_unit
        self.quantity=quantity
