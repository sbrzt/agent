# functions/get_files_info.py

import os
from google import genai


def get_files_info(working_directory, directory="."):
    working_directory = os.path.realpath(os.path.abspath(working_directory))
    full_path = os.path.realpath(os.path.abspath(os.path.join(working_directory, directory)))

    if os.path.commonpath([working_directory]) != os.path.commonpath([working_directory, full_path]):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    contents = []
    for content in os.listdir(full_path):
        content_path = os.path.join(full_path, content)
        contents.append(f"- {content}: file_size={os.path.getsize(content_path)}, is_dir={os.path.isfile(content_path)}")
    return "\n".join(contents)


schema_get_files_info = genai.types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "directory": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)