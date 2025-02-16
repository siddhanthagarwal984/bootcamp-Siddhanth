import typer
import logging
from hello.hello import say_hello

app = typer.Typer()

# Disable logging
logging.basicConfig(level=logging.CRITICAL)  # Suppress logs

@app.command()
def greet(names: list[str]):
    """Say hello to multiple people without logging."""
    for name in names:
        print(say_hello(name))

if __name__ == "__main__":
    app()

