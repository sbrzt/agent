# functions/run_python_file.py

import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    try:
        if os.path.commonpath([working_directory]) != os.path.commonpath([working_directory, full_path]):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: File "{file_path}" not found'

        command = ["python3", full_path] + args
        completed_process = subprocess.run(command, timeout=30, capture_output=True, text=True)

        output = f"STDOUT: {completed_process.stdout}, STDERR: {completed_process.stderr}"

        if completed_process.returncode != 0:
            output += f"\nProcess exited with code {completed_process.returncode}"

    except subprocess.TimeoutExpired:
        return f"Error: Execution of {file_path} timed out."
    except Exception as e:
        return f"Error: executing Python file: {e}"

    return output
    

schema_run_python_file = genai.types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python script in the specified directory, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The path to the files to be read, relative to the working directory.",
            ),
            "args": genai.types.Schema(
                type=genai.types.Type.LIST,
                description="The arguments to be passed in the command used to run the script.",
            ),
        },
    ),
)