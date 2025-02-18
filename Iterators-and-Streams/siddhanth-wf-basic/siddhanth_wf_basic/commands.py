import typer
from siddhanth_wf_basic import processing_functions

app = typer.Typer()

@app.command()
def upper_case(input_file: str, output_file: str = None):
    processing_functions.upper_case(input_file, output_file)

@app.command()
def lower_case(input_file: str, output_file: str = None):
    processing_functions.lower_case(input_file, output_file)

if __name__ == "__main__":
    app()
