import json
from pathlib import Path


# Store all JSON files inside the data folder.
DATA_DIR = Path("data")


def load_json(filename):
    """Load data from a JSON file"""

    file_path = DATA_DIR / filename

    try:
        # Open the file for reading.
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        # Handle a missing file without crashing the program.
        print(f"File not found: {file_path}")
        return None

    except json.JSONDecodeError:
        # Handle invalid or corrupted JSON data.
        print(f"Invalid JSON file: {file_path}")
        return None

    except PermissionError:
        # Handle cases where Python does not have permission to read the file.
        print(f"Permission denied: {file_path}")
        return None

    except OSError as error:
        # Handle other file-system related errors.
        print(f"Could not read file: {error}")
        return None


def save_json(filename, data):
    """Save Python data into a JSON file."""

    file_path = DATA_DIR / filename

    try:
        # Open the file for writing.
        with open(file_path, "w", encoding="utf-8") as file:
            # Convert Python data into formatted JSON.
            json.dump(data, file, indent=4)

    except PermissionError:
        # Handle cases where Python cannot write to the file.
        print(f"Permission denied: {file_path}")

    except TypeError:
        # Handle data that cannot be converted into JSON.
        print("The provided data cannot be converted to JSON.")

    except OSError as error:
        # Handle other file-system related errors.
        print(f"Could not save file: {error}")