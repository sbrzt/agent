# functions/write_file.py

import os


def write_file(working_directory, file_path, content):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if os.path.commonpath([working_directory]) != os.path.commonpath([working_directory, full_path]):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w") as f:
        f.write(content)
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'