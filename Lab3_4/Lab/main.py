from field import *
from gen_random import *
from unique import *
from print_result import *
from sort import *
from cm_timer import *
import json

with open('data_light.json', 'r', encoding='utf-8') as dat:
    data = json.load(dat)

@print_result
def f1(arg):
    return sorted(list(Unique([j['job-name'] for j in arg], ignore_case = True)))

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x}, с опытом Python", arg))

@print_result
def f4(arg):
    salary = gen_random1(1, 100000, 200000)
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(arg, salary)]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))