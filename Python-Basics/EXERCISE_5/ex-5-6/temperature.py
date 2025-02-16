class Temperature:
    def __init__(self, celsius: float):
        self._celsius = None
        self.celsius = celsius  # Calls the property setter

    @property
    def celsius(self):
        """Getter for temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter that enforces a valid temperature range."""
        if not (-273.15 <= value <= 5000):
            raise ValueError("Temperature must be between -273.15°C and 5000°C")
        self._celsius = value
