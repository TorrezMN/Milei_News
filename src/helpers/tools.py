import json


import os

def get_or_create_file(file_path, content=""):
    # Split the file path into its components
    components = file_path.split("/")

    # Create the directories if they don't exist
    for component in components[:-1]:
        if not os.path.exists(component):
            os.makedirs(component)

    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(content)

    return open(file_path, "r+")


def append_data(file, data):
    with open(file, 'r+') as f:
        try:
            # Load existing JSON data
            existing_data = json.load(f)
        except json.JSONDecodeError:
            # File is empty or invalid JSON, create an empty list
            existing_data = []

        # Append new data to the existing data
        existing_data.append(data)

        # Reset the file position to the beginning
        f.seek(0)

        # Overwrite the file with the updated data
        json.dump(existing_data, f, indent=4)

