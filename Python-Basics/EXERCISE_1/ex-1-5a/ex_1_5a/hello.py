import yaml

def say_hello(name: str) -> str:
    """Load config and return greeting multiple times."""
    with open("_config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    num_times = config.get("num_times", 1)
    
    return "\n".join([f"Hello, {name}!" for _ in range(num_times)])
