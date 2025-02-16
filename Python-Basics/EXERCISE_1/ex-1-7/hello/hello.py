import logging
from .config_loader import load_config

logger = logging.getLogger(__name__)

def say_hello(name: str) -> str:
    """Say hello to a person based on the configuration."""
    config = load_config()
    num_times = config.get("num_times", 1)

    logger.info(f"Saying hello {num_times} times to {name}")
    return "\n".join([f"Hello, {name}!" for _ in range(num_times)])
