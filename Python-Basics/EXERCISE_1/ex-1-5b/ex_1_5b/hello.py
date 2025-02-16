import yaml
import os

def load_config():
    """Load config from current directory, then CONFIG_PATH, else default."""
    paths = ["_config.yaml"]
    
    env_paths = os.getenv("CONFIG_PATH")
    if env_paths:
        paths.extend(env_paths.split(":"))
    
    for path in paths:
        if os.path.exists(path):
            with open(path, "r") as f:
                return yaml.safe_load(f)
    
    return {"num_times": 1}  # Default config

def say_hello(name: str) -> str:
    config = load_config()
    num_times = config.get("num_times", 1)
    return "\n".join([f"Hello, {name}!" for _ in range(num_times)])
