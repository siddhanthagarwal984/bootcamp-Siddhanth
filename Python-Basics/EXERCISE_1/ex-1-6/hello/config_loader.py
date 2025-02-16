import yaml
import os
import logging

# Configure logging
logger = logging.getLogger(__name__)

def load_config() -> dict:
    """Load configuration from _config.yaml or alternative locations."""
    config_paths = [os.path.join(os.path.dirname(__file__), "_config.yaml")]

    env_config_path = os.getenv("CONFIG_PATH")
    if env_config_path:
        config_paths.extend(env_config_path.split(":"))

    for path in config_paths:
        if os.path.exists(path):
            logger.info(f"Loading config from {path}")
            with open(path, "r") as f:
                return yaml.safe_load(f)

    logger.warning("No config file found, using default settings")
    return {"num_times": 1}  # Default if no config found
