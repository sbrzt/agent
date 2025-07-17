from functions.get_files_info import get_files_info


def run_manual_tests():
    print("Result for current directory:")
    print(get_files_info("calculator", "."), end="\n\n")

    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"), end="\n\n")

    print("Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"), end="\n\n")

    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"), end="\n\n")

if __name__ == "__main__":
    run_manual_tests()