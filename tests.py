# tests.py

from functions.get_files_info import get_files_info


def run_manual_tests():
    print(get_files_info({'directory': '.'}))
    print(get_files_info({'directory': 'pkg'}))

if __name__ == "__main__":
    run_manual_tests()