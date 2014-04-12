#!/usr/bin/env python

import util
# util.DEBUG = True
from util import *

def solution(count):
    print_case(count, '')

if __name__ == '__main__':
    count = int_input()
    loop(count, solution)