class Counter:
    instances = 0  # Static variable

    def __init__(self):
        Counter.instances += 1

    @staticmethod
    def get_instance_count():
        """Returns the number of instances created."""
        return Counter.instances
