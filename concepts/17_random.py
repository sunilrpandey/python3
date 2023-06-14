
# pypi.org,cowsay, pypi.org/project/requests

import random
import statistics

from random import choice

def demo_random_choices():
    dice_value = choice([ 2,3,4,5,6])
    print(dice_value)

def demo_suffle_list():
    nums = [ 2,3,4,5,6]
    random.shuffle(nums)
    print(nums)


if __name__ == "__main__" :
    # demo_random_choices()
    demo_suffle_list()
