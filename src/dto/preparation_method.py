class PreparationMethodDTO:
    def __init__(self, uuid=None, dish_uuid=None, preparation_method=''):
        self.uuid = uuid
        self.dish_uuid = dish_uuid
        self.preparation_method = preparation_method

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            uuid=data_dict.get('uuid', None),
            dish_uuid=data_dict.get('dish_uuid', None),
            preparation_method=data_dict.get('preparation_method', ''),
        )
