class IngredientDTO:
    def __init__(self, uuid=None, name=''):
        self.uuid = uuid
        self.name = name

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            uuid=data_dict.get('uuid', None),
            name=data_dict.get('name', ''),
        )
