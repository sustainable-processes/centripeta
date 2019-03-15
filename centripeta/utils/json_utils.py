"""
JSON Wrappers

.. moduleauthor:: Graham Keenan <https://github.com/ShinRa26>
"""

import json

def read_json(filepath):
    """
    Reads a JSON file and returns a python dictionary

    Args:
        filepath (str): Fiel to read

    Returns:
        data (Dict): Python dictionary representation of the JSON data
    """
    with open(filepath) as f:
        return json.load(f)

def write_json(filepath, data):
    """
    Writes a python dictionary to a JSON file

    Args:
        filepath (str): File to write to
        data (Dict): Data to write to JSON
    """
    with open(filepath, "w") as f:
        json.dump(data, f)