import time
import random
import os
import json
import datetime


def wait_random_time():
    # Generate a random number between 2 and 5
    random_time = random.randrange(2, 6)
    print(f"Waiting {random_time} seconds.")

    # Wait for the random number of seconds
    time.sleep(random_time)


def get_file_tree(d, s, origin):
    today = datetime.date.today()
    date_str = today.strftime("%Y-%m-%d")
    output_str = f"./data/{origin}/{d}/{s}/" + date_str + ".json"
    return output_str


def create_path(file_path):
    if os.path.exists(file_path):
        # Path already exists, so do nothing
        return None

    # Create the parent directory if it doesn't exist
    parent_dir = os.path.dirname(file_path)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    # Create the file itself
    with open(file_path, "w"):
        pass

    # Return the file path
    return file_path


def append_data(file, data):
    f_path = create_path(file)

    with open(file, "r+") as f:
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


def pprint_data(data):
    """Pretty prints a dictionary."""
    print(json.dumps(data, sort_keys=True, indent=4))
