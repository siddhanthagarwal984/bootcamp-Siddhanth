import typer
from siddhanth_wf_dynamic.yaml_processor import process_pipeline

app = typer.Typer()

@app.command()
def run_pipeline(input_file: str, yaml_file: str, output_file: str):
    """Runs the transformation pipeline from a YAML config."""
    process_pipeline(input_file, yaml_file, output_file)
    typer.echo(f"Processing completed. Output saved to {output_file}")

if __name__ == "__main__":
    app()
