import sys
import os

def create_open_file(name, mode) :
    test_file = open(name,mode)
    print("mode -> ", test_file.mode)
    print("name -> {test_file.name}")
    test_file.write(bytes("Hello File : You have lot of stuff to store\n", 'UTF-8'))
    #next_line = "Here I want to add more\n"
    #test_file.write(next_line)
    test_file.close()

def read_file(name, mode) :
    test_file = open(name,mode)
    print("file detail :",test_file)

    print("mode -> ", test_file.mode)
    print("name -> ", test_file.name)
    file_content = test_file.read()
    print(file_content)
    test_file.close()

def demo_file_handling():
    create_open_file("my_file.txt","wb")
    read_file("my_file.txt","r+")

    os.remove("my_file.txt")
    
demo_file_handling()