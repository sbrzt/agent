# functions/get_file_content.py

import os
from google import genai
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if os.path.commonpath([working_directory]) != os.path.commonpath([working_directory, full_path]):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(full_path, "r") as f:
        contents = f.read(MAX_CHARS)
        if os.path.getsize(full_path) > MAX_CHARS:
            return contents + f'[...File "{full_path}" truncated at 10000 characters]'
        return contents

    
schema_get_file_content = genai.types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the contents of the files in the specified directory, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The path to the files to be read, relative to the working directory.",
            ),
        },
    ),
)