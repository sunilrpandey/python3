import sys
import os

from base import Base


class Derived(Base):
    def fun_impl(self):
        # self.common_fun()
        print("It's Derived")
