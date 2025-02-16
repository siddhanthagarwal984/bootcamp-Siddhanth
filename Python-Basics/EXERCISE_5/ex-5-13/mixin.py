import json

class JsonMixin:
    """A mixin that provides JSON serialization and deserialization."""

    def to_json(self):
        """Serializes the object to a JSON string."""
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        """Deserializes a JSON string to an object."""
        data = json.loads(json_str)
        return cls(**data)
