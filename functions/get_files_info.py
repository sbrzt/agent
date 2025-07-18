# functions/get_files_info.py

import os


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
