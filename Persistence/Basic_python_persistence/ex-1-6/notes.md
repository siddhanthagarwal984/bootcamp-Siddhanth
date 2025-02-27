# Notes on YAML Deserialization

## Problem Understanding
This script deserializes a Car object from a YAML string.

## Approach & Methodology
Read the YAML string and convert it back into a Car instance.

## LLMs Used
GPT-4 was used to assist in creating the deserialization logic for the Car object.

## Prompts & Responses
**Prompt:**  
How do I deserialize a YAML string into a Python object?

**Response:**  
Use the `yaml.safe_load()` function to convert a YAML string into a Python dictionary, then create an object from it.

**Prompt:**  
What is the expected output when deserializing the Car object?

**Response:**  
The Car object will be recreated from the YAML string, and its details will be printed.
