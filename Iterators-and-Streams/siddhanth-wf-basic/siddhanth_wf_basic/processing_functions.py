import os
import requests
import re

def upper_case(input_file, output_file=None):
    if output_file is None:
        output_file = input_file + ".processed"
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(line.upper())

def lower_case(input_file, output_file=None):
    if output_file is None:
        output_file = input_file + ".processed"

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(line.lower())

STOP_WORDS = {"a", "an", "the", "and", "or"}

def remove_stop_words(text):
    words = text.split()
    return " ".join(word for word in words if word.lower() not in STOP_WORDS)

def capitalize(text):
    return text.title()

def fetch_geo_ip(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/geo")
    data = response.json()
    return f"{data.get('city', '')}, {data.get('region', '')}, {data.get('country', '')}"

def uk_to_us(text):
    return re.sub(r"sation\b", "zation", text)