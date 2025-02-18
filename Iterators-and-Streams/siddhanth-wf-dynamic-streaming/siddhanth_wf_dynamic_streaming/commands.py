import typer
from siddhanth_wf_dynamic_streaming.stream_functions import *
from siddhanth_wf_dynamic_streaming.stream_adapter_functions import *

app = typer.Typer()

@app.command()
def process_stream(input_file: str, output_file: str):
    """Applies a streaming pipeline to process text files."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        lines = infile
        lines = number_the_lines(lines)
        lines = coalesce_empty_lines(lines)
        lines = break_lines(lines)
        for line in lines:
            outfile.write(line + "\n")
    typer.echo(f"Processing completed. Output saved to {output_file}")

if __name__ == "__main__":
    app()
