from config_loader import load_config

def say_hello(name: str) -> str:
    """Say hello based on config settings."""
    num_times = load_config().get("num_times", 1)  # Get num_times from config
    return "\n".join([f"Hello, {name}!" for _ in range(num_times)])

if __name__ == "__main__":
    print(say_hello("Alice"))
