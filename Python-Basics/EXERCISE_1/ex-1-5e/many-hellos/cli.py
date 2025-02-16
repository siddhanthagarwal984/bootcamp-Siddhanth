import typer
from hello import say_hello

app = typer.Typer()

@app.command()
def greet(names: list[str]):
    for name in names:
        print(say_hello(name))

if __name__ == "__main__":
    app()
