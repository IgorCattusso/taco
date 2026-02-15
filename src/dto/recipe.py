class RecipeDTO:
    def __init__(self, uuid=None, dish_uuid=None, nutritional_value_uuid=None, quantity=None):
        self.uuid = uuid
        self.dish_uuid = dish_uuid
        self.nutritional_value_uuid = nutritional_value_uuid
        self.quantity = quantity

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            uuid=data_dict.get('uuid', None),
            dish_uuid=data_dict.get('dish_uuid', None),
            nutritional_value_uuid=data_dict.get('nutritional_value_uuid', None),
            quantity=data_dict.get('quantity', None),
        )
