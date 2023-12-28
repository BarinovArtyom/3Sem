import random

def gen_random1(num_count, begin, end):
    for x in range(num_count):
        yield random.randint(begin, end)
