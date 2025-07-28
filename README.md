# agent

An agentic CLI tool that:
- Accepts a coding task
- Chooses from a set of predefined functions to work on the task, for example:
    - Scan the files in a directory
    - Read a file's contents
    - Overwrite a file's contents
    - Execute the Python interpreter on a file
- Repeats step 2 until the task is complete or fails
