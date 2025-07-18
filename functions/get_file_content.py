import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    working_directory = os.path.realpath(os.path.abspath(working_directory))
    full_path = os.path.realpath(os.path.abspath(os.path.join(working_directory, file_path)))

    if os.path.commonpath([working_directory]) != os.path.commonpath([working_directory, file_path]):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(file_path, "r") as f:
        contents = f.read(MAX_CHARS)
        if os.path.getsize(file_path) > MAX_CHARS:
            return contents + f'[...File "{file_path}" truncated at 10000 characters]'
