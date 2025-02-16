import yaml
import os
import logging

logger = logging.getLogger(__name__)

def load_config():
    """Load the configuration file (_config.yaml)."""
    default_config_path = os.path.join(os.path.dirname(__file__), "_config.yaml")
    config_path = os.getenv("CONFIG_PATH", default_config_path)

    try:
        with open(config_path, "r") as f:
            logger.info(f"Loading config from {config_path}")
            return yaml.safe_load(f)
    except FileNotFoundError:
        logger.warning(f"Config file not found at {config_path}, using defaults.")
        return {"num_times": 1}
