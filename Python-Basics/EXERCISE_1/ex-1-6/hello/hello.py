import logging
from .config_loader import load_config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def say_hello(name: str) -> str:
    """Say hello based on config settings."""
    logger.info(f"Loading configuration for {name}")
    config = load_config()
    num_times = config.get("num_times", 1)

    logger.info(f"Saying hello {num_times} times to {name}")
    return "\n".join([f"Hello, {name}!" for _ in range(num_times)])

if __name__ == "__main__":
    print(say_hello("Alice"))
