import typer
import logging
from hello.hello import say_hello

app = typer.Typer()

# Set root logger to CRITICAL (disables logs globally)
logging.basicConfig(level=logging.CRITICAL)

# Enable INFO logging **only** for `config_loader`
logging.getLogger("hello.config_loader").setLevel(logging.INFO)

@app.command()
def greet(names: list[str]):
    """Say hello to multiple people, but only log config loading."""
    for name in names:
        print(say_hello(name))

if __name__ == "__main__":
    app()
