# tests.py

from functions.get_files_info import get_files_info


def run_manual_tests():
    print(get_file_content({'file_path': 'main.py'}))
    print(write_file({'file_path': 'main.txt', 'content': 'hello'}))
    print(run_python_file({'file_path': 'main.py'}))
    print(get_files_info({'directory': 'pkg'}))
    

if __name__ == "__main__":
    run_manual_tests()