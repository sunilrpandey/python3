import sys
import os
import logging
class Base :
    def fun_impl(self):
        print("It's Base")
    def common_fun(self):
        logging.info("Info Logging Message")
        print(dir(logging.info))

if __name__ == "__main__":
    b = Base()
    print("Abstract class")
    b.common_fun()
