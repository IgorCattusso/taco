class MeasurementUnitDTO:
    def __init__(self, uuid=None, name='', abbreviation=''):
        self.uuid = uuid
        self.name = name
        self.abbreviation = abbreviation

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            uuid=data_dict.get('uuid', None),
            name=data_dict.get('name', ''),
            abbreviation=data_dict.get('abbreviation', ''),
        )
