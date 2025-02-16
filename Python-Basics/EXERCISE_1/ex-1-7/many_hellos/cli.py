import typer
import logging
from hello.hello import say_hello

app = typer.Typer()

# Enable logging
logging.basicConfig(level=logging.INFO)

@app.command()
def greet(names: list[str]):
    """Say hello to multiple people with logging enabled."""
    for name in names:
        print(say_hello(name))

if __name__ == "__main__":
    app()
