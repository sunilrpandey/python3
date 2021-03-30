import sys
import os
# open multiple file using with open
# with open('outfile.txt', 'w') as file_obj_2, open('sample.txt', 'r') as file_obj_1:
# line.strip() to remove newline character from teh line
# os.remove(path_of_file) - remove file OR os.unlink(filePath)

def write_file(name, mode):
    test_file = open(name, mode)
    print("mode -> ", test_file.mode)
    print(f"name -> {test_file.name}")
    test_file.write(bytes("Hello File : You have lot of stuff to store\n", "UTF-8"))
    test_file.write(bytes("Hi File : This is second line \n", "UTF-8"))
    test_file.write(bytes("Hi File : This is third line \n\n\n", "UTF-8"))

    next_line = "Here I want to add more\n"
    test_file.write(bytes(next_line, "UTF-8"))
    test_file.close()


def read_file(name, mode):
    test_file = open(name, mode)
    print("file detail :", test_file)

    print("mode -> ", test_file.mode)
    print("name -> ", test_file.name)
    file_content = test_file.read()
    print("Reading file content :\n", file_content)
    test_file.close()


def demo_file_handling():
    print("Demo: Write/Read/Remove file")
    write_file("file1.txt", "wb")
    read_file("file1.txt", "r+")

    os.remove("file1.txt")


def dump_file_content_using_with_open(filename):
    with open(filename) as f:
        print("name -> ", f.name)

        # file_content = f.read()
        # print(file_content)

        #   for one line at a time
        # file_content = f.readline()
        # print(file_content)

        file_content = f.readlines() # this will return comma separated lines
        print(file_content)
        print("\n\n\nThats all from the file")


def demo_file_operation_using_with_open():
    print("Demo: Write/Read file by opening by using with/open method")
    write_file("my_file.txt", "wb")
    dump_file_content_using_with_open("my_file.txt")

if __name__ == "__main__":
    demo_file_operation_using_with_open()
    
