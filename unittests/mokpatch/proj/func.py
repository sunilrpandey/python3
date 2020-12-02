from subprocess import check_output


def print_ls():
    """
    prints content of the string
    """
    # return check_output(['ls']).split()
    print(check_output(["ls"]).split())


if __name__ == "__main__":
    print_ls()
