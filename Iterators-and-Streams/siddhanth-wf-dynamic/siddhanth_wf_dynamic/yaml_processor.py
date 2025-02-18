import yaml
from siddhanth_wf_dynamic.processing_functions import *

FUNCTION_MAP = {
    "lowercase": lower_case,
    "remove_stop_words": remove_stop_words,
    "uk_to_us": uk_to_us,
    "upper_case": upper_case
}

def process_pipeline(input_file, yaml_file, output_file):
    with open(yaml_file, 'r') as f:
        config = yaml.safe_load(f)

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            for func_name in config["pipeline"]:
                line = FUNCTION_MAP[func_name](line)
            outfile.write(line + "\n")
